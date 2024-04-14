from persistencia.usuario_p import UsuarioP
from modelo.usuario import Usuario

class UsuarioControle:

    def __init__(self):
        self.persistencia = UsuarioP()

    def atualizar_arquivo(self):
        self.persistencia.atualizar_arquivo()

    def buscar_email(self, email: str):
        return self.persistencia.buscar_email(email)

    def buscar_nome(self, nome: str):
        return self.persistencia.buscar_nome(nome)
    
    def inserir(self, entidade: Usuario):
        self.persistencia.inserir(entidade)

    def excluir(self, entidade: Usuario):
        self.persistencia.excluir(entidade)
    
    def alterar_adm(self, entidade: Usuario):
        self.persistencia.alterar_adm(entidade)
    
    def getUsuarios(self):
        return self.persistencia.usuarios
    