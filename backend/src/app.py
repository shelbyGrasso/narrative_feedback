from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from analyze_text import router as analyze_text_router

# Create the main FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include the analyze_text router
app.include_router(analyze_text_router, prefix="/analyze", tags=["analyze"])

# Future routes can also be added here
# e.g., app.include_router(other_router, prefix="/other", tags=["other"])
