from typing import Union
from bertopic import BERTopic
from types import TextFile, ScientificArticle
from utils.FileHelpers import loadPickle, savePickle


def createTopicEmbedding(textFiles: list[Union[TextFile, ScientificArticle]]) -> dict[str, list[str]]:
    topic_model = BERTopic()

    docs = []
    # TODO:
    # See if removing stopwords improves cluster performance,
    # or maybe just need more articles?
    # https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
    for textFile in textFiles:
        docs.append(textFile["file_content"])

    topics, probs = topic_model.fit_transform(docs)

    topicIndex: dict[str, list[str]] = {}

    for topic, textFile in zip(topics, textFiles):
        if topic in topicIndex:
            topicIndex[topic].append(textFile["file_id"])
        else:
            topicIndex[topic] = [textFile["file_id"]]

    # TODO: Learn how to just use the embedding so we can ditch this index
    savePickle(topicIndex, "./models/indexes/topicIndex.pickle")
    topic_model.save("./models/topic-model")


# TODO: Make this not a cold start
def inferTopic(text: str):
    topic_model = BERTopic.load("./models/topic-model")
    topicIndex = loadPickle("./models/indexes/topicIndex.pickle")
    topics, _ = topic_model.transform([text])

    # print(f"Topics found for associated text: {topics}")

    results_dict: dict[str, list[str]] = {}
    for topic in topics:
        if topic in topicIndex and topic not in results_dict:
            print(f"Results found for topic: {topic}")
            results_dict[topic] = topicIndex[topic]
        elif topic in topicIndex and topic in results_dict:
            print(f"Found duplicate additional results for: {topic}")
            results_dict[topic].extend(topicIndex[topic])

    return results_dict


def loadAndPrint() -> None:
    topic_model = BERTopic.load("./models/topic-model")

    freq = topic_model.get_topic_info()
    print(freq.head(5))
