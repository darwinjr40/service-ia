# from config import config

from app import app
from utils.db import db
    
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # app.config.from_object(config['development'])
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run( host='0.0.0.0')        