from modelo.playlist import Playlist
from persistencia.playlist_pers import PlaylistPers
from controle.tipo_controle import TipoControle


class PlaylistControle(TipoControle):
    def __init__(self) -> None:
        super().__init__(PlaylistPers())
        
    def pesquisar(self,atributo:str,valor:str):
        return self.persistencia.pesquisar(atributo,valor) 

    def inserir(self,playlist:Playlist):
        
        return self.persistencia.inserir(playlist)
    
    def carregar_dados(self):
        
        return self.persistencia.carregar_dados()
    
    def remover(self,playlist:Playlist):
        
        return self.persistencia.remover(playlist)