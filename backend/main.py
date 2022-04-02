from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import json
from pathlib import Path
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/components")
    component_paths = [str(j)  for i in list((Path.cwd().parent / "components").iterdir()) for j in list(i.iterdir())]
    component_jsons = [pd.read_json(i, orient='index').to_dict() for i in component_paths if Path(i).suffix == ".json"]
    component_svg = [Path(i).read_text() for i in component_paths if Path(i).suffix == ".svg"]
    test = [Path(i).read_text() for i in component_paths if Path(i).suffix == ".json"][0]
    return ( JSONResponse(content= jsonable_encoder(component_jsons)) )