from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base, engine
from app.feedback.controller import router as feedback_router
from app.user.controller import router as user_router
from app.session.controller import router as session_router
from app.interaction.controller import router as interaction_router
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Chatbot Backend API",
    description="A modular FastAPI backend for managing chatbot users, sessions, interactions, and feedback.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only local origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(session_router, prefix="/sessions", tags=["Sessions"])
app.include_router(interaction_router, prefix="/sessions", tags=["Interactions"])
app.include_router(feedback_router, prefix="/feedbacks", tags=["Feedback"])

@app.on_event("startup")
def on_startup():
    """
    Event handler for application startup.
    Creates all database tables if they don't exist.
    """
    print("Application startup: Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created (if not already existing).")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chatbot Backend API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
