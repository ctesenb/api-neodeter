from sqlalchemy import Column, ForeignKey, Integer, String
from Conexion import Base
    
class QrEnvasadoCab(Base):
    __tablename__= 'qrenvasadocab'
    Id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    FechaHora = Column(String(30))
    Id_google = Column(String(20))
    OrdenEnvasado = Column(String(20))

class QrEnvasadoDet(Base):
    __tablename__ = 'qrenvasadodet'
    Id_cabecera = Column(Integer, ForeignKey('QrEnvasadoCab.Id')) #foreign key -> animation.id
    codProducto = Column(String(30))
    cantidad = Column(Integer)
