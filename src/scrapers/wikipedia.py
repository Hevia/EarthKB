from utils.FileHelpers import loadFileAsLines, saveTextFile
import wikipediaapi
import time

#
wiki_articles: list[str] = loadFileAsLines("./data/sources/wikipedia.txt")

output_dir: str = "./data/wikipedia/"

wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
)

# TODO: Good thing to multiprocess since its all I/O
for article in wiki_articles:
    p_wiki = wiki_wiki.page(article.rstrip())

    try:
        if (p_wiki.exists()):
            saveTextFile(p_wiki.text, f"{output_dir}/{article.rstrip()}.txt")
        else:
            print(f"The article for {article.rstrip()} was not found")
    except Exception:
        raise Exception(f"Error with article: {article.rstrip()}")

    time.sleep(2)

