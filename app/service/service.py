"""Service layer"""

from app.config import Config
from ..config import Config

implemented_repositories = {"IN_MEMORY"}

if Config.REPOSITORY not in implemented_repositories:
    raise NotImplementedError(
        f"Repositoyr not implemented. Select from {implemented_repositories}"
    )


def create_user(
    user,
):
    """Add a user"""
