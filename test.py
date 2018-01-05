import unittest
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
import crud

class StopsTestCase(unittest.TestCase):

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=self.engine))
        Base.query = self.session.query_property()

        Base.metadata.create_all(bind=self.engine)

    # verifica se o BD foi criado e está vazio
    def test_empty_db(self):
        articles = self.session.query(models.Article).all()
        self.assertEqual(len(articles), 0)

    # verifica se a função crud funciona e se foi salva entrada no BD
    def test_add_item(self):
        result = crud.saveItem(self.session, titulo='titulo_test',
                               autor="autor_test", ano=2000, local="local_test",
                               objetivos="objetivos_test",
                               delineamento="delineamento_test",
                               discussao="discussao_test",
                               desfechos="desfechos_test",
                               resultados="resultados_test")

        articles = self.session.query(models.Article).all()
        self.assertEqual(len(articles), 1)

    def tearDown(self):
        self.session.remove()

if __name__ == '__main__':
    unittest.main()
