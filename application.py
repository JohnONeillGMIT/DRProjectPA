#!flask/bin/python
from flask import Flask
#from Flask_cors import Flask_cors

app = Flask(__name__, static_url_path='', static_folder='.')
#pp= Flask(__name__)
#CORS(app)

@app.route('/')
def index():
    return "Hello, World!, Johhny"

@app.route('/empl/<int:id>')
def getEmply(id):
    return "you want book with "+ str(id)

if __name__== '__main__':
    app.run(debug=True)