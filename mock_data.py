# ==========================================
# STATIC CONTENT & FALLBACK DATA
# ==========================================

DISPOSAL_INSTRUCTIONS = {
    "plastic": {
        "category": "Plastic",
        "recyclable": True,
        "hazard_level": "Low",
        "steps": [
            "Rinse out any food or liquid residue thoroughly.",
            "Remove non-plastic components like metal lids or paper labels if possible.",
            "Crush the item to save space.",
            "Place in the blue municipal recycling bin."
        ],
        "warning": "Do not bag recyclables; keep them loose."
    },
    "organic": {
        "category": "Organic",
        "recyclable": False,
        "hazard_level": "None",
        "steps": [
            "Ensure no plastic bags, stickers, or rubber bands are mixed in.",
            "Store in a compostable bag or green bin.",
            "Can be used for home composting or placed in municipal organics collection."
        ],
        "warning": "Avoid adding excessive amounts of meat or dairy to home composts to prevent pests."
    },
    "e-waste": {
        "category": "E-Waste",
        "recyclable": True,
        "hazard_level": "High",
        "steps": [
            "Do not throw in regular trash or standard recycling bins.",
            "Tape over battery terminals with clear tape.",
            "Wipe any personal data if the device has storage.",
            "Take to a specialized e-waste drop-off facility or retailer."
        ],
        "warning": "Batteries can leak toxic chemicals or cause fires if crushed in standard garbage trucks."
    },
    "cardboard": {
        "category": "Cardboard",
        "recyclable": True,
        "hazard_level": "Low",
        "steps": [
            "Empty the box of all packing materials (styrofoam, bubble wrap).",
            "Break down and flatten the box completely.",
            "Keep dry; wet cardboard cannot be recycled.",
            "Place in or next to the blue recycling bin."
        ],
        "warning": "Pizza boxes heavily soiled with grease belong in the organic/compost bin, not recycling."
    },
    "metal": {
        "category": "Metal",
        "recyclable": True,
        "hazard_level": "Medium",
        "steps": [
            "Rinse cans to remove food residue.",
            "Push the sharp lid inside the can and squeeze the top closed.",
            "Place in the blue municipal recycling bin."
        ],
        "warning": "Aerosol cans must be completely empty before recycling. Do not puncture them."
    }
}

# Used as a fallback if the Google Places API fails or key is missing
MOCK_CENTERS = [
    {
        "id": "mock_1",
        "name": "Green City Recycling Facility",
        "address": "123 Eco Way, Tech District",
        "lat": 28.6139, 
        "lng": 77.2090, 
        "rating": 4.5
    },
    {
        "id": "mock_2",
        "name": "Tech E-Waste Hub",
        "address": "45 Circuit Dr, Innovation Park",
        "lat": 28.6150, 
        "lng": 77.2150,
        "rating": 4.8
    },
    {
        "id": "mock_3",
        "name": "Community Scrap Yard",
        "address": "88 Greenbelt Ave",
        "lat": 28.6000,
        "lng": 77.2000,
        "rating": 4.0
    }
]