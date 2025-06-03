import random
from cards import cards


async def get_random_card():
    card_types = list(cards.keys())
    card_type = random.choice(card_types)
    card_name = random.choice(list(cards[card_type].keys()))
    card_data = cards[card_name]
    return card_name, card_data


async def one_card():
    card_name, card_data = await get_random_card()
    card_description = card_data["description"]

    return card_name, card_description, card_data["display_name"]
