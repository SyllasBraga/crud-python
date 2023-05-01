from DataBaseConfiguration import BaseModel
from peewee import *


class VendaModel(BaseModel):

    id_venda = PrimaryKeyField()
    nome_produto = TextField()
    valor = FloatField()

    def get_all(self):
        vendas = []

        for venda in self.select():
            vendas.append(self.to_dict(venda))

        return vendas

    def to_dict(self, row):
        return {
            'id_produto': row.id_venda,
            'nome_produto': row.nome_produto,
            'valor': row.valor
        }

    class Meta:
        table_name = 'vendas'