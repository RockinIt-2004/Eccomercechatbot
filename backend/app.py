from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

from database import db
from auth import auth_bp
from chatbot import chatbot_bp
from models import Product

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data', 'ecommerce.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(chatbot_bp, url_prefix='/chat')

@app.route('/')
def home():
    return "E-commerce Chatbot Running!"

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('q', '')
    category = request.args.get('category', None)
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    products = Product.query

    if query:
        products = products.filter(Product.name.ilike(f'%{query}%'))

    if category:
        products = products.filter(Product.category == category)

    if min_price is not None:
        products = products.filter(Product.price >= min_price)

    if max_price is not None:
        products = products.filter(Product.price <= max_price)

    results = products.all()
    return jsonify([p.to_dict() for p in results])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables exist before running
    app.run(debug=True)
