import email
from operator import ge
from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
   return RedirectResponse(url="/docs/")

@app.get('/marcaciones/',response_model=List[schemas.Marcation])
def show_marcaciones(db:Session=Depends(get_db)):
    marcaciones = db.query(models.Marcation).all()
    return marcaciones

#Crear marcacion
@app.post('/marcaciones/',response_model=schemas.Marcation)
def create_marcaciones(entrada:schemas.Marcation,db:Session=Depends(get_db)):
    marcacion = models.Marcation(fullname = entrada.fullname,email=entrada.email,area=entrada.area,geolocation=entrada.geolocation,hora=entrada.hora,fecha=entrada.fecha)
    db.add(marcacion)
    db.commit()
    db.refresh(marcacion)
    return marcacion

@app.delete('/marcaciones/{marcacion_id}',response_model=schemas.Respuesta)
def delete_mercaciones(marcacion_id:int,db:Session=Depends(get_db)):
    marcacion = db.query(models.Marcation).filter_by(id=marcacion_id).first()
    db.delete(marcacion)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/geolocation/',response_model=List[schemas.Geolocation])
def show_geolocations(db:Session=Depends(get_db)):
    geolocations = db.query(models.Geolocation).all()
    return geolocations

#Si la geolocalizacion y el area existen, devolver "existe" y sino "no existe"
@app.get('/geolocation/{geolocation}/{area}/',response_model=schemas.Respuesta)
def show_geolocation(geolocation:str,area:str,db:Session=Depends(get_db)):
    geolocation = db.query(models.Geolocation).filter_by(geolocation=geolocation,area=area).first()
    if geolocation:
        respuesta = schemas.Respuesta(mensaje="Existe")
    else:
        respuesta = schemas.Respuesta(mensaje="No existe")
    return respuesta

@app.post('/geolocation/',response_model=schemas.Geolocation)
def create_geolocations(entrada:schemas.Geolocation,db:Session=Depends(get_db)):
    geolocation = models.Geolocation(area= entrada.area, geolocation = entrada.geolocation)
    db.add(geolocation)
    db.commit()
    db.refresh(geolocation)
    return geolocation

@app.delete('/geolocation/{geolocation_id}',response_model=schemas.Respuesta)
def delete_geolocation(geolocation_id:int,db:Session=Depends(get_db)):
    geolocation = db.query(models.Geolocation).filter_by(id=geolocation_id).first()
    db.delete(geolocation)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.put('/geolocation/{geolocation_id}',response_model=schemas.Geolocation)
def update_geolocation(geolocation_id:int,entrada:schemas.Geolocation,db:Session=Depends(get_db)):
    geolocation = db.query(models.Geolocation).filter_by(id=geolocation_id).first()
    geolocation.area = entrada.area
    geolocation.geolocation = entrada.geolocation
    db.commit()
    db.refresh(geolocation)
    return geolocation

@app.get('/empresa/',response_model=List[schemas.Empresa])
def show_empresas(db:Session=Depends(get_db)):
    empresas = db.query(models.Empresa).all()
    return empresas

#Si el ruc de la empresa existe, devolver "existe" y sino "no existe"
@app.get('/empresa/{ruc}/',response_model=schemas.Respuesta)
def show_empresa(ruc:str,db:Session=Depends(get_db)):
    empresa = db.query(models.Empresa).filter_by(ruc=ruc).first()
    if empresa:
        respuesta = schemas.Respuesta(mensaje="Existe")
    else:
        respuesta = schemas.Respuesta(mensaje="No existe")
    return respuesta

@app.post('/empresa/',response_model=schemas.Empresa)
def create_empresas(entrada:schemas.Empresa,db:Session=Depends(get_db)):
    empresa = models.Empresa(empresa = entrada.empresa, ruc = entrada.ruc)
    db.add(empresa)
    db.commit()
    db.refresh(empresa)
    return empresa

@app.delete('/empresa/{empresa_id}',response_model=schemas.Respuesta)
def delete_empresa(empresa_id:int,db:Session=Depends(get_db)):
    empresa = db.query(models.Empresa).filter_by(id=empresa_id).first()
    db.delete(empresa)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.put('/empresa/{empresa_id}',response_model=schemas.Empresa)
def update_empresas(empresa_id:int,entrada:schemas.EmpresaUpdate,db:Session=Depends(get_db)):
    empresa = db.query(models.Empresa).filter_by(id=empresa_id).first()
    empresa.ruc = entrada.ruc
    db.commit()
    db.refresh(empresa)
    return empresa
