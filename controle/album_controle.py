from persistencia.album_pers import AlbumPers
from controle.tipo_controle import TipoControle

class AlbumControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(AlbumPers())
