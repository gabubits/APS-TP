from persistencia.artista_pers import ArtistaPers
from controle.tipo_controle import TipoControle

class ArtistaControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(ArtistaPers())
