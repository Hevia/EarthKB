import pke
from nltk.corpus import wordnet

from utils.FileHelpers import loadFile

sample = loadFile("./data/wikipedia/Advection.txt")

extractor = pke.unsupervised.TopicRank()
extractor.load_document(input=sample, language='en')
extractor.candidate_selection()
extractor.candidate_weighting()

# Get the N-best candidates (here, 5) as keyphrases
keyphrases = extractor.get_n_best(n=5, stemming=False)

# for each of the best candidates
for i, (candidate, score) in enumerate(keyphrases):
    
    # print out the its rank, phrase and score
    print("rank {}: {} ({})".format(i, candidate, score))

    # Grab similar keyphrases for insertion into the inverted index
    synonyms = []
    
    for syn in wordnet.synsets(candidate):
        for l in syn.lemmas():
            synonyms.append(l.name())
    
    print(f"Synonyms for {candidate}: {set(synonyms)}")
