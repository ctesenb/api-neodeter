from typing import Optional
from pydantic import BaseModel
#TABLAS DE LOS SERVICIOS
class QrEnvasadoCab(BaseModel): #POST DETELE GET
    Id:Optional[int]
    FechaHora: str
    Id_google: str
    OrdenEnvasado: str
    
    class Config:
        orm_mode =True
    
class QrEnvasadoDet(BaseModel): #POST DETELE GET
    Id_cabecera:Optional[int]
    codProducto: str
    cantidad: int
    
    class Config:
        orm_mode =True
    
class Respuesta(BaseModel):#RESULTADO DE LAS OPERACIONES 
    mensaje:str