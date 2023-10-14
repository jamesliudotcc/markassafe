from fastapi import APIRouter

from app.entity.user import InputUser, User
from app.service.service import create_user, get_one_user

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user(user_id: int):
    return get_one_user(user_id)


@router.post("/")
def create_a_user(user: InputUser) -> User:
    # TODO Start here.
    # Instead of using a basemodel, just accept the User model,
    # and always strip the ID.
    return create_user(User.from_orm(user))
