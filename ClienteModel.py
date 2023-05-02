from collections import OrderedDict

from DataBaseConfiguration import BaseModel
from peewee import *


class ClienteModel(BaseModel):
    id_cliente = PrimaryKeyField()
    nome_cliente = TextField()
    login = TextField()

    def get_all(self):
        clientes = []

        for cliente in self.select():
            clientes.append(self.to_dict(cliente))

        return clientes

    def to_dict(self, cliente):

        return {
            'id_cliente': cliente.id_cliente,
            'nome_cliente': cliente.nome_cliente,
            'login': cliente.login
        }

    def to_cliente(self, cliente):
        return ClienteModel(
            id_cliente=cliente['id_cliente'],
            nome_cliente=cliente['nome_cliente'],
            login=cliente['login']
        )

    class Meta:
        table_name = 'cliente'