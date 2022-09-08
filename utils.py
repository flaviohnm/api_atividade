from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome='Leonardo', idade=23)
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

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()
    
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('adriano','1250')
    insere_usuario('vampeta','8987')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()