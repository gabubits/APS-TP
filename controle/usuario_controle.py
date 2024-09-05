from modelo.playlist import Playlist
from modelo.usuario import Usuario
from persistencia.usuario_pers import UsuarioPers
from controle.tipo_controle import TipoControle

class UsuarioControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(UsuarioPers())
        

   
