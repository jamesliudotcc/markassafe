from app.entity.adventure import Adventure
from app.entity.user import User
from app.repository.in_memory import in_memory_repository
from app.service import service


def test_create_user():
    in_memory_repository.delete_all()
    user = User(name="Test", email="test@example.com", phone="206-555-1234")

    service.create_user(user)
    assert in_memory_repository.get_one("User", {"id": user.id}).name == user.name

def test_happy_path():
    in_memory_repository.delete_all()

    # Create a test user
    user = User(name="Test", email="test@example.com", phone="206-555-1234")
    created_user = service.create_user(user)

    # Create adventure
    adventure = Adventure(user_id=created_user.id, location="Seattle", status="ready")
    created_adventure = service.create_adventure(adventure)

    assert created_adventure.id is not None
    assert created_adventure.user_id == 1
    assert created_adventure.status == "ready"

    # Start adventure
    service.adventure_to_started(created_adventure.id)

    assert created_adventure.status == "started"

    # Return from adventure
    service.adventure_to_returned(created_adventure.id)

    assert created_adventure.status == "returned"

    # Contact after return
    service.adventure_to_contacted(created_adventure.id)

    assert created_adventure.status == "contacted"