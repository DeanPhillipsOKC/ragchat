from typing import Union
from uuid import UUID

def is_uuid4(candidate: Union[str, UUID]) -> bool:
    try:
        if isinstance(candidate, UUID):
            return candidate.version == 4
        
        val = UUID(candidate, version=4)
        return val.version == 4
    except ValueError:
        return False

def to_uuid4(id: str) -> UUID:
    return UUID(id, version=4)
