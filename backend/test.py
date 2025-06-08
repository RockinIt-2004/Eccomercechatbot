from app import app
from models import Product

with app.app_context():
    products = Product.query.limit(3).all()
    print(f"Found {len(products)} products")
    for p in products:
        print(f"Product: {p.name}, Price: {p.price}")
