from pydantic import BaseModel


class ListDocumentsViewModel(BaseModel):
    id: str
    name: str
    type: str
