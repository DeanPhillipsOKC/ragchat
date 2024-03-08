from pydantic import BaseModel, root_validator, HttpUrl, FilePath
from typing import Optional, Union
import requests
import re

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

    @root_validator
    def load_and_identify_content(cls, values):
        source = values.get('source')
        if source:
            content = None
            if is_url(str(source)):  # Check if source is a URL
                response = requests.get(source)
                content = response.content
            else:  # Assume source is a FilePath
                with open(source, "rb") as f:
                    content = f.read()

            # Check if the content is HTML
            if is_html(content):
                file_type = 'html'
            else:
                # Placeholder for using Magika or other type identification logic
                file_type = 'unknown'  # Modify this line with actual identification logic

            values['content'] = content
            values['type'] = file_type
        return values
