from flask import Flask, jsonify, request
from VendaModel import *
from ClienteModel import *

app = Flask(__name__)

vendaModel = VendaModel()
clienteModel = ClienteModel()

@app.route('/vendas', methods=['GET'])
def get_vendas():
    vendas = vendaModel.get_all()
    return jsonify(vendas)


@app.route('/vendas/<int:id>', methods=['GET'])
def get_venda_by_id(id):
    venda = vendaModel.get_by_id(id)
    return jsonify(venda)


@app.route('/vendas', methods=['POST'])
def create_venda():
    venda = request.get_json()

    return vendaModel.create(venda)


@app.route('/vendas/<int:id>', methods=['PUT'])
def update_venda(id):
    venda = request.get_json()

    return vendaModel.update_venda(id, venda)


@app.route('/vendas/<int:id>', methods=['DELETE'])
def delete_venda(id):
    return vendaModel.delete_venda(id)


@app.route('/clientes', methods=['GET'])
def get_all_clientes():
    return jsonify(clienteModel.get_all())


app.run(port=5000, host='localhost', debug=True)
