class Usuario:
    def __init__(self, nome, email, senha, bio, img_perfil, ehADM):
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
    """
