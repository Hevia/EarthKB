# EarthKB
A pipeline for turning Earth &amp; Life science documents(images, videos, academic papers, news articles) into a full stack neural searchable knowledge base


## Setup

Windows:
```powershell
python -m venv wvenv # Create a virtual environment
. .\wvenv\Scripts\activate # Activate it
pip install -r requirements.txt # Install requirements
python -m spacy download en_core_web_sm # Install the spacy language model you want to use
git clone https://github.com/thunlp/OpenNRE # TODO: We are on Python 3.9 when this repo is on 3.6, had to manually update Torch dependency to 1.7.1
cd OpenNRE
```

Linux:
```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```