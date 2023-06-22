
import init

from flask import Flask
from routes.routes import rutas
from routes.items import route_items

#main
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/api_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def inbdex(): return "bienvenido"
    
#rutas
app.register_blueprint(rutas)
app.register_blueprint(route_items)


        
    