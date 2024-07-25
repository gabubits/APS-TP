from modelo.album import Album


class Artista:
    
    def __init__(self,nome,bio,img_perfil,nacionalidade,comentario,artista_id, albuns:Album=[]) -> None:
        self.nome = nome
        self.bio = bio
        self.img_perfil = img_perfil
        self.nacionalidade = nacionalidade       
        self.comentario = comentario
        self.artista_id = artista_id
        self.albuns = albuns
        
    
    def to_dict(self):
         return {
           'nome': self.nome,
            'bio': self.bio,
            'img_perfil': self.img_perfil,
            'nacionalidade': self.nacionalidade,
            'comentario': self.comentario,
            'artista_id':  self.artista_id,
            'albuns': [album.to_dict() for album in self.albuns]
         }
        
        
        
    
    