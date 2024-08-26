from modelo.entidade import (dataclass, Entidade)
from typing import List, Dict
from datetime import datetime
from dataclasses import field

@dataclass
class Reproducao:
    data: datetime
    cancao: int

@dataclass
class Usuario(Entidade):
    nome_de_usuario: str
    senha: str
    nome: str
    img_perfil: str
    cancoes: List[int] = field(default_factory=list)
    playlists: List[int] = field(default_factory=list)
    reproducoes: List[Reproducao] = field(default_factory=list)

    def add_cancao(self, cancao_id: int) -> None:
        self.cancoes.append(cancao_id)
    
    def rem_cancao(self, cancao_id: int) -> None:
        self.cancoes.remove(cancao_id)
    
    def add_playlist(self, playlist_id: int) -> None:
        self.playlists.append(playlist_id)
    
    def rem_playlist(self, playlist_id: int) -> None:
        self.playlists.remove(playlist_id)
    
    def add_reproducao(self, cancao_id: int) -> None:
        self.reproducoes.append(Reproducao(datetime.today(), cancao_id))

    @staticmethod
    def from_dict(usuario_dict: Dict):
        id = usuario_dict["id"]
        nome_de_usuario = usuario_dict["nome_de_usuario"]
        senha = usuario_dict["senha"]
        nome = usuario_dict["nome"]
        img_perfil = usuario_dict["img_perfil"]
        cancoes = usuario_dict["cancoes"]
        playlists = usuario_dict["playlists"]
        reproducoes = [Reproducao(datetime.fromisoformat(rep["data"]), rep["cancao"]) for rep in usuario_dict["reproducoes"]]
        return Usuario(id, nome_de_usuario, senha, nome, img_perfil, cancoes, playlists, reproducoes)