import os
import requests
from fastapi import APIRouter

from mock_data import MOCK_CENTERS

# ==========================================
# GEOLOCATION ROUTER CONFIGURATION
# ==========================================

router = APIRouter()

# ==========================================
# GEOLOCATION & GOOGLE PLACES API ENDPOINT
# ==========================================

@router.get("/centers")
async def get_centers(lat: float, lng: float):
    api_key = os.getenv("GOOGLE_PLACES_API_KEY")
    
    # FALLBACK 1: Missing or unconfigured API Key
    if not api_key or api_key == "your_actual_api_key_here":
        return {
            "user_location": {"lat": lat, "lng": lng},
            "results": MOCK_CENTERS,
            "is_fallback": True,
            "message": "Missing API Key. Displaying mock locations."
        }

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": 5000,
        "keyword": "recycling center OR e-waste OR scrap metal",
        "key": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=5) # 5 second timeout
        data = response.json()
        
        # FALLBACK 2: Google API Error (Quota exceeded, billing issue, etc.)
        if data.get("status") not in ["OK", "ZERO_RESULTS"]:
            return {
                "user_location": {"lat": lat, "lng": lng},
                "results": MOCK_CENTERS,
                "is_fallback": True,
                "error": data.get("status"),
                "message": "Map service unavailable. Displaying mock locations."
            }

        parsed_results = []
        for place in data.get("results", [])[:5]: 
            parsed_results.append({
                "id": place.get("place_id"),
                "name": place.get("name"),
                "address": place.get("vicinity"),
                "lat": place["geometry"]["location"]["lat"],
                "lng": place["geometry"]["location"]["lng"],
                "rating": place.get("rating", "N/A")
            })

        return {
            "user_location": {"lat": lat, "lng": lng},
            "results": parsed_results,
            "is_fallback": False
        }
        
    except Exception as e:
        # FALLBACK 3: Network error or timeout talking to Google
        return {
            "user_location": {"lat": lat, "lng": lng},
            "results": MOCK_CENTERS,
            "is_fallback": True,
            "error": str(e),
            "message": "Network timeout. Displaying mock locations."
        }