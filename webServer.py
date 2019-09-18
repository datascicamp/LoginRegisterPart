from app import app
import time
from config import Config
import os

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # os.system('flask db init')
    # os.system("flask db migrate -m'Server running on K8s.'")
    # os.system('flask db upgrade')
    # for K8s reading config
    while Config.POSTGRES_HOST is None or Config.POSTGRES_PORT is None:
        logging.error('Waiting for parameter POSTGRES_HOST and POSTGRES_PORT...')
        time.sleep(3)
    app.run(host='0.0.0.0', port=5000, debug=False)
