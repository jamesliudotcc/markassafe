"""Service layer"""

from app.config import Config
from app.entity.adventure import Adventure
from app.entity.user import User
from app.repository.in_memory import in_memory_repository

map_config_to_repository = {"IN_MEMORY": in_memory_repository}

if Config.REPOSITORY not in map_config_to_repository.keys():
    raise NotImplementedError(f"Instead, select from {map_config_to_repository.keys()}")

repository = map_config_to_repository[Config.REPOSITORY]


def create_user(user: User, repository=repository):
    """Create a user"""
    return repository.add("User", user)

def get_user(user_id: int, repository=repository):
    """Get a user by ID"""
    return repository.get("User", user_id)

def create_adventure(adventure: Adventure, repository=repository):
    """Create an adventure"""
    return repository.add("Adventure", adventure)

def get_adventure(id: int, repository=repository):
    """Get an adventure by ID"""
    return repository.get("Adventure", id)

def adventure_to_started(adventure_id: int, repository=repository):
    """Transition adventure from ready to started"""
    # TODO: refactor repository into context manager
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.status = "started"

def adventure_to_returned(adventure_id: int, repository=repository):
    """Transition adventure from started to returned"""
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.status = "returned"

def adventure_to_contacted(adventure_id: int, repository = repository):
    """Transition adventure from returned to contacted"""
    adventure = repository.get_one("Adventure", {"id": adventure_id})
    adventure.status = "contacted"

