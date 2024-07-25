
from modelo.cancao_id import CancaoId


class Playlist:
    def __init__(self, nome, descricao, img_capa, data_criacao, data_ultima_modif, comentario, playlist_id, cancoes_playlist:CancaoId=[]) -> None:
        
        self.nome = nome
        self.descricao  = descricao
        self.img_capa  = img_capa
        self.data_criacao  = data_criacao
        self.data_ultima_modif = data_ultima_modif
        self.comentario = comentario
        self.playlist_id = playlist_id
        self.cancoes_playlist = cancoes_playlist
    
    def to_dict(self):
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'img_capa': self.img_capa,
            'data_criacao': self.data_criacao,
            'data_ultima_modif': self.data_ultima_modif,
            'comentario': self.comentario,
            'playlist_id': self.playlist_id,
            'cancoes_playlist': [c.to_dict() for c in self.cancoes_playlist]
        }
        