from bottle import route
from bottle import run

@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8000, debug=True)
