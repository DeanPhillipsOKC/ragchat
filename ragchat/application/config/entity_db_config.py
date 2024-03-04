from pydantic import BaseModel

class EntityDbConfig(BaseModel):
    path: str