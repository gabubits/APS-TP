

from modelo.artista import Artista
from modelo.playlist import Playlist


class Usuario:
    
    def __init__(self, username, senha, nome, img_perfil,usuario_id = None, colecao:list[Artista]=[], playlists:list[Playlist]=[]) -> None:
        self.usuario_id = usuario_id
        self.username = username
        self.senha = senha
        self.nome = nome
        self.img_perfil = img_perfil            
        self.colecao = colecao 
        self.playlists = playlists
    
    def add_colecao(self, artista:Artista):
        if self.artista_na_colecao(artista.nome): return
        if len(self.colecao) == 0:
            artista.artista_id = 1
        else:
            artista.artista_id = self.colecao[-1].artista_id + 1
        self.colecao.append(artista)
    
    def artista_na_colecao(self, nome_art: str):
        for artista in self.colecao:
            if artista.nome.lower() == nome_art:
                return artista
        
        return None
    
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