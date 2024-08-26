from modelo.entidade import (dataclass, Entidade)
from datetime import datetime
from typing import List, Dict
from dataclasses import field

@dataclass
class Playlist(Entidade):
    nome: str
    descricao: str
    img_capa: str
    data_criacao: datetime
    cancoes: List[int] = field(default_factory=list)

    def add_cancao(self, cancao_id: int) -> None:
        self.cancoes.append(cancao_id)
    
    def rem_cancao(self, cancao_id: int) -> None:
        self.cancoes.remove(cancao_id)
    
    @staticmethod
    def from_dict(playlist_dict: Dict):
        id = playlist_dict["id"]
        nome = playlist_dict["nome"]
        descricao = playlist_dict["descricao"]
        img_capa = playlist_dict["img_capa"]
        data_criacao = datetime.fromisoformat(playlist_dict["data_criacao"])
        cancoes = playlist_dict["cancoes"]
        return Playlist(id, nome, descricao, img_capa, data_criacao, cancoes)
