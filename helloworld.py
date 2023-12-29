from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Orcodio!!'

@app.route('/admin')
def hello_world():
    return 'Admin page'