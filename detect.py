from fastapi import APIRouter, File, UploadFile
import random

from mock_data import DISPOSAL_INSTRUCTIONS

# ==========================================
# ML ROUTER CONFIGURATION
# ==========================================

router = APIRouter()

# ==========================================
# DETECTION ENDPOINT
# ==========================================

@router.post("/detect")
async def detect_waste(file: UploadFile = File(...)):
    # TODO: Integrate the actual YOLO inference script from the ML Engineer here.
    # Once integrated, change is_fallback to False.
    
    # FALLBACK: Faking the ML output until the model is ready.
    available_categories = list(DISPOSAL_INSTRUCTIONS.keys())
    detected_category = random.choice(available_categories)
    
    return {
        "filename": file.filename,
        "category": detected_category,
        "confidence": round(random.uniform(0.70, 0.98), 2),
        "is_fallback": True 
    }