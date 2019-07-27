from app import app
import os

import logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    os.system('flask db init')
    os.system("flask db migrate -m'Server running on K8s.'")
    os.system('flask db upgrade')
    app.run(host='0.0.0.0', port=80, debug=False)
