from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Humberto', idade=31)
    pessoa.save()
    print(pessoa)    

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.idade = 45
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Flavio').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    consulta_pessoas()