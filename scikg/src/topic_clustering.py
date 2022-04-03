from bertopic import BERTopic
from scikg_types.DocumentTypes import TextFile
from utils.FileHelpers import loadPickle, savePickle

def createTopicIndex(textFiles: list[TextFile]) -> dict[str, list[str]]:
    topic_model = BERTopic()

    docs = []
    # TODO: See if removing stopwords improves cluster performance, or maybe just need more articles?
    # https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
    for textFile in textFiles:
        docs.append(textFile['file_content'])
    
    topics, probs = topic_model.fit_transform(docs)

    topicIndex: dict[str, list[str]] = {}
    
    for topic, textFile in zip(topics, textFiles):
        if topic in topicIndex:
                topicIndex[topic].append(textFile["file_id"])
        else:
            topicIndex[topic] = [textFile["file_id"]]

    savePickle(topicIndex, "./models/indexes/topicIndex.pickle")
    topic_model.save("./models/topic-model")

    return topicIndex

# TODO: Make this not a cold start
def inferTopic(text: str): 
    topic_model = BERTopic.load("./models/topic-model")
    topicIndex = loadPickle("./models/indexes/topicIndex.pickle")
    topics, _ = topic_model.transform([text])

    print(f"Topics found for associated text: {topics}")

    for topic in topics:
        if topic in topicIndex:
            print(f"Topic: {topic}, related files: {topicIndex[topic]}")

def loadAndPrint():
    topic_model = BERTopic.load("./models/topic-model")

    freq = topic_model.get_topic_info(); 
    print(freq.head(5))