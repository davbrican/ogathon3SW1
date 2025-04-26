from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

def contar_patrones(n: int) -> int:
    if n < 0:
        return 0
    dp = [0] * (n + 2)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
    return dp[n]

@app.get("/challenges/solution-1")
def obtener_patrones(n: int = Query(..., ge=0)):
    resultado = contar_patrones(n)
    return JSONResponse(content={"distancia": n, "patrones": resultado})
