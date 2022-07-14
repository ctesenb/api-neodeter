import email
from operator import ge
from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Conexion import SessionLocal,engine

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

#La segunda etiqueta es EL NOMBRE DEL PRODUCTO, eso lo jala de una API que apunta a la misma BD a la tabla IF5PLA.... Select F5NOMPRO FROM IF5PLA WHERE F5CODPRO = {dato del Qr}
@app.get('/IF5PLA/{codProducto}')
def get_producto(codProducto: str,db):
    producto = db.query('SELECT F5NOMPRO FROM IF5PLA WHERE F5CODPRO = codProducto',params={'codProducto':codProducto}).first()
    return producto

