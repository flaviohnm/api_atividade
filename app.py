from urllib import request, response
from flask import Flask
from flask_restful import Resource, Api
from models import Atividades, Pessoas

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id':pessoa.id,
                'nome':pessoa.nome,
                'idade':pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'pessoa não encontrada'
            }
        return response
    
    def put(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome': i.nome, 'idade':i.idade} for i in pessoas]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome } for i in atividades]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'],pessoa=pessoa)
        atividade.save()
        response = {
            'id':atividade.id,
            'nome':atividade.nome,
            'pessoa':atividade.pessoa.nome
        }
        return response

api.add_resource(Pessoa,'/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoa/')
api.add_resource(ListaPessoas,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)