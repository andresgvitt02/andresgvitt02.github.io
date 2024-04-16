# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma api de disponibiliza a consulta,
# edição e exclusão de livro.
# 2. URL base - localhost
# 3. Endpoints -
    # - localhost/livros (GET)
    # - localhost/id (GET)
    # - localhost/livros (PUT)
    # - localhost/livros (DELETE)
# 4. Quais recursos - livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O senhor dos Anéis',
        'autor': 'J.K Tolkien'
    },
    {
        'id': 2,
        'título': 'Bastardos inglórios',
        'autor': 'Quentin Tarantino'
    },
    {
        'id': 3,
        'título': 'Turma da Mônica',
        'autor': 'Maurício de Souza'
    },
]

# Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)    

app.run(port=5000,host='localhost', debug=True)