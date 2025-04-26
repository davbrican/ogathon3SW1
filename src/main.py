from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import List

from utils.sw1 import count_patterns
from utils.sw2 import count_up_to_89
from utils.sw3 import calculate_min_moves

app = FastAPI(docs_url="/swagger")

@app.get("/challenges/solution-1")
def obtener_patrones(n: int = Query(..., ge=0)):
    resultado = count_patterns(n)
    return JSONResponse(str(resultado))

@app.get("/challenges/solution-2")
def cifrado_ciclos(n: int = Query(..., ge=0)):
    resultado = count_up_to_89(n)
    return JSONResponse(str(resultado))

@app.post("/challenges/solution-3")
def effective_recycling(data: List[List[int]]):
    result = calculate_min_moves(data)
    return result