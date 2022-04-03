from entity_extraction import createKeyphraseIndex, inferIndex
from infer.index_ranking import rank_index_results
from scikg_types.DocumentTypes import TextFile
from topic_clustering import createTopicIndex, inferTopic

from utils.FileHelpers import loadFile, loadTextFilesBulk
from utils.PrintHelpers import show_ents

import time

# starting time
start = time.time()
# textFiles: list[TextFile] = loadTextFilesBulk("./data/wikipedia")

# keyphraseIndex: dict[str, list[str]] = createKeyphraseIndex(textFiles)

# topicIndex: dict[str, list[str]] = createTopicIndex(textFiles)

text = "Fungi, a major element of atmospheric bioaerosols, are capable of existing and surviving in the air for extended periods of time."
keyphrase_results: dict[str, list[str]] = inferIndex(text)
topic_results: dict[str, list[str]] = inferTopic(text)

rank_index_results(keyphrase_results, topic_results)

# end time
end = time.time()

# total time taken
print("Execution time of the program is- ", end - start)
