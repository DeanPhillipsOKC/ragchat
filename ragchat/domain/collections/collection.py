from uuid import UUID

from pydantic import ConfigDict
from ragchat.domain.kernel.entity import Entity


class Collection(Entity):
    id: UUID
    name: str
