from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Libera CORS
    CORS(app)

    # Importa e registra blueprint das rotas
    from .routes import bp
    app.register_blueprint(bp)

    return app
