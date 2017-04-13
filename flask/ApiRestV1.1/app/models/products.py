from flask_sqlalchemy import SQLAlchemy
import datetime
from collections import OrderedDict
import  json
from app import db

class productos(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	nombre = db.Column(db.String(50),unique=True)
	precio = db.Column(db.Integer)
	foto = db.Column(db.String(50))
	descripcion = db.Column(db.String(50))
	categoria = db.Column(db.String(50))
	vendido = db.Column(db.Integer)

	def create_prod(self, nombre, precio, foto, descripcion, categoria, vendido):
		self.nombre = nombre
		self.precio = precio
		self.foto = foto
		self.descripcion = descripcion
		self.categoria = categoria
		self.vendido = vendido

	def get_prod(self, id):		
		aux = productos.query.filter_by(id=id).first()
		if aux is None:
			return 0
		return {'id':aux.id,'nombre': aux.nombre,'precio':aux.precio,'foto': aux.foto,'descripcion':aux.descripcion,'categoria': aux.categoria,'vendido':aux.vendido}

	def get_object(self,id):
		return productos.query.filter_by(id=id)

	def all_prod(self):		
		aux = productos.query.all()
		if aux is None:
			return 0
		return aux
	def number_prod(self):		
		print( productos.query.count())
		return productos.query.count()

	def convert(self, lista, cantidad):
		jsona = [{'id':lista[i].id,'nombre':lista[i].nombre,'precio':lista[i].precio,'foto':lista[i].foto,'descripcion':lista[i].descripcion,'categoria':lista[i].categoria,'vendido':lista[i].vendido} for i in range(0,cantidad)]
		print(jsona)
		return jsona

	def set_prod(self, id, nombre, precio, foto, descripcion, categoria, vendido):	
		#Retorno el objecto de la bd y el registro nuevo a almacenar
		return productos.query.filter_by(id=id), {'id': id,'nombre': nombre,'precio': precio,'foto': foto,'descripcion': descripcion,'categoria': categoria,'vendido':vendido}

	def delete_prod(self, id):		
		aux = productos.query.get(id)
		if aux is None:
			return 0 
		return aux 
		
			
