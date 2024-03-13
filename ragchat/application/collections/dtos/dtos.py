class ListCollectionsViewModel:
    def __init__(self, id: str, name: str, is_selected: bool):
        self.id = id
        self.name = name
        self.is_selected = is_selected
