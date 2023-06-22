from utils.db import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), default='')
    cantidad = db.Column(db.Integer, default=0)
    precio = db.Column(db.Float, default=0.0)
    estado = db.Column(db.String(100), default='')
    url = db.Column(db.String(150), default='')
    
    def __init__(self, nombre, cantidad, precio, estado, url):            
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.estado = estado
        self.url = url
        
    def toStr(self):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'cantidad':self.cantidad,
            'precio':self.precio,
            'estado':self.estado,
            'url':self.url,
        }    