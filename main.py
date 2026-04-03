from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

from mock_data import DISPOSAL_INSTRUCTIONS, MOCK_CENTERS

# ==========================================
# APP INITIALIZATION & MIDDLEWARE
# ==========================================

app = FastAPI(title="AI-SahiBin API")

# TODO: I need to restrict these CORS origins before the final demo so we don't get hit by random domains.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# ML INFERENCE ENDPOINT
# ==========================================

@app.post("/detect")
async def detect_waste(file: UploadFile = File(...)):
    # TODO: I need to get the YOLO inference script from the ML Engineer, load the .pt file into memory on startup, and pass this file to it instead of using random choice.
    
    available_categories = list(DISPOSAL_INSTRUCTIONS.keys())
    detected_category = random.choice(available_categories)
    
    return {
        "filename": file.filename,
        "category": detected_category,
        "confidence": round(random.uniform(0.70, 0.98), 2)
    }

# ==========================================
# DISPOSAL INFORMATION ENDPOINT
# ==========================================

@app.get("/info/{category}")
async def get_disposal_info(category: str):
    # TODO: I need to add a fuzzy search here later so if the ML model returns "plastic_bottle", it still maps to "plastic".
    
    normalized_category = category.lower()
    
    if normalized_category not in DISPOSAL_INSTRUCTIONS:
        raise HTTPException(status_code=404, detail="Disposal information not found for this category.")
        
    return DISPOSAL_INSTRUCTIONS[normalized_category]

# ==========================================
# GEOLOCATION & CENTERS ENDPOINT
# ==========================================

@app.get("/centers")
async def get_centers(lat: float, lng: float):
    # TODO: I need to write the `requests.get` call to the Google Places API here, pass in the lat/lng, and parse the JSON response. Using MOCK_CENTERS for now so UI is unblocked.
    
    # Simulating a small delay to test UI loading states
    return {
        "user_location": {"lat": lat, "lng": lng},
        "results": MOCK_CENTERS
    }