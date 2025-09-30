# rag42/cli.py
import fire

class RAG:
    def index(self, src_dir: str):
        """Ingest files from a directory and build an index."""
        print(f"[INDEX] Would process directory: {src_dir}")

    def search(self, query: str, k: int = 5):
        """Search the index for top-k relevant chunks."""
        print(f"[SEARCH] Query='{query}' | k={k}")

    def answer(self, query: str, k: int = 5):
        """Retrieve chunks and generate an answer (stub)."""
        print(f"[ANSWER] Query='{query}' | k={k}")

if __name__ == "__main__":
    fire.Fire(RAG)

