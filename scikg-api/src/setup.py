from ner import createKeyphraseIndex, inferIndex
from infer.index_ranking import rank_index_results
from scikg_types.DocumentTypes import TextFile
from topic_clustering import createTopicIndex, inferTopic

from utils.FileHelpers import loadFile, loadTextFilesBulk
from utils.PrintHelpers import show_ents

import time

# This script is for setting up SciKG for first time runs on your own data.

# 1. Load & preprocess data
textFiles: list[TextFile] = loadTextFilesBulk("./data/wikipedia")

# 2. Index creation 
# We use an inverted index with keyphrases as keys to support a very basic standard search functionality
keyphraseIndex: dict[str, list[str]] = createKeyphraseIndex(textFiles)

# We create topic embeddings for our 
topicIndex: dict[str, list[str]] = createTopicIndex(textFiles)

# 3. Knowledge Graph Creation

# 4. Cleanup
