from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import json
from utils import encode_descriptions, semantic_search

app = FastAPI()

with open("sf_symbols.json", "r") as f:
    SYMBOLS = json.load(f)

SYMBOL_EMBEDDINGS = encode_descriptions(SYMBOLS)

@app.post("/search-text")
def search_symbol_by_text(description: str = Form(...)):
    results = semantic_search(description, SYMBOLS, SYMBOL_EMBEDDINGS)
    return JSONResponse(content={"results": results})
