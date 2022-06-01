from typing import Union
from entity_extraction import createKeyphraseIndex
from types import TextFile, ScientificArticle
from topic_clustering import createTopicEmbedding

from utils.FileHelpers import loadTextFilesBulk
import multiprocessing

# This script is for setting up SciKG for first time runs on your own data.
# What this script does: Processes & cleans the data, creates indexes, graphs, & embeddings for searching.
# What this script DOESN'T do: Fetch data, start/serve the API
def process_text_data(textFiles: list[Union[TextFile, ScientificArticle]]) -> list[Union[TextFile, ScientificArticle]]:
    """ """
    return textFiles

# 1. Load & preprocess data
# Preprocessing steps: coref resolution, remove unusual characters
textFiles: list[TextFile] = loadTextFilesBulk("./data/wikipedia")

# 2. Index, Knowledge Graph, & Dense Vectors creation 
# We use an inverted index with keyphrases as keys to support a very basic standard search functionality
target_processes = [createKeyphraseIndex, createTopicEmbedding]
created_processes = []

for process in target_processes:
    created_processes.append(multiprocessing.Process(target=process, args=(textFiles,)))

for process in created_processes:
    process.start()

for process in created_processes:
    process.join()

# 4. Cleanup
