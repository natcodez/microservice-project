🍲 Microservice-Based Recipe App

A learning project that demonstrates how to build a microservice architecture with FastAPI, JWT Authentication, SQLite databases, and a frontend client.
The system is composed of two microservices:

Auth Service – handles user login and issues JWT tokens.

Recipe Service – manages recipes (CRUD operations) and validates requests using JWT.

The project is fully Dockerized and can be run locally with docker-compose.

🚀 Features

Authentication Service

User login with username & password

Passwords hashed with bcrypt

JWT token generation with python-jose

Recipe Service

Secure endpoints with JWT authentication

SQLite database for recipe storage

Endpoints to add & fetch recipes

Frontend (menu.html)

Simple HTML/JS client

Login form + recipe management UI

Stores JWT and attaches it to API calls

Dockerized

Independent containers for each microservice

Runs with a single command: docker-compose up

📂 Project Structure
microservice-project/
│
├── backend/
│   ├── auth_service.py      # Authentication microservice
│   ├── recipe_service.py    # Recipe microservice
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Backend Dockerfile
│   └── *.db                 # SQLite databases
│
├── frontend/
│   └── menu.html            # Frontend client
│
├── docker-compose.yml       # Multi-container setup
├── users.db                 # User database (auth-service)
├── recipes.db               # Recipe database (recipe-service)
└── README.md                # Project documentation

⚡ Quickstart
1️⃣ Run Locally (without Docker)

Start Auth Service:

uvicorn backend.auth_service:app --reload --port 5000


Start Recipe Service:

uvicorn backend.recipe_service:app --reload --port 4000


Start Frontend:

npx http-server -p 5500


Access: http://localhost:5500/menu.html

2️⃣ Run with Docker

Build and run both services:

docker-compose up --build


Auth Service → http://localhost:5000

Recipe Service → http://localhost:4000

🔑 Authentication Flow

User logs in via Auth Service (POST /token)
→ returns JWT token

JWT is stored by frontend

Frontend sends JWT in headers:

Authorization: Bearer <token>


Recipe Service validates token → allows or rejects request

📌 API Endpoints
Auth Service (localhost:5000)

POST /token → Authenticate user & return JWT

Recipe Service (localhost:4000)

GET /recipes → Fetch all recipes (requires JWT)

POST /recipes → Add a new recipe (requires JWT)

🛠️ Tech Stack

Backend: FastAPI, SQLite, JWT (python-jose), bcrypt (passlib)

Frontend: HTML, JavaScript (Fetch API)

Containers: Docker, Docker Compose

🔮 Future Improvements

Add user registration (sign-up)

Extend Recipe Service with update & delete endpoints

Role-based access control (e.g., admin users)

Deployment to cloud providers (AWS, Render, GCP, etc.)

Replace SQLite with PostgreSQL/MySQL for production

📖 Learning Goals

This project was built to practice and understand:

Microservice architecture concepts

FastAPI for REST APIs

Authentication with JWT

Database integration with SQLite

Docker & Docker Compose for service orchestration

👏 Contributions, suggestions, and improvements are welcome!
