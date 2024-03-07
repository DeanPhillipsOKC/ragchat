import requests
from typing import Optional, Union
from uuid import UUID
from pydantic import BaseModel, ConfigDict, validator, FilePath
from ragchat.domain.kernel.entity import Entity
from magika import Magika
import re


def is_url(string: str) -> bool:
    # Simple regex for demonstration; consider using a more robust solution for production
    return re.match(r"https?://", string) is not None


class Document(Entity):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    source: Optional[Union[str, FilePath]] = None
    type: Optional[str] = None

    @validator("type", always=True)
    def set_type(cls, v, values, **kwargs):
        source = values.get("source")
        if source:
            if is_url(source):
                response = requests.get(source)
                content = response.content
            else:  # source is assumed to be a FilePath
                with open(source, "rb") as f:
                    content = f.read()
            magika = Magika()
            file_type = magika.identify_bytes(content)
            return file_type.output.ct_label
        return v
