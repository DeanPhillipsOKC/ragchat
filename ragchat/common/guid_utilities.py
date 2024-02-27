from uuid import UUID

def is_uuid4(candidate: str) -> bool:
    try:
        val = UUID(candidate, version=4)
        return val.version == 4
    except ValueError:
        return False
    
def to_uuid4(id: str) -> UUID:
    return UUID(id, version=4)
