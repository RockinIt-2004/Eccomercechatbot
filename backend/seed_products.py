from app import app
from database import db
from models import Product
import random

def seed_products():
    with app.app_context():
        db.create_all()

        # Clear existing products
        Product.query.delete()

        categories = ['mobile', 'laptop', 'book', 'tablet', 'headphones']
        product_names = {
            'mobile': ['Redmi Note 11', 'Samsung Galaxy M13', 'iPhone 13', 'Realme 9', 'OnePlus Nord'],
            'laptop': ['Dell Inspiron', 'HP Pavilion', 'Lenovo ThinkPad', 'MacBook Air', 'Asus ZenBook'],
            'book': ['The Alchemist', 'Atomic Habits', 'Deep Work', 'Clean Code', 'Python Crash Course'],
            'tablet': ['iPad Mini', 'Samsung Galaxy Tab', 'Amazon Fire', 'Lenovo Tab', 'Microsoft Surface Go'],
            'headphones': ['Sony WH-1000XM4', 'Bose QuietComfort', 'JBL Tune', 'Apple AirPods', 'Sennheiser HD']
        }

        # Generate 100 products
        count_per_category = 100 // len(categories)

        for category in categories:
            names = product_names[category]
            for i in range(count_per_category):
                name = random.choice(names)
                price = round(random.uniform(20.0, 1000.0), 2)
                description = f"{name} is one of our best {category} products with excellent reviews."
                
                product = Product(
                    name=name,
                    category=category,
                    price=price,
                    description=description
                )
                db.session.add(product)

        db.session.commit()
        print("✅ Seeded 100 real-world products successfully.")

if __name__ == '__main__':
    seed_products()
