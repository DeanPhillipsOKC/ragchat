from pydantic import BaseModel, HttpUrl, FilePath, model_validator
from typing import Optional, Union
import requests
import re
from magika import Magika

def is_html(content: bytes) -> bool:
    content_sample = content[:500].lower()  # Check the beginning of the content
    return b'<!doctype html' in content_sample or b'<html' in content_sample

def is_url(source: str) -> bool:
    return re.match(r'https?://', source)

class Document(BaseModel):
    id: str
    source: Optional[Union[HttpUrl, FilePath]] = None
    type: Optional[str] = None
    content: Optional[bytes] = None

    @model_validator(mode='after')
    def load_and_identify_content(self):
        if self.source:
            content = None
            src = self.source
            if is_url(str(src)):  # Check if source is a URL
                response = requests.get(src)
                content = response.content
            else:  # Assume source is a FilePath
                with open(src, "rb") as f:
                    content = f.read()

            # Check if the content is HTML
            if is_html(content):
                file_type = 'html'
            else:
                magica = Magika()
                result = magica.identify_bytes(content)
                file_type = result.output.ct_label

            self.content = content
            self.type = file_type
        return self
