from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from mock_data import DISPOSAL_INSTRUCTIONS
import detect 
import centers 

# ==========================================
# APP INITIALIZATION & MIDDLEWARE
# ==========================================

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="AI-SahiBin API")

# TODO: Restrict these CORS origins before deployment if time permits.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach the modular routers
app.include_router(detect.router)
app.include_router(centers.router)

# ==========================================
# STATIC DISPOSAL INFORMATION ENDPOINT
# ==========================================

@app.get("/info/{category}")
async def get_disposal_info(category: str):
    # TODO: Add fuzzy search logic here later so variations like "plastic_bottle" still map to "plastic".
    
    normalized_category = category.lower()
    
    if normalized_category not in DISPOSAL_INSTRUCTIONS:
        raise HTTPException(status_code=404, detail="Disposal information not found for this category.")
        
    return DISPOSAL_INSTRUCTIONS[normalized_category]