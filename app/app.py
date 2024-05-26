from fastapi import FastAPI
from api.eps import router as epsRouter
from api.generos import router as generosRouter
from api.pacientes import router as pacientesRouter
from api.personas import router as personasRouter
from api.tiposDocumentos import router as documentosRouter
from api.usuarios import router as usuariosRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url = "/docs")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # o cualquier otro origen desde donde deseas permitir solicitudes
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(epsRouter, prefix="/api")
app.include_router(generosRouter, prefix="/api")
app.include_router(pacientesRouter, prefix="/api")
app.include_router(personasRouter, prefix="/api")
app.include_router(documentosRouter, prefix="/api")
app.include_router(usuariosRouter, prefix = "/api")