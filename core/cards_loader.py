import json
import os


def load_cards():
    """Load cards from JSON file"""
    cards_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cards.json")
    try:
        with open(cards_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return empty dict if cards.json doesn't exist
        return {}


# Load cards once when module is imported
cards = load_cards() 