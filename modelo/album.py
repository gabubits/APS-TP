from modelo.entidade import (dataclass, Entidade)
from datetime import datetime
from typing import List, Dict
from dataclasses import field

@dataclass
class Album(Entidade):
    titulo: str
    img_capa: str
    data_lancamento: datetime
    data_adicao: datetime
    tipo: str
    artistas: List[int] = field(default_factory=list)
    cancoes: List[int] = field(default_factory=list)

    def add_artista(self, artista_id: int) -> None:
        self.artistas.append(artista_id)
    
    def rem_artista(self, artista_id: int) -> None:
        self.artistas.remove(artista_id)
    
    def add_cancao(self, cancao_id: int) -> None:
        self.artistas.append(cancao_id)
    
    def rem_cancao(self, cancao_id: int) -> None:
        self.artistas.remove(cancao_id)
    
    @staticmethod
    def from_dict(album_dict: Dict):
        id = album_dict["id"]
        titulo = album_dict["titulo"]
        img_capa = album_dict["img_capa"]
        data_lancamento = datetime.fromisoformat(album_dict["data_lancamento"])
        data_adicao = datetime.fromisoformat(album_dict["data_adicao"])
        tipo = album_dict["tipo"]
        artistas = album_dict["artistas"]
        cancoes = album_dict["cancoes"]
        return Album(id, titulo, img_capa, data_lancamento, data_adicao, tipo, artistas, cancoes)