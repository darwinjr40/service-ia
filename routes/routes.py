
import cv2

import numpy as np

from flask import Blueprint, jsonify, request, send_from_directory
import clases.metodos as met

# Crear el blueprint para las rutas
rutas = Blueprint('route_rutas', __name__, url_prefix='/api')



@rutas.route('/imagen/<name_url>')
def gell_hola(name_url):
    return send_from_directory('static/images', name_url)

@rutas.route('/bienvenido')
def gell_bienvenido():
    return 'bienvenido desde routes'




    
# Ruta para obtener una lista de elementos
@rutas.route('/comparacion', methods=['POST'])
def comparacion():
    try:
        filea = request.files['imagea'].read()
        nparr = np.fromstring(filea, np.uint8)
        imagea = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        fileb = request.files['imageb'].read()
        nparr = np.fromstring(fileb, np.uint8)
        imageb = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # xi, yi, xf, yf = 1, 1, 100, 100
        # cv2.rectangle(img_array, (xi, yi), (xf, yf), Color.ROJO, 3)
        # # Codificar la imagen en formato jpg
        # gris1 = cv2.cvtColor(imagea, cv2.COLOR_BGR2GRAY)
        
        return met.frame_to_base64(imagea)
        compare_imgs1(imagea, imageb)
        return 'xd'
        # return es_similar(imagea, imageb)
    except Exception as e:
        return jsonify(
            {'result': 'errors', 'type': f"Tipo de excepción: {type(e)}", 'errors': f"Mensaje de error: {e}"})            


# Ruta para obtener una lista de elementos
@rutas.route('/rut', methods=['GET'])
def get_dato():
    datos = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'}
    ]
    return jsonify(datos)

# Ruta para obtener un elemento específico
@rutas.route('/rut/<int:item_id>', methods=['GET'])
def get_datos(item_id):
    item = {'id': item_id, 'name': 'Item ' + str(item_id)}
    return jsonify(item)

# Ruta para crear un nuevo elemento
@rutas.route('/rut', methods=['POST'])
def create_dato():
    data = request.get_json()
    # Lógica para crear el nuevo elemento en la base de datos
    return jsonify(data), 201

# Ruta para actualizar un elemento existente
@rutas.route('/rut/<int:item_id>', methods=['PUT'])
def update_dato(item_id):
    data = request.get_json()
    # Lógica para actualizar el elemento con el ID dado en la base de datos
    return jsonify(data)

# Ruta para eliminar un elemento existente
@rutas.route('/rut/<int:item_id>', methods=['DELETE'])
def delete_dato(item_id):
    # Lógica para eliminar el elemento con el ID dado de la base de datos
    return '', 204