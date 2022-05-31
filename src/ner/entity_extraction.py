from typing import Union
import pke
from nltk.corpus import wordnet
from scikg_types.DocumentTypes import TextFile, ScientificArticle

from utils.FileHelpers import loadPickle, savePickle


def inferIndex(text):
    extractor = pke.unsupervised.TopicRank()
    keyPhraseIndex: dict[str, list[str]] = loadPickle(
        "./models/indexes/keyPhraseIndex.pickle"
    )

    extractor.load_document(input=text, language="en")
    extractor.candidate_selection()
    extractor.candidate_weighting()

    # Get the N-best candidates (here, 5) as keyphrases
    keyphrases = extractor.get_n_best(n=5, stemming=False)

    # Grab synonyms for each candidate
    keyphrases_and_synonyms = set()
    for (candidate, score) in keyphrases:
        # Add the base keyphrase
        keyphrases_and_synonyms.add(candidate)

        # TODO: Possible restrict how many syns we pick from?
        # Add related words
        for syn in wordnet.synsets(candidate):
            for l in syn.lemmas():
                keyphrases_and_synonyms.add(l.name())

    results_dict: dict[str, list[str]] = {}
    for key in keyphrases_and_synonyms:
        if key in keyPhraseIndex and key not in results_dict:
            print(f"Results found for key: {key}")
            results_dict[key] = keyPhraseIndex[key]
        elif key in keyPhraseIndex and key in results_dict:
            print(f"Found duplicate key, adding additional results for: {key}")
            results_dict[key].extend(keyPhraseIndex[key])

    return results_dict


def createKeyphraseIndex(textFiles: list[Union[TextFile, ScientificArticle]]) -> None:
    # TODO: Some defensive coding here
    extractor = pke.unsupervised.TopicRank()

    keyphraseIndex: dict[str, list[str]] = {}
    for textFile in textFiles:

        extractor.load_document(input=textFile["file_content"], language="en")
        extractor.candidate_selection()
        extractor.candidate_weighting()

        # Get the N-best candidates (here, 5) as keyphrases
        keyphrases = extractor.get_n_best(n=5, stemming=False)

        # Grab synonyms for each candidate
        keyphrases_and_synonyms = set()
        for (candidate, score) in keyphrases:
            # Add the base keyphrase
            keyphrases_and_synonyms.add(candidate)

            # TODO: Possible restrict how many syns we pick from?
            # Add related words
            for syn in wordnet.synsets(candidate):
                for l in syn.lemmas():
                    keyphrases_and_synonyms.add(l.name())

        for key in keyphrases_and_synonyms:
            # check if the key is already present
            if key in keyphraseIndex:
                keyphraseIndex[key].append(textFile["file_id"])
            else:
                keyphraseIndex[key] = [textFile["file_id"]]

    # Save the file as a pickle
    savePickle(keyphraseIndex, "./models/indexes/keyPhraseIndex.pickle")