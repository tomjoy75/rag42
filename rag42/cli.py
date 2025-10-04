# rag42/cli.py
import  fire
from    rag42.io.loader import load_texts

class RAG:
    def index(self, src_dir: str):
        """Ingest files from a directory and build an index."""
        # print(f"[INDEX] Would process directory: {src_dir}")
        docs = load_texts(src_dir)
        # print ("nb_files : ", len(docs))
        nb_char = 0
        for doc in docs:
            nb_char += doc[1]['end'] - doc[1]['start'] + 1
        print (f"Ingested {len(docs)} files, {nb_char} characters")

    def search(self, query: str, k: int = 5):
        """Search the index for top-k relevant chunks."""
        print(f"[SEARCH] Query='{query}' | k={k}")

    def answer(self, query: str, k: int = 5):
        """Retrieve chunks and generate an answer (stub)."""
        print(f"[ANSWER] Query='{query}' | k={k}")

if __name__ == "__main__":
    fire.Fire(RAG)

