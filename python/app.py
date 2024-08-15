from flask import Flask
from redis import Redis


import logging
_logger = logging.getLogger(__name__)


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


if __name__ == "__main__":
    print('Starting App...')
    app.run(host="0.0.0.0", debug=True)
