from typing import Optional
from uuid import UUID
from pydantic import ConfigDict, FilePath, HttpUrl
from ragchat.domain.kernel.entity import Entity

class Document(Entity):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    loaded_from_url: Optional[HttpUrl] = None
    loaded_from_path: Optional[FilePath] = None