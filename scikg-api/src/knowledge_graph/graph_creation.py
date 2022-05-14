from typing import Union
from scikg_types.DocumentTypes import TextFile, ScientificArticle

def createKnowledgeGraph(docs: list[Union[TextFile, ScientificArticle]]) -> None:
    return