from modelo.entidade import (dataclass, Entidade)
from modelo.cancao import Cancao
from typing import List, Dict
from dataclasses import field

@dataclass
class Playlist(Entidade):
    nome: str
    descricao: str
    img_capa: str
    cancoes: List[Cancao] = field(default_factory=list)

    def add_cancao(self, cancao: Cancao) -> None:
        self.cancoes.append(cancao)
    
    def rem_cancao(self, cancao: Cancao) -> None:
        try:
            self.cancoes.remove(cancao)
        except: pass
    
    def asdict(self) -> None:
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "img_capa": self.img_capa,
            "cancoes": [cancao.id for cancao in self.colecao]
        }
    
    @staticmethod
    def from_dict(playlist_dict: Dict, cancoes: List[Cancao]):
        id = playlist_dict["id"]
        nome = playlist_dict["nome"]
        descricao = playlist_dict["descricao"]
        img_capa = playlist_dict["img_capa"]
        return Playlist(id, nome, descricao, img_capa, cancoes)
