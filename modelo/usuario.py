from modelo.entidade import (dataclass, Entidade)
from modelo.cancao import Cancao
from modelo.playlist import Playlist
from typing import List, Dict
from dataclasses import field

@dataclass
class Usuario(Entidade):
    nome_de_usuario: str
    senha: str
    nome: str
    img_perfil: str
    colecao: List[Cancao] = field(default_factory=list)
    playlists: List[Playlist] = field(default_factory=list)

    def add_cancao(self, cancao: Cancao) -> None:
        self.colecao.append(cancao)
    
    def rem_cancao(self, cancao: Cancao) -> None:
        self.colecao.remove(cancao)
    
    def add_playlist(self, playlist: Playlist) -> None:
        self.playlists.append(playlist)
    
    def rem_playlist(self, playlist: Playlist) -> None:
        self.playlists.remove(playlist)
    
    def asdict(self) -> None:
        return {
            "nome": self.nome,
            "nome_de_usuario": self.nome_de_usuario,
            "senha": self.senha,
            "img_perfil": self.img_perfil,
            "colecao": [cancao.id for cancao in self.colecao],
            "playlists": [playlist.id for playlist in self.playlists]
        }

    @staticmethod
    def from_dict(usuario_dict: Dict, colecao: List[Cancao], playlists: List[Playlist]):
        id = usuario_dict["id"]
        nome_de_usuario = usuario_dict["nome_de_usuario"]
        senha = usuario_dict["senha"]
        nome = usuario_dict["nome"]
        img_perfil = usuario_dict["img_perfil"]

        return Usuario(id, nome_de_usuario, senha, nome, img_perfil, colecao, playlists)