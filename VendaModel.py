from peewee import *

mysql_db = MySQLDatabase(database='crud_python', password='12345', user='root', autocommit=True)


class BaseModel(Model):
    class Meta:
        database = mysql_db


def to_dict(row):
    return {
        'id_produto': row.id_venda,
        'nome_produto': row.nome_produto,
        'valor': row.valor
    }


class Vendas(BaseModel):
    id_venda = PrimaryKeyField()
    nome_produto = TextField()
    valor = FloatField()

    def get_all(self):
        vendas = []

        for venda in Vendas.select():
            vendas.append(to_dict(venda))

        return vendas


