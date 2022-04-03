import spacy

from utils.FileHelpers import loadFile
from utils.PrintHelpers import show_ents


nlp = spacy.load("en_core_web_sm")

doc = loadFile("./data/wikipedia/Advection.txt")

results = nlp(doc)

show_ents(results)