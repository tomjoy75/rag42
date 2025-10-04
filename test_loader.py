from rag42.io.loader import load_texts

print(load_texts("./data"))

"""
from rag42.io.loader import load_texts

docs = load_texts("./data")
for text, meta in docs:
    print(meta["path"], ":", len(text))
"""
