from flask import Flask, jsonify, request
from VendaModel import *

app = Flask(__name__)

vendaModel = VendaModel()


@app.route('/vendas', methods=['GET'])
def get_vendas():
    vendas = vendaModel.get_all()
    return jsonify(vendas)

@app.route('/vendas/<int:id>', methods=['GET'])
def get_venda_by_id(id):
    venda = vendaModel.get_by_id(id)
    return jsonify(venda)


app.run(port=5000, host='localhost', debug=True)
