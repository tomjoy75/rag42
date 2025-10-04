from typing import List, Tuple, Dict
from pathlib import Path

def load_texts(src_dir: str) -> List[Tuple[str, Dict]]:
    """Scan src_dir, read supported files, return [(text, meta), ...]."""
    files_meta = []
    for file in Path(src_dir).rglob('*.*'):
        if file.suffix in [".txt", ".md", ".py"] :
            # with open(file, encoding="utf-8") as f:
            #     content = f.read()
            # print(file, ":",  len(content))
            text = file.read_text(encoding="utf-8")
            #print(file, ":", len(text))
            text = " ".join(text.split())
            #t staprint(text,"/ new length :", len(text))
            meta = (text, {"path": str(file), "start": 0, "end": len(text) - 1})
            files_meta.append(meta)
    return files_meta

#load_texts("./data/")

