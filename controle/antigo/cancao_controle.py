from persistencia.persistencia import UsuarioP
from modelo.cancao import Cancao

class CancaoControle:

    def __init__(self):
        self.persistencia = UsuarioP()

    def atualizar_arquivo(self):
        self.persistencia.atualizar_arquivo()

    def inserir_cancao(self, entidade: Cancao):
        self.persistencia.inserir_cancao(entidade)
    
    def excluir_cancao(self, entidade: Cancao):
        self.persistencia.excluir_cancao(entidade)