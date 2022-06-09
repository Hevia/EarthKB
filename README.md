# EarthKG
A pipeline for turning Earth &amp; Life science documents into a searchable knowledge base to aid researchers generate new hypotheses.

## Features
- Searching documents by keywords

## Planned Features
- Easy CLI setup to spin up your own system.
- Knowledge graph driven hypothesis generation. 
- Reccomendations powered by topic embeddings.
- Dockerfiles for reproducability & easy deployment

## Setup


### Installing dependencies 
You should use the provided Dockerfiles for development, but in the case you rather install locally. You can 

Windows:
Read this guide on how to install poppler for windows: https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows (required for mmda)

```powershell
python -m venv wvenv # Create a virtual environment
. .\wvenv\Scripts\activate # Activate it
pip install -r requirements.txt # Install requirements
```

Linux:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

All Systems:
```sh
>>> python # start a python repl in your command prompt
>>> import nltk
>>> nltk.download('wordnet')
>>> nltk.download('omw-1.4')
python -m spacy download en_core_web_sm # Install the spacy language model you want to use
```

### Getting the data
