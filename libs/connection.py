# from sqlalchemy import create_engine
# import pandas as pd
# import os



class DatabaseManager():
    def __init__(self, table):
        self.table = table

    def where_id(self, id):
        '''Buscar o id no banco de dados e retornar um dataframe'''
        # df = pd.read_sql(f'SELECT * FROM {self.table} WHERE id = {id}', con=engine)
        # return df
        return {'id': 1, 'nome': 'Miliano'}

    def where_condition(self, condition):
        '''Buscar o condição no banco de dados e retornar um dataframe'''
        # df = pd.read_sql(f'SELECT * FROM {self.table} WHERE {condition}', con=engine)
        # return df
        return {'id': 1, 'nome': 'Miliano 2'}





if __name__ == '__main__':
    db = DatabaseManager(table='cgh_fae')
    busca_id = db.where_id(1)
    print(busca_id.head())
    buca_condicao = db.where_condition('id < 6000')
    print(buca_condicao.head())



    # __tablename__ = "users"
    #
    # id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    # username = Column(String, unique=True, index=True)
    # password = Column(String)

'''
Talvez eu esteja confundindo as conexões, o que eu entendo agora é,
Tenho meu código local, vinculado ao github, e o github está vinculado ao railway.
As credencias para conexão do banco de dados com a railway, estão no arquivo .env do github.


'''