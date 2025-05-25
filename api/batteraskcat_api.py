from fastapi import APIRouter
from core.one_card_logic import one_card

router = APIRouter()


@router.get("/one_card_info")
async def get_one_card():
    card_name, card_description, card_display_name = await one_card()
    return {"card_name": card_name, "card_description": card_description, "card_display_name": card_display_name}
