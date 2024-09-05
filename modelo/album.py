from modelo.entidade import (dataclass, Entidade)
from modelo.cancao import Cancao
from typing import List, Dict
from dataclasses import field

@dataclass
class Album(Entidade):
    titulo: str
    img_capa: str
    tipo: str
    artista: str
    cancoes: List[Cancao] = field(default_factory=list)
    
    def add_cancao(self, cancao: Cancao) -> None:
        self.artistas.append(cancao)
    
    def rem_cancao(self, cancao: Cancao) -> None:
        self.artistas.remove(cancao)
    
    def asdict(self) -> None:
        return {
            "titulo": self.titulo,
            "img_capa": self.img_capa,
            "tipo": self.tipo,
            "artista": self.artista,
            "cancoes": [cancao.id for cancao in self.cancoes]
        }
    
    @staticmethod
    def from_dict(album_dict: Dict, cancoes: List[Cancao]):
        id = album_dict["id"]
        titulo = album_dict["titulo"]
        img_capa = album_dict["img_capa"]
        tipo = album_dict["tipo"]
        artista = album_dict["artista"]
        return Album(id, titulo, img_capa, tipo, artista, cancoes)