import spacy

def show_ents(doc):
    """
    A function to display the results of spacy's NER
    Source: https://towardsdatascience.com/named-entity-recognition-ner-using-spacy-nlp-part-4-28da2ece57c6
    """
    if doc.ents: 
        for ent in doc.ents: 
            print(ent.text + ' - ' + str(ent.start_char) + ' - ' + str(ent.end_char) + ' - ' + ent.label_ +  ' - ' + str(spacy.explain(ent.label_))) 
    else: 
        print('No named entities found.')