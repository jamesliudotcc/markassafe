from fastapi import APIRouter

from app.entity.adventure import Adventure, CreateAdventure
from app.service.service import (
    create_adventure,
    get_adventure,
)

router = APIRouter(prefix="/adventure")


@router.get("/{adventure_id}", response_model=Adventure)
async def get_an_adventure(adventure_id: int):
    return get_adventure(adventure_id)

@router.post("/", response_model=Adventure)
async def post_adventure(adventure: CreateAdventure):
    return create_adventure(Adventure.from_orm(adventure))

@router.put("/{adventure_id}", response_model=Adventure)
async def update_adventure(adventure_id: int, status: str):
    # TODO fix service layer to use the adventure object directly.
    pass
