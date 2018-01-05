from flask import Flask
from database import db_session, init_db

app = Flask(__name__)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def createItem():
    return 'create item'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
