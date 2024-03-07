from typing import Optional, Union
from uuid import UUID
from pydantic import ConfigDict, FilePath, HttpUrl
from ragchat.domain.kernel.entity import Entity

class Document(Entity):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    source: Optional[Union[HttpUrl, FilePath]] = None