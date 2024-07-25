class CancaoId:
    def __init__(self, artista_id, album_id, cancao_id) -> None:
        self.artista_id = artista_id
        self.album_id = album_id
        self.cancao_id = cancao_id
    
    def to_dict(self):
        return{
            'artista_id': self.artista_id,
            'album_id': self.album_id,
            'cancao_id': self.cancao_id
        }
        