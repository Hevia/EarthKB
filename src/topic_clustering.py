from bertopic import BERTopic
from scikg_types.DocumentTypes import TextFile

def createTopicIndex(textFiles: list[TextFile]) -> None:
    topic_model = BERTopic()

    docs = []
    for textFile in textFiles:
        docs.append(textFile['file_content'])
    
    topics, probs = topic_model.fit_transform(docs)

    topic_model.save("./models/topic-model")

    topic_model.get_topics()