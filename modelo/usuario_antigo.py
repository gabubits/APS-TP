class Usuario:
    def __init__(self, nome: str, email: str, senha: str, 
                 bio: str, img_perfil: str = "visao/src/img/icon_padrao.png", 
                 eh_adm: bool = 0,
                 historico_ouvidas = [], cancoes_favoritas = [],
                 albuns_favoritos = [], artistas_favoritos = [],
                 playlists = [], amigos = [], solicitacoes_amizade = []):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.bio = bio
        self.img_perfil = img_perfil
        self.eh_adm = eh_adm
        self.historico_ouvidas = historico_ouvidas
        self.cancoes_favoritas = cancoes_favoritas
        self.amigos = amigos
        self.solicitacoes_amizade = solicitacoes_amizade
        self.artistas_favoritos = artistas_favoritos
        self.albuns_favoritos = albuns_favoritos
        self.playlists = playlists
    
    def add_no_historico_ouvidas(self, cancao):
        # Adicionar canção no histórico de ouvidas
        self.historico_ouvidas.append(cancao)

    def add_cancao_fav(self, cancao):
        # Adicionar canção como favorita
        self.cancoes_favoritas.append(cancao)
    
    def add_amigo(self, amigo):
        # Adicionar amigo na lista de amigos
        self.amigos.append(amigo)
    
    def add_solicit(self, solicitacao):
        # Adicionar usuário na lista de solicitações
        self.historico_ouvidas.append(solicitacao)
    
    def add_art_fav(self, artista):
        # Adicionar artista como favorito
        self.historico_ouvidas.append(artista)
    
    def add_album_fav(self, album):
        # Adicionar album como favorito
        self.historico_ouvidas.append(album)
    
    def add_playlist(self, playlist):
        # Adicionar playlist
        self.playlists.append(playlist)
    
    def rem_do_historico_ouvidas(self, cancao):
        self.historico_ouvidas.remove(cancao)

    def rem_cancao_fav(self, cancao):
        self.cancoes_favoritas.remove(cancao)
    
    def rem_amigo(self, amigo):
        self.amigos.remove(amigo)
    
    def rem_solicit(self, solicitacao):
        self.historico_ouvidas.remove(solicitacao)
    
    def rem_art_fav(self, artista):
        self.historico_ouvidas.remove(artista)
    
    def rem_album_fav(self, album):
        self.historico_ouvidas.rem(album)
    
    def rem_playlist(self, playlist):
        self.playlists.remove(playlist)
    
    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'bio': self.bio,
            'img_perfil': self.img_perfil,
            'eh_adm': self.eh_adm,
            'historico_ouvidas': [],
            'cancoes_favoritas': [],
            'albuns_favoritos': [],
            'artistas_favoritos': [],
            'playlists': [],
            'amigos': [],
            'solicitacoes_amizade': []
        }
            # 'historico_ouvidas': [cancao.to_dict() for cancao in self.historico_ouvidas],
            # 'cancoes_favoritas': [cancao.to_dict() for cancao in self.cancoes_favoritas],
            # 'albuns_favoritos': [album.to_dict() for album in self.albuns_favoritos],
            # 'artistas_favoritos': [artista.to_dict() for artista in self.artistas_favoritos],
            # 'playlists': [playlist.to_dict() for playlist in self.playlists],
            # 'amigos': [amigo.to_dict() for amigo in self.amigos],
            # 'solicitacoes_amizade': [solicit.to_dict() for solicit in self.solicitacoes_amizade]
