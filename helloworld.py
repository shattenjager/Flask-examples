from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Orcodio!!'

@app.route('/admin')
def admin():
    return 'Admin page'