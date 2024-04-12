import json
import os
import sys

from modelo.usuario import Usuario

class UsuarioP():

    def __init__(self, diretorio):
        self.caminho_arquivo = os.path.join(diretorio, 'UsuarioPersistencia.json')
        self.ListadeUsuarios = []
        self.carregado = False  # Flag para indicar se os dados foram carregados do arquivo

    #atualiza o json com novos dados
    def atualizar_arquivo(self):
        with open(self.caminho_arquivo, 'w') as arquivo:
            json.dump(self.ListadeUsuarios, arquivo)
                
    #exibe os dados do arquivo
    def ler_dados(self):
            with open(self.caminho_arquivo, 'r') as arquivo:
                return json.load(arquivo) 
    
    def inserir(self, objeto):
        self.ListadeUsuarios.append((objeto))


    def excluir(self, objeto):
        if objeto in self.ListadeUsuarios:  # Verifica se o objeto está na lista
            self.ListadeUsuarios.remove(objeto)  # Remove o objeto da lista
            print(f"Usuário {objeto['nome']} removido com sucesso.")
        else:
            print("Usuário não encontrado para ser excluído.")

    def buscar_email(self, email):
        for usuario in self.ListadeUsuarios: 
            if usuario['email'] == email:
                print(usuario)
                return usuario  # Retorna o dicionário do usuário
        print("Não existe um usuário com este email")
        return None  # Retorna None se o usuário não for encontrado
             
         
    def buscar(self, nome):
        for usuario in self.ListadeUsuarios: 
            if usuario['nome'] == nome:
                print(usuario)
                return usuario  # Retorna o dicionário do usuário
        print("Não existe um usuário com este nome")
        return None  # Retorna None se o usuário não for encontrado



if __name__ == "__main__":
    # Criar uma instância do gerenciador UsuarioP com o diretório especificado
    diretorio = ''  # Substitua pelo caminho correto
    manager = UsuarioP(diretorio)
    
    #inserir esta funcionando 
    manager.inserir({'nome': 'João','email':'joao@gmail.com', 'idade': 30})
    manager.inserir({'nome': 'Maria','email':'mariaa12@gmail.com', 'idade': 18})
    manager.inserir({'nome': 'Evelyn','email':'evelinda@gmail.com', 'idade': 38})


    manager.atualizar_arquivo()

    
    #buscar_email etsa funcionando
    email_usuario = "mariaa12@gmail.com"
    for usuario in manager.ListadeUsuarios:
        if usuario['email'] == email_usuario :
           # print(email_usuario)
            manager.buscar_email(email_usuario)

    # buscar esta funcionando estou buscando por nome 
    nome_usuario = "Evelyn"
    for usuario in manager.ListadeUsuarios:
        if usuario['nome'] == nome_usuario :
           # print(email_usuario)
            manager.buscar(nome_usuario)
            
    #exlcuir esta funcionando 
    for usuario in manager.ListadeUsuarios:
        if usuario['nome'] ==  "Maria":
            manager.excluir(usuario)
            manager.atualizar_arquivo()

     #inserir esta funcionando 
    manager.inserir({'nome': 'Marcos','email':'marquinho@gmail.com', 'idade': 10})
    manager.atualizar_arquivo()

    # a lista na memoria e o arquivo json estão imprimindo a mesma coisa
    print(manager.ler_dados())
    print(manager.ListadeUsuarios)