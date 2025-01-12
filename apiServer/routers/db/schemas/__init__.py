from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class Status(BaseModel):
    message: str

class Autores(BaseModel):
    id_autor: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: str
    pais: str

class Categorias(BaseModel):
    id_categoria: Optional[int]
    nombre: str

class Clientes(BaseModel):
    id_cliente: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: str
    email: str
    telefono: int
    direccion: str
    password: str

class Editoriales(BaseModel):
    id_editorial: Optional[int]
    pais: str
    nombre: str

class Libros(BaseModel):
    id_libro: Optional[int]
    num_paginas: int
    anio: int
    isbn: str
    nombre: str
    estado: str
    resenia: str
    precio: int
    stock: int
    id_autor: int
    id_editorial: int
    id_categoria: int

class Compras(BaseModel):
    id_compra: Optional[int]
    fecha: datetime
    precio: int
    cantidad: int
    id_libro: int
    id_cliente: int