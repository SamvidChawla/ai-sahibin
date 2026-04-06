# ==========================================
# STATIC CONTENT & REAL-WORLD FALLBACK DATA
# ==========================================

DISPOSAL_INSTRUCTIONS = {
    "plastic": {
        "category": "Plastic",
        "recyclable": True,
        "hazard_level": "Low",
        "steps": [
            "Rinse out any food or liquid residue thoroughly.",
            "Remove non-plastic components like lids or paper labels.",
            "Crush the item to save space.",
            "Place in the blue municipal recycling bin (Dry Waste)."
        ],
        "warning": "Do not mix with wet kitchen waste.",
        "carbon": {
            "kg_co2": 6.0,
            "label": "per kg if landfilled",
            "tip": "Recycling plastic saves ~6kg CO₂ per kg vs landfill disposal."
        }
    },
    "organic": {
        "category": "Organic",
        "recyclable": False,
        "hazard_level": "None",
        "steps": [
            "Ensure no plastic bags or rubber bands are mixed in.",
            "Store in a compostable bag or green bin (Wet Waste).",
            "Can be used for home composting or municipal collection."
        ],
        "warning": "Avoid adding large amounts of dairy or meat to home compost.",
        "carbon": {
            "kg_co2": 1.5,
            "label": "per kg if sent to landfill",
            "tip": "Composting organic waste produces 1.5kg less CO₂ vs landfill methane."
        }
    },
    "e-waste": {
        "category": "E-Waste",
        "recyclable": True,
        "hazard_level": "High",
        "steps": [
            "Do not throw in regular trash bins.",
            "Tape over battery terminals.",
            "Take to a specialized e-waste collection center or authorized recycler."
        ],
        "warning": "Lithium batteries can cause fires if crushed in garbage trucks.",
        "carbon": {
            "kg_co2": 20.0,
            "label": "per device if landfilled",
            "tip": "Proper e-waste recycling recovers rare metals and prevents ~20kg CO₂ equivalent."
        }
    },
    "metal": {
        "category": "Metal",
        "recyclable": True,
        "hazard_level": "Medium",
        "steps": [
            "Rinse cans to remove food residue.",
            "Place in the blue municipal recycling bin (Dry Waste)."
        ],
        "warning": "Ensure aerosol cans are completely empty before disposal.",
        "carbon": {
            "kg_co2": 9.0,
            "label": "per kg saved by recycling",
            "tip": "Recycling aluminium uses 95% less energy than producing new metal."
        }
    },
    "glass": {
        "category": "Glass",
        "recyclable": True,
        "hazard_level": "Medium",
        "steps": [
            "Rinse out any food or liquid residue.",
            "Do not break the glass intentionally.",
            "Wrap safely if broken to prevent injury to sanitation workers.",
            "Place in the designated glass recycling bin."
        ],
        "warning": "Mirrors, lightbulbs, and window glass are treated differently than bottle glass.",
        "carbon": {
            "kg_co2": 0.3,
            "label": "per bottle saved by recycling",
            "tip": "Recycling one glass bottle saves enough energy to power a bulb for 4 hours."
        }
    }
}

# REAL-WORLD DELHI-NCR CENTERS (FALLBACKS)
MOCK_CENTERS = [
    {
        "id": "delhi_1",
        "name": "MCD Waste to Energy Plant",
        "address": "Okhla Phase III, New Delhi",
        "lat": 28.5360, 
        "lng": 77.2713, 
        "rating": 4.2,
        "type": "Municipal/Multi-Category"
    },
    {
        "id": "delhi_2",
        "name": "Namo E-Waste Management Ltd",
        "address": "14/1, Main Mathura Rd, Faridabad",
        "lat": 28.3600, 
        "lng": 77.3100, 
        "rating": 4.7,
        "type": "E-Waste Specialist"
    },
    {
        "id": "delhi_3",
        "name": "Attero Recycling Center",
        "address": "H-59, Sector 63, Noida",
        "lat": 28.6210, 
        "lng": 77.3880, 
        "rating": 4.5,
        "type": "E-Waste & Metals"
    },
    {
        "id": "delhi_4",
        "name": "Chintan Environmental Research Group",
        "address": "222, Ratendon Rd, New Delhi",
        "lat": 28.6015,
        "lng": 77.2270,
        "rating": 4.8,
        "type": "Organic & Plastic"
    },
    {
        "id": "delhi_5",
        "name": "SWACHH Multi-Waste Collection Hub",
        "address": "Plot No. 5, Sector 18, Gurugram",
        "lat": 28.4800,
        "lng": 77.0800,
        "rating": 4.1,
        "type": "Multi-Category"
    }
]