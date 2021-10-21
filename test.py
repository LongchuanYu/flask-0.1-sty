import os, sys
from flask import Flask


SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/hallo')
def test():
    print('test')
    return 'test'

app.run()
