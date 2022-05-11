from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World!\n'

# Route dynamique
@app.route('/hello/<username>')
def hello_user(username):
    return 'salut %s!\n' % username

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(host='0.0.0.0')


