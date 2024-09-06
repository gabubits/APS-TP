from modelo.entidade import (dataclass, Entidade)
from modelo.album import Album
from modelo.cancao import Cancao
from typing import List, Dict
from dataclasses import field

@dataclass
class Artista(Entidade):
    nome: str
    nacionalidade: str
    albuns: List[Album] = field(default_factory=list)
    singles: List[Cancao] = field(default_factory=list)

    def add_album(self, album: Album) -> None:
        self.albuns.append(album)

    def rem_album(self, album: Album) -> None:
        try:
            self.albuns.remove(album)
        except: pass

    def add_single(self, cancao: Cancao) -> None:
        self.singles.append(cancao)

    def rem_single(self, cancao: Cancao) -> None:
        try:
            self.singles.remove(cancao)
        except: pass

    def asdict(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "nacionalidade": self.nacionalidade,
            "albuns": [album.id for album in self.albuns],
            "singles": [single.id for single in self.singles]
        }

    @staticmethod
    def from_dict(artista_dict: Dict, albuns: List[Album], singles: List[Cancao]):
        id = artista_dict["id"]
        nome = artista_dict["nome"]
        nacionalidade = artista_dict["nacionalidade"]
        return Artista(id, nome, nacionalidade, albuns, singles)
