import pandas as pd    
df = pd.read_json(path_or_buf="./sample.jsonl", lines=True)

for index, row in df.iterrows():
    print(row["abstract"], row["bib_entries"].keys())