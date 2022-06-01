from typing import Any, TypedDict


class TextFile(TypedDict):
    file_id: str
    file_content: str
    cleaned_content: str

class ScientificFigure(TypedDict):
    image: Any
    caption: str
class ScientificArticle(TypedDict):
    file_id: str
    figures: list[ScientificFigure]
    file_content: str
    cleaned_content: str
