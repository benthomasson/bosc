from bottle import request, Bottle, abort, static_file
app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/Users/bthomass/git/bosc/bosc/static')

@app.route('/websocket')
def handle_websocket():
    print('connected')
    wsock = request.environ.get('wsgi.websocket')
    if not wsock:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            message = wsock.receive()
            print('received message')
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break


def main():
    from gevent.pywsgi import WSGIServer
    from geventwebsocket import WebSocketError
    from geventwebsocket.handler import WebSocketHandler
    server = WSGIServer(("0.0.0.0", 8080), app,
                        handler_class=WebSocketHandler)
    print('serving')
    server.serve_forever()
    print('nope')
