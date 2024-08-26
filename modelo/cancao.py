from modelo.entidade import (dataclass, Entidade)
from typing import List, Dict
from datetime import datetime
from dataclasses import field

@dataclass
class Cancao(Entidade):
    titulo: str
    genero: str
    album: int
    diretorio_audio: str
    data_adicao: datetime
    artistas: List[int] = field(default_factory=list)

    def add_artista(self, artista_id: int) -> None:
        self.artistas.append(artista_id)

    def rem_artista(self, artista_id: int) -> None:
        self.artistas.remove(artista_id)
    
    @staticmethod
    def from_dict(cancao_dict: Dict):
        id = cancao_dict["id"]
        titulo = cancao_dict["titulo"]
        artistas = cancao_dict["artistas"]
        genero = cancao_dict["genero"]
        album = cancao_dict["album"]
        diretorio_audio = cancao_dict["diretorio_audio"]
        data_adicao = datetime.fromisoformat(cancao_dict["data_edicao"])
        return Cancao(id, titulo, artistas, genero, album, diretorio_audio, data_adicao)
