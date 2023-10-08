from pydantic import BaseModel


class Entity(BaseModel):
    """Entities are hashable so that they can be compared, put in sets, etc."""

    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
