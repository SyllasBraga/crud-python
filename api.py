from flask import Flask, jsonify, request
from VendaModel import *

app = Flask(__name__)

vendaModel = VendaModel()


@app.route('/vendas', methods=['GET'])
def get_livros():
    vendas = vendaModel.get_all()
    return jsonify(vendas)


app.run(port=5000, host='localhost', debug=True)
