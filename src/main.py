from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

from utils.sw1 import count_patterns
from utils.sw2 import count_up_to_89

app = FastAPI()

@app.get("/challenges/solution-1")
def obtener_patrones(n: int = Query(..., ge=0)):
    resultado = count_patterns(n)
    return JSONResponse(str(resultado))

@app.get("/challenges/solution-2")
def cifrado_ciclos(n: int = Query(..., ge=0)):
    resultado = count_up_to_89(n)
    return JSONResponse(str(resultado))
