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

@app.get('/produccion/',response_model=List[schemas.QrEnvasadoCab])
def show_producciones(db: Session = Depends(get_db)):
    producciones = db.query(models.QrEnvasadoCab).all()
    return producciones

@app.get('/produccion/{Id}',response_model=schemas.QrEnvasadoCab)
def show_produccion(Id: int,db: Session = Depends(get_db)):
    produccion = db.query(models.QrEnvasadoCab).filter(models.QrEnvasadoCab.Id == Id).first()
    return produccion

@app.post('/produccion/',response_model=schemas.QrEnvasadoCab)
def create_produccion(entrada: schemas.QrEnvasadoCab, db:Session=Depends(get_db)):
    produccion = models.QrEnvasadoCab(FechaHora=entrada.FechaHora,Id_google=entrada.Id_google,OrdenEnvasado=entrada.OrdenEnvasado)
    db.add(produccion)
    db.commit()
    db.refresh(produccion)
    return produccion

@app.put('/produccion/{Id}',response_model=schemas.QrEnvasadoCab)
def put_produccion(Id: int,entrada: schemas.QrEnvasadoCab, db:Session=Depends(get_db)):
    produccion = db.query(models.QrEnvasadoCab).filter(models.QrEnvasadoCab.Id == Id).first()
    produccion.FechaHora = entrada.FechaHora
    produccion.Id_google = entrada.Id_google
    produccion.OrdenEnvasado = entrada.OrdenEnvasado
    db.commit()
    db.refresh(produccion)
    return produccion

@app.deleted('/produccion/{Id}',response_model=schemas.QrEnvasadoCab)
def delete_produccion(Id: int,db: Session = Depends(get_db)):
    produccion = db.query(models.QrEnvasadoCab).filter(models.QrEnvasadoCab.Id == Id).first()
    db.delete(produccion)
    db.commit()
    return produccion

@app.get('/pDetalles/',response_model=List[schemas.QrEnvasadoDet])
def get_pDetalles(db: Session = Depends(get_db)):
    pDetalles = db.query(models.QrEnvasadoDet).all()
    return pDetalles

@app.get('/pDetalles/{Id}',response_model=schemas.QrEnvasadoDet)
def get_pDetalle(Id: int,db: Session = Depends(get_db)):
    pDetalle = db.query(models.QrEnvasadoDet).filter(models.QrEnvasadoDet.Id == Id).first()
    return pDetalle

@app.post('/pDetalle/',response_model=schemas.QrEnvasadoDet)
def post_pDetalle(entrada: schemas.QrEnvasadoDet, db:Session=Depends(get_db)):
    pDetalle = models.QrEnvasadoDet(Id_cabecera=entrada.Id_cabecera,codProducto=entrada.codProducto,cantidad=entrada.cantidad)
    db.add(pDetalle)
    db.commit()
    db.refresh(pDetalle)
    return pDetalle

@app.put('/pDetalle/{Id}',response_model=schemas.QrEnvasadoDet)
def pust_pDetalle(Id: int,entrada: schemas.QrEnvasadoDet, db:Session=Depends(get_db)):
    pDetalle = db.query(models.QrEnvasadoDet).filter(models.QrEnvasadoDet.Id == Id).first()
    pDetalle.Id_cabecera = entrada.Id_cabecera
    pDetalle.codProducto = entrada.codProducto
    pDetalle.cantidad = entrada.cantidad
    db.commit()
    db.refresh(pDetalle)
    return pDetalle

@app.delete('/pDetalle/{Id}',response_model=schemas.QrEnvasadoDet)
def delete_pDetalle(Id: int,db: Session = Depends(get_db)):
    pDetalle = db.query(models.QrEnvasadoDet).filter(models.QrEnvasadoDet.Id == Id).first()
    db.delete(pDetalle)
    db.commit()
    return pDetalle
