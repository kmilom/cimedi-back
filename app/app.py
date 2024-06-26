from fastapi import FastAPI
from api.citas import router as citasRouter
from api.eps import router as epsRouter
from api.especialidades import router as especialidadesRouter
from api.generos import router as generosRouter
from api.horarios import router as horariosRouter
from api.medicos import router as medicosRouter
from api.pacientes import router as pacientesRouter
from api.personas import router as personasRouter
from api.tiposDocumentos import router as documentosRouter
from api.usuarios import router as usuariosRouter
#from authentication.router import router as loginRouter
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

app.include_router(citasRouter, prefix="/api")
app.include_router(especialidadesRouter, prefix="/api")
app.include_router(epsRouter, prefix="/api")
app.include_router(generosRouter, prefix="/api")
app.include_router(horariosRouter, prefix="/api")
#app.include_router(loginRouter, prefix="/api")
app.include_router(medicosRouter, prefix="/api")
app.include_router(pacientesRouter, prefix="/api")
app.include_router(personasRouter, prefix="/api")
app.include_router(documentosRouter, prefix="/api")
app.include_router(usuariosRouter, prefix = "/api")