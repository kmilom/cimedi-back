from pydantic import BaseModel

class TipoDocumento(BaseModel):
    idTipoDocumento: int
    Tipo: str