import spacy
import opennre

from utils.FileHelpers import loadFile
from utils.PrintHelpers import show_ents


nlp = spacy.load("en_core_web_sm")

doc = loadFile("./data/polar_vortex.txt")

results = nlp(doc)

show_ents(results)

model = opennre.get_model('wiki80_cnn_softmax')
model.infer({'text': doc})