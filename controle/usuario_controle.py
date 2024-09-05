from modelo.playlist import Playlist
from modelo.usuario import Usuario
from persistencia.usuario_pers import UsuarioPers
from controle.tipo_controle import TipoControle

class UsuarioControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(UsuarioPers())
        
    def atualizar_dados(self):
        
        return self.persistencia.atualizar_dados()
    
    def remover_playlist(self,usuario:Usuario, playlist:Playlist):
        
        for p in usuario.playlists:
            print(f'oiaaa  {p.id} {playlist.id}')
            if p.id == playlist.id:
                
                usuario.playlists.remove(p)
                self.atualizar_dados()
                return
        return
                
    
    def inserir_playlist(self, usuario:Usuario, playlist:Playlist):
        usuario.playlists.append(playlist)
        self.atualizar_dados()
    
   
