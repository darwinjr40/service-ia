import os
import random
import cv2
from flask import Blueprint, Flask, abort, jsonify, request
import numpy as np

from models.item import Item
from utils.db import db
from sqlalchemy.orm import class_mapper
from init import names_files_complete_ext, names_files
import clases.metodos as met

route_items = Blueprint('route_items', __name__, url_prefix='/api')

datos = [
    {
        'id': 1,
        'title': 'Do laundry',
        'description': 'Wash clothes, dry clothes, fold clothes',
        'done': False
    },
    {
        'id': 2,
        'title': 'Buy groceries',
        'description': 'Milk, bread, eggs, cheese',
        'done': False
    }
]

@route_items.route('/items/seed')
def seed_ejecutar():    
    # global names_files_complete_ext, names_files
    dim = len(names_files)    
    for i in range(0, dim):
        new_item = Item(                
                nombre= os.path.splitext(names_files_complete_ext[i])[0],
                cantidad= random.randint(5, 25),
                precio= random.randint(50, 1000),
                estado= 'disponible',
                url= f'http://127.0.0.1:5000/api/imagen/{names_files_complete_ext[i]}'
            )    
        db.session.add(new_item)
        db.session.commit()    
    # for data in names_files_complete_ext:
    #     numero_aleatorio = random.randint(0, dim-1)
    #     new_item = Item(
    #         nombre= names_files[numero_aleatorio],
    #         cantidad= random.randint(10, 50),
    #         estado= 'disponible',
    #         url= f'http://127.0.0.1:5000/api/imagen/{data}'
    #     )    
    #     db.session.add(new_item)
    #     db.session.commit()
    return jsonify({'result': True})

    # print (f"coded_files: {coded_files}")

# Ruta para obtener una lista de elementos
@route_items.route('/items/get-compara', methods=['POST'])
def rutas_compara():
    try:
        filea = request.files['img'].read()
        nparr = np.fromstring(filea, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        nombres = met.buscar_similares(img)
        if len(nombres) == 0:
            items_dict = []
        else:
            items = Item.query.filter(Item.nombre.in_(nombres)).all()
            items_dict = [item_to_dict(item) for item in items]
        print(items_dict)
        return jsonify(items_dict)
    except Exception as e:
        return jsonify(
            {'result': 'errors', 'type': f"Tipo de excepción: {type(e)}", 'errors': f"Mensaje de error: {e}"})            

    
def item_to_dict(item):
    # Convierte el objeto Item en un diccionario
    item_dict = {}
    for column in class_mapper(Item).mapped_table.columns:
        item_dict[column.name] = getattr(item, column.name)
    return item_dict

@route_items.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    items_dict = [item_to_dict(item) for item in items]
    print(items_dict)
    return jsonify(items_dict)

@route_items.route('/items/<int:task_id>', methods=['GET'])
def get_item(task_id):
    task = [task for task in datos if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@route_items.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'nombre' in request.json:
        abort(400)
    new_item = Item(
        nombre= request.json['nombre'],
        cantidad= 0,
        estado= request.json['estado'],
        url= request.json['url']
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'task': new_item.toStr()}), 201
    return jsonify({'task': new_item.toStr()}), 201
    return "xd"
    # return request.get_json()
    datos.append(task) 
    return jsonify({'task': new_item}), 201

@route_items.route('/items/<int:task_id>', methods=['PUT'])
def update_item(task_id):
    task = [task for task in datos if task['id'] == task_id]
    if (len(task) == 0) or (not request.json):
        abort(404)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@route_items.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()    
    return jsonify({'result': True})
    task = [task for task in datos if task['id'] == id]
    if len(task) == 0:
        abort(404)
    datos.remove(task[0])