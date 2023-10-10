from collections import defaultdict

from app.entity.entity import Entity
from app.repository.abstract import AbstractRepository


def filter_query(result: set[Entity] | list[Entity], entity_query: dict) -> list[dict]:
    """Given a collection of results and an entity query, filter the results to only
    those matching the query."""
    return [
        r for r in result if all([getattr(r, k) == v for k, v in entity_query.items()])
    ]


class InMemoryRepository(AbstractRepository):
    """Database implemented as in-memory Python structures.

    Use a defaultdict to store types. Each key in the defaultdict
    contains a list of items.
    """

    def __init__(self):
        self.delete_all()

    def next_id(self, entity_type: str) -> int:
        """Given an entity type, give the correct next auto-increment id."""
        if not self.database[entity_type]:
            return 1
        return self.database[entity_type][-1].id + 1

    def delete_all(self):
        """Start over."""
        self.database = defaultdict(list)

    def add(self, entity_type: str, entity: Entity) -> Entity:
        """Add an entity to the default dict."""
        entity.id = self.next_id(entity_type)

        self.database[entity_type].append(entity)

        return entity

    def get(
        self,
        entity_type,
        entity_query: dict | None = None,
        skip: int = 0,
        stride: int = 10,
    ):
        """Get from the default dict."""
        if entity_type not in self.database:
            raise ValueError(f"Entity type {entity_type} does not exist.")

        if entity_query is None:
            entity_query = {}

        results = self.database[entity_type]
        filtered_results = filter_query(results, entity_query)

        return filtered_results[skip : skip + stride]

    def get_one(self, type, query):
        return self.get(type, query, stride=1)[0]

    def update(self, entity_type: str, entity_id: int, changes: dict | None) -> Entity:
        """Changes the object in the database"""
        match = self.get_one(entity_type, {"id": entity_id})

        for k, v in changes.items():
            setattr(match, k, v)

        return match


in_memory_repository = InMemoryRepository()
