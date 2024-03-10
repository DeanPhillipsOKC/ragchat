from uuid import UUID

from ragchat.domain import Entity


class Collection(Entity):
    id: UUID
    name: str
