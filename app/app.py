from fastapi import FastAPI
from api.usuarios import router as usuariosRouter
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url = "/docs")

app.include_router(usuariosRouter, prefix = "/api")