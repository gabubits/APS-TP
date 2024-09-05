from modelo.playlist import Playlist
from persistencia.playlist_pers import PlaylistPers
from controle.tipo_controle import TipoControle


class PlaylistControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(PlaylistPers())
        