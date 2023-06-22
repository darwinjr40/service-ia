
import init

from flask import Flask
from routes.routes import rutas
from routes.items import route_items
from config import ENV

#main
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/api_flask'
app.config['SQLALCHEMY_DATABASE_URI'] = f'{ENV.DB_CONNECTION}://{ENV.DB_USERNAME}:{ENV.DB_PASSWORD}@{ENV.DB_HOST}/{ENV.DB_DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def inbdex(): return "bienvenido"
    
#rutas
app.register_blueprint(rutas)
app.register_blueprint(route_items)


        
    