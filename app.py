from flask import Flask
from flask_cors import CORS

from config import config
from routes.todo import todo_route
from routes.auth import auth_route

def create_app():
    app = Flask(__name__)
    app.config.update(config.build_config())
    
    app.register_blueprint(todo_route)
    app.register_blueprint(auth_route)
    
    CORS(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port='5000')