from uuid import UUID

class EntityNotFoundException(Exception):
    """Exception raised when an entity is not found in the database."""
    def __init__(self, entity_id: UUID, message="Entity not found"):
        self.entity_id = entity_id
        self.message = f"{message}: {entity_id}"
        super().__init__(self.message)
