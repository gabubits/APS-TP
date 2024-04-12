from Persistencia.UsuarioP import UsuarioP 

class UsuarioControle():

    def __init__(self, persistencia=None):
        if persistencia is None:
            persistencia = UsuarioP()
        self.persistencia = persistencia

    def atualizar_arquivo(self):
        self.persistencia.atualizar_arquivo()

    def ler_dados(self):
        return self.persistencia.ler_dados()
    
    def inserir(self, entidade):
        self.persistencia.inserir(entidade)

    def excluir(self, entidade):
        self.persistencia.excluir(entidade)

    def buscar_email(self, email):
        return self.persistencia.buscar_email(email)

    def buscar(self):
        return self.persistencia.buscar()
    