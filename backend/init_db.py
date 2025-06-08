from app import app
from database import db
from models import User, Product, ChatLog

with app.app_context():
    db.create_all()
    print("✅ Database and tables created successfully!")
