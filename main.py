from fastapi import FastAPI
import json
import os
from api.batteraskcat_api import router as batteraskcat_router

app = FastAPI()

# Load cards from JSON file
def load_cards():
    cards_file = os.path.join(os.path.dirname(__file__), "cards.json")
    try:
        with open(cards_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return empty dict if cards.json doesn't exist
        return {}

cards = load_cards()

# Include the API router
app.include_router(batteraskcat_router)
