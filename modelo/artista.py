from modelo.entidade import (dataclass, Entidade)
from typing import List, Dict
from dataclasses import field

@dataclass
class Artista(Entidade):
    nome: str
    albuns: List[int] = field(default_factory=list)
    singles: List[int] = field(default_factory=list)

    def add_album(self, album_id: int) -> None:
        self.albuns.append(album_id)
    
    def rem_album(self, album_id: int) -> None:
        self.albuns.remove(album_id)

    def add_album(self, album_id: int) -> None:
        self.albuns.append(album_id)
    
    def rem_album(self, album_id: int) -> None:
        self.albuns.remove(album_id)
    
    @staticmethod
    def from_dict(artista_dict: Dict):
        id = artista_dict["id"]
        nome = artista_dict["nome"]
        albuns = artista_dict["albuns"]
        singles = artista_dict["singles"]
        return Artista(id, nome, albuns, singles)