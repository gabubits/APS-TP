from modelo.entidade import (dataclass, Entidade)
from typing import Dict

@dataclass
class Cancao(Entidade):
    titulo: str
    genero: str
    album: str
    diretorio_audio: str
    artista: str
    
    @staticmethod
    def from_dict(cancao_dict: Dict):
        id = cancao_dict["id"]
        titulo = cancao_dict["titulo"]
        artista = cancao_dict["artista"]
        genero = cancao_dict["genero"]
        album = cancao_dict["album"]
        diretorio_audio = cancao_dict["diretorio_audio"]
        return Cancao(id, titulo, genero, album, diretorio_audio, artista)
