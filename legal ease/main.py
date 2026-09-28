from fastapi import FastAPI
from routes import router

# Initialize the FastAPI app
app = FastAPI(title="LegalEase API")

# Connect the routes from routes.py
app.include_router(router)
