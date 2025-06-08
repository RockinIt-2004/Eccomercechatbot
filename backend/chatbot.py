from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Product, ChatLog, db
from datetime import datetime
import re
chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/message', methods=['POST'])
@jwt_required()
def chatbot_message():
    user_id = get_jwt_identity()
    data = request.get_json()
    message = data.get('message', '').lower()

    # Default response
    response = "Sorry, I didn't understand that. Can you please rephrase?"

    # Rule-based chatbot logic
    if 'hello' in message or 'hi' in message:
        response = "Hello! How can I assist you with our products today?"

    elif 'recommend' in message:
        categories = ['mobile', 'laptop', 'book', 'tablet', 'headphones']
        recommendations = []

        for category in categories:
            products = Product.query.filter_by(category=category).limit(1).all()
            if products:
                product = products[0]
                recommendations.append(f"📦 *{category.capitalize()}*: {product.name} - ₹{product.price}")

        response = "Here are some product recommendations for you:\n\n" + "\n".join(recommendations)

    elif 'price' in message:
        all_products = Product.query.all()
        matched = None
        for p in all_products:
            if p.name.lower() in message:
                matched = p
                break
        if matched:
            response = f"The price of *{matched.name}* is ₹{matched.price}"
        else:
            response = "Sorry, I couldn't find that product."
    


    elif any(cat in message for cat in ['mobile', 'laptop', 'book', 'tablet', 'headphones']) and any(term in message for term in ['under', 'below', 'less than']):
        # Extract category
        category = next((cat for cat in ['mobile', 'laptop', 'book', 'tablet', 'headphones'] if cat in message), None)

        # Extract price using regex
        price_match = re.search(r'(\d{2,6})', message)  # Find number like 500, 29999, etc.
        if category and price_match:
            max_price = float(price_match.group(1))

            # Query filtered products
            products = Product.query.filter(Product.category.ilike(category), Product.price <= max_price).all()

            if products:
                product_list = '\n'.join([f"- {p.name} (₹{p.price})" for p in products])
                response = f"Here are some {category}s under ₹{max_price}:\n{product_list}"
            else:
                response = f"Sorry, no {category}s found under ₹{max_price}."
        else:
            response = "Please specify both category and price correctly."


    # Save chat interaction
    chat = ChatLog(
        user_id=user_id,
        user_message=data.get('message', ''),
        bot_response=response,
        timestamp=datetime.utcnow()
    )
    db.session.add(chat)
    db.session.commit()

    return jsonify({'response': response})
