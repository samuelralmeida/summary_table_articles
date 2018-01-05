from models import Article

def saveItem(session, titulo, autor, ano, local, objetivos, delineamento,
             discussao, desfechos, resultados):

    new_item = Article(titulo=titulo, autor=autor, ano=ano, local=local,
                 objetivos=objetivos, delineamento=delineamento,
                 discussao=discussao, desfechos=desfechos, resultados=resultados)

    session.add(new_item)
    session.commit()
    return 'added'
