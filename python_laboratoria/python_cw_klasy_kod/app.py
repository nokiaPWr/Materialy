from flask import Flask

app = Flask('hello')

@app.route('/appka')
def hello_world():
    return str('Witamy w podstornie appka!')

if __name__ == '__main__':
    app.run(host='localhost')
