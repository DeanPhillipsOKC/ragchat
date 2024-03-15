from typing import List, Any, Tuple
from pydantic import BaseModel


class TableUtilities:
    @staticmethod
    def convert_to_tabulate_headers_and_rows(
        objects: List[BaseModel],
    ) -> Tuple[List[str], List[List[Any]]]:
        """
        Converts a list of Pydantic model objects into headers and rows
        suitable for tabulate.

        Args:
            objects (List[BaseModel]): A list of Pydantic model objects.

        Returns:
            Tuple[List[str], List[List[Any]]]: A tuple containing a list of
            headers and a list of rows.
        """
        if not objects:
            return [], []

        # Assuming all objects are Pydantic models and have the same structure
        headers = list(objects[0].dict().keys())
        rows = [list(obj.dict().values()) for obj in objects]

        return headers, rows
