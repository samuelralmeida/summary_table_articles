from flask import Flask
from database import db_session, init_db
import crud

app = Flask(__name__)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/', methods=['GET', 'POST'])
def createItem():
    if request.method == 'POST':
        titulo = request.form.get('name', None)
        autor = request.form.get('autor', None)
        local = request.form.get('local', None)
        objetivos = request.form.get('objetivos', None)
        delineamento = request.form.get('delineamento', None)
        discussao = request.form.get('discussao', None)
        desfechos = request.form.get('desfechos', None)
        resultados = request.form.get('resultados', None)

        crud.saveItem(db_session, autor, ano, local, objetivos, delineamento,
                      discussao, desfechos, resultados )

        return 'created'

    else:
        return 'create item'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
