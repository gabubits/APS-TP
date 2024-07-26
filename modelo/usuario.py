

from modelo.artista import Artista
from modelo.playlist import Playlist


class Usuario:
    
    def __init__(self, username, senha, nome, img_perfil,usuario_id, colecao:Artista=[], playlists:Playlist=[]) -> None:
        self.usuario_id = usuario_id
        self.username = username
        self.senha = senha
        self.nome = nome
        self.img_perfil = img_perfil            
        self.colecao = colecao 
        self.playlists = playlists
    
    def add_colecao(self, artista:Artista):
        artista.artista_id = len(self.colecao)
        self.colecao.append(artista)
        
            
    
    def to_dict(self):
        print(self.playlists)
        return {
            'usuario_id': self.usuario_id,
            'username': self.username,
            'senha': self.senha,
            'nome': self.nome,
            'img_perfil': self.img_perfil,
            'colecao': [artista.to_dict() for artista in self.colecao],
            'playlists': [playlist.to_dict() for playlist in self.playlists]
            
        }