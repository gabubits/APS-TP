"""
from Cancao import Cancao
from Artista import Artista
from Album import Album
from Playlisr import Playlist
"""

class Usuario:
    # Pode tirar todos os atributos depois de ehADM
    def __init__(self, nome, email, senha, bio, img_perfil, ehADM, historico_ouvidas=None, 
                 cancoes_favoritas=None, lista_amigos=None, solicitacoes_amizade=None, artistas_favoritos=None, 
                 albuns_favoritos=None, lista_playlists=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.bio = bio
        self.img_perfil = img_perfil
        self.ehADM = ehADM
        self.historico_ouvidas = []
        self.cancoes_favoritas = []
        self.lista_amigos = []
        self.solicitacoes_amizade = []
        self.artistas_favoritos = []
        self.albuns_favoritos = []
        self.lista_playlists = []
        """
        if historico_ouvidas is None:
            historico_ouvidas = Cancao("","") #Erro por não ter a classe Cancoes ainda, cada "" é para a quantidade de atributos da classe
        self.historico_ouvidas = [historico_ouvidas]

        if cancoes_favoritas is None:
            cancoes_favoritas = Cancao("","")
        self.cancoes_favoritas = [cancoes_favoritas]

        if lista_amigos is None:
            lista_amigos = Usuario("","","","","","","","","")
        self.lista_amigos = [lista_amigos]

        if solicitacoes_amizade is None:
            solicitacoes_amizade = Usuario("","","","","","","","","")
        self.solicitacoes_amizade = [solicitacoes_amizade]

        if artistas_favoritos is None:
            artistas_favoritos = Artista("","")
        self.artistas_favoritos = [artistas_favoritos]

        if albuns_favoritos is None:
            albuns_favoritos = Album("","")
        self.albuns_favoritos = [albuns_favoritos]

        if lista_playlists is None:
            lista_playlists = Playlist("","")
        self.lista_playlists = [lista_playlists]
    
    def adicionar_historico_ouvidas(self, cancao):
        self.historico_ouvidas.append(cancao)

    def adicionar_cancao_favorita(self, cancao):
        self.cancoes_favoritas.append(cancao)

    def adicionar_lista_amigos(self, usuario):
        self.lista_amigos.append(usuario)

    def adicionar_solicitacoes_amizade(self, usuario):
        self.solicitacoes_amizade.append(usuario)
    
    def adicionar_artista_favorito(self, artista):
        self.artistas_favoritos.append(artista)

    def adicionar_album_favorito(self, album):
        self.albuns_favoritos.append(album)

    def adicionar_lista_playlists(self, playlist):
        self.lista_playlists.append(playlist)
    """
