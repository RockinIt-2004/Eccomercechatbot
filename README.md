# Ecommerce Chatbot

An AI-powered chatbot integrated with an e-commerce platform backend and frontend, built with Flask (backend) and React (frontend). The chatbot assists users by recommending products, providing product details, and responding intelligently to queries.

---------------------------------------------------------------------------------------------------------------------------------

## Project Structure

ecommerce-chatbot/
│
├── backend/
│ ├── app.py # Flask app entry point
│ ├── auth.py # Authentication Blueprint (register/login)
│ ├── chatbot.py # Chatbot Blueprint (chat message handling)
│ ├── database.py # DB setup and initialization
│ ├── models.py # SQLAlchemy models (User, Product, ChatLog)
│ ├── seed_products.py # Script to populate products data
│ ├── requirements.txt # Python dependencies
│ ├── config.py # Configuration variables (DB URI, JWT secret, etc.)
│ ├── migrations/ # DB migration files (Flask-Migrate)
│ ├── tests/ # Backend tests
│ └── data/ # Contains SQLite DB file
│
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json # React dependencies & scripts


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Features

- User authentication (register/login) with JWT
- Chatbot with rule-based logic for product recommendation & price queries
- Products seeded with real product names and categories
- Chat interactions stored in database for logging
- Responsive React frontend with chat UI

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Setup Instructions

### Backend

1. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


2. Install dependencies:
pip install -r backend/requirements.txt

3. Seed the product database:
python backend/seed_products.py

4. Run the Flask app:
python backend/app.py




### Frontend

1. Navigate to the frontend folder and install dependencies:
cd frontend
npm install

2. Start the React app:
npm start

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage
Register or login to get your JWT token.
Use the chat interface to ask for product recommendations or price inquiries.

The chatbot will respond with relevant product information based on your query.

Technologies Used
Backend: Flask, SQLAlchemy, Flask-JWT-Extended, SQLite

Frontend: React, Axios, Bootstrap

Tools: VS Code, Postman for API testing

Potential Challenges and Solutions
Natural Language Variations: Handling different user input phrases was managed by simple keyword detection and pattern matching in chatbot logic.

Database Management: Implemented proper migrations and careful seeding to avoid data inconsistencies.

Authentication & API Integration: Managed JWT token refresh and Axios interceptors for seamless authentication flow between frontend and backend.

Debugging Cross-Origin Issues: Configured CORS headers properly for smooth frontend-backend communication.
