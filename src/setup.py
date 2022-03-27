from entity_extraction import createKeyphraseIndex
from scikg_types.DocumentTypes import TextFile

from utils.FileHelpers import loadFile, loadTextFilesBulk
from utils.PrintHelpers import show_ents


textFiles: list[TextFile] = loadTextFilesBulk("./data/wikipedia")

keyphraseIndex: dict[str, list[str]] = createKeyphraseIndex(textFiles)
print(keyphraseIndex)

#topicIndex: dict[str, list[str]] = createTopicIndex(textFiles)