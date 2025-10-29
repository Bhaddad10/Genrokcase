import logging
from logging.handlers import RotatingFileHandler
import os

# Criação da pasta de logs
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Caminho do arquivo de log
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configuração do logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Formatação do log
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%d-%m-%y %H:%M:%S"
)

# Handler para salvar e rotacionar o arquivo de log
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
file_handler.setFormatter(formatter)

# Handler para exibir logs no console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Evita adicionar múltiplos handlers duplicados
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
