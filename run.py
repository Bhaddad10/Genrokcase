from app import create_app
from app.db import init_db

app = create_app()
init_db()  # garante que a tabela exista

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
