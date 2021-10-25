import os, sys
from flask import Flask, request


SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/hello')
def test():
    print('test')
    return 'test'

app.run()
