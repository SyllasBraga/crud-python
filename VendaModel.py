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

    def get_by_id(self, id):
        venda = self.get(id)

        return self.to_dict(venda)

    def create(self, venda):

        venda_obj = self.to_venda(venda)
        venda_obj.save()

        return self.get_all()

    def to_dict(self, row):
        return {
            'id_venda': row.id_venda,
            'nome_produto': row.nome_produto,
            'valor': row.valor
        }

    def to_venda(self, venda):

        venda_cvt = VendaModel(nome_produto=venda['nome_produto'],
                          valor=venda['valor'])

        return venda_cvt

    class Meta:
        table_name = 'vendas'
