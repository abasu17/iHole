from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from route import *

if __name__ == '__main__':
    app.run('0.0.0.0')
