from uuid import UUID

from ragchat.domain.kernel import Entity


class Collection(Entity):
    id: UUID
    name: str
