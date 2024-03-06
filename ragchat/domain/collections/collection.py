from uuid import UUID

from pydantic import ConfigDict
from ragchat.domain.kernel.entity import Entity

class Collection(Entity):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
