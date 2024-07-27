from persistencia.persistencia import Persistencia
from modelo.usuario import Usuario

class Controle:

    def __init__(self):
        self.persistencia = Persistencia()

    def obter_usuarios(self):
        return self.persistencia.obter_usuarios()

    def atualizar_arquivo(self):
        self.persistencia.atualizar_arquivo()
    
    def inserir_usuario(self, entidade: Usuario):
        self.persistencia.inserir_usuario(entidade)
    
    def excluir_usuario(self, id: int):
        self.persistencia.excluir_usuario(id)

    def buscar_username(self, username: str):
        return self.persistencia.buscar_username(username)

    def buscar_id(self, id: int):
        return self.persistencia.buscar_id(id)
    
    def usuarios(self):
        return self.persistencia.usuarios
    
    def verificar_senha(self, usuario_id, senha_digitada):
        return self.persistencia.verificar_senha(usuario_id, senha_digitada)

    def lista_usuarios_vazia(self):
        return self.persistencia.lista_usuarios_vazia()
    
    def obter_artistas(self, id):
        return self.persistencia.obter_artistas(id)
    
    def excluir_artista(self, id, art_id):
        return self.persistencia.excluir_artista(id, art_id)

    def obter_albuns(self, id_usuario):
        return self.persistencia.obter_albuns(id_usuario)
    
    def excluir_album(self, id_usuario, art_id, alb_id):
        return self.persistencia.excluir_album(id_usuario, art_id, alb_id)
    
    def obter_cancoes(self, id_usuario):
        return self.persistencia.obter_cancoes(id_usuario)

    def excluir_cancao(self, id_usuario, art_id, alb_id, can_id):
        return self.persistencia.excluir_cancao(id_usuario, art_id, alb_id, can_id)
    
    def adicionar_musicas(self, id_usuario, audios):
        return self.persistencia.adicionar_musicas(id_usuario, audios)