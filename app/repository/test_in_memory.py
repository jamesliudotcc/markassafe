"""Test in-memory repository implementation."""

from typing import Optional

from app.entity.entity import Entity
from app.repository.in_memory import filter_query, in_memory_repository


class EntityWithId(Entity):
    id: Optional[int]


class AdventureLike(Entity):
    id: Optional[int]
    user_id: int
    active: bool = True


def test_filter_query_by_id_null_result():
    """When filtering by id, if the id does not result, an empty set is returned."""
    in_memory_repository.delete_all()
    results = [EntityWithId(id=1), EntityWithId(id=2)]
    assert filter_query(results, {"id": 3}) == []


def test_filter_query_by_id_result_exists():
    """When filtering by id, if the id exists in results, it is returned."""
    in_memory_repository.delete_all()
    results = [EntityWithId(id=1), EntityWithId(id=2)]
    assert filter_query(results, {"id": 1}) == [EntityWithId(id=1)]


def test_filter_query_by_user_id():
    """When filtering by user id, if the user id exists in results, those are returned.
    """
    in_memory_repository.delete_all()
    results = [
        AdventureLike(id=1, user_id=1),
        AdventureLike(id=2, user_id=1),
        AdventureLike(id=3, user_id=2),
    ]
    assert filter_query(results, {"user_id": 1}) == [
        AdventureLike(id=1, user_id=1),
        AdventureLike(id=2, user_id=1),
    ]


def test_filter_query_by_user_id_and_status():
    """When filtering by user id and active status, return the correct result"""
    in_memory_repository.delete_all()
    results = [
        AdventureLike(id=1, user_id=1),
        AdventureLike(id=2, user_id=1),
        AdventureLike(id=3, user_id=1, active=False),
        AdventureLike(id=4, user_id=2),
    ]
    assert filter_query(results, {"user_id": 1, "active": True}) == [
        AdventureLike(id=1, user_id=1),
        AdventureLike(id=2, user_id=1),
    ]


def test_add_auto_increments_id():
    """This is only necessary becaues we are not using a real db"""
    in_memory_repository.delete_all()
    in_memory_repository.add("adventure_like", AdventureLike(user_id=1))
    adventure_from_db = in_memory_repository.get("adventure_like")[-1]

    assert adventure_from_db.id == 1

    # And then do a second one.
    in_memory_repository.add("adventure_like", AdventureLike(user_id=1))
    adventure_from_db = in_memory_repository.get("adventure_like")[-1]

    assert adventure_from_db.id == 2


def test_update_adventure():
    in_memory_repository.delete_all()
    in_memory_repository.add("adventure_like", AdventureLike(user_id=1))
    in_memory_repository.update("adventure_like", 1, {"active": False})

    assert in_memory_repository.get("adventure_like", {"id": 1})[0] == AdventureLike(
        id= 1, user_id=1, active=False
    )
