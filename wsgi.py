from flask import Flask
from finder import location


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(location)
    app.run(host='0.0.0.0', port=8080)
