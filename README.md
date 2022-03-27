# EarthKG
A pipeline for turning Earth &amp; Life science documents(images, videos, academic papers, news articles) into a full stack neural searchable knowledge base

## Features
A complete roadmap can be found [here.]()

EarthKG offers
- Data scrapers for wikipedia


## Setup

You can self-host EarthKG &amp; create a knowledge graph from your own collection of documents. If you want to see EarthKG in action, check out the demo site which is trained on knowledge graph papers: [link](). (Very meta!)

### Installing dependencies 
EarthKG is currently not a python package, until then here are the instructions for getting it running on your system.

Windows:
```powershell
python -m venv wvenv # Create a virtual environment
. .\wvenv\Scripts\activate # Activate it
pip install -r requirements.txt # Install requirements
pip install git+https://github.com/boudinfl/pke.git # PKE is only on github for some reason??
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
