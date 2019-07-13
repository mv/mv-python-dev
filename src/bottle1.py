from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<h2>Hello {{name}}!</h2>', name=name)


run(host='0.0.0.0', port=8080)

