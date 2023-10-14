from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity_type, entity):
        """Add an entity."""
        raise NotImplementedError

    @abstractmethod
    def get(self, entity_type, entity_query: dict, skip: int = 0, stride: int = 10):
        """Get an entity."""
        raise NotImplementedError

    @abstractmethod
    def update(self, entity_type, entity_id: int, changes: dict):
        """Update an entity."""
        raise NotImplementedError
