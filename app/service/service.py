"""Service layer"""

from app.config import Config
from app.entity.adventure import Adventure
from app.entity.user import User
from app.repository.in_memory import in_memory_repository
from app.texter.fake import fake_texter

map_config_to_repository = {"IN_MEMORY": in_memory_repository}

if Config.REPOSITORY not in map_config_to_repository.keys():
    raise NotImplementedError(f"Instead, select from {map_config_to_repository.keys()}")

# Use Python's closures to pass the repository
repository = map_config_to_repository[Config.REPOSITORY]
# TODO Allow other texters than fake
texter = fake_texter

def create_user(user: User):
    """Create a user"""
    return repository.add("User", user)


def get_one_user(user_id: int):
    """Get a user by ID"""
    return repository.get_one("User", {"id": user_id})


def create_adventure(adventure: Adventure):
    """Create an adventure"""
    return repository.add("Adventure", adventure)


def get_adventure(id: int):
    """Get an adventure by ID"""
    return repository.get("Adventure", id)


def adventure_to_started(adventure_id: int):
    """Transition adventure from ready to started"""
    # TODO: refactor repository into context manager
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.start()


def adventure_to_returned(adventure_id: int):
    """Transition adventure from started to returned"""
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.return_from()


def adventure_to_contacted(adventure_id: int):
    """Transition adventure from returned to contacted"""
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.contact(texter)
