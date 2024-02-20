from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [

    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atomicos',
        'autor': 'James Clear'
    },
    {
        'id': 4,
        'título': 'O Inferno de Dante',
        'autor': 'Dante Alighieri'
    },
    {
        'id': 5,
        'título': 'A arte da Guerra',
        'autor': ' SUN TZU'
    },
]

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods = ['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].uptade(livro_alterado)
            return jsonify(livro[indice])

@app.route('/livros',methods=['POST'])
def criar_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)