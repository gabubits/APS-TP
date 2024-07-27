from modelo.album import Album


class Artista:
    
    def __init__(self,nome,bio,img_perfil,nacionalidade,comentario,artista_id, albuns:list[Album]=[]) -> None:
        self.nome = nome
        self.bio = bio
        self.img_perfil = img_perfil
        self.nacionalidade = nacionalidade       
        self.comentario = comentario
        self.artista_id = artista_id
        self.albuns = albuns
    
    def adicionar_album(self, album: Album):
        if self.album_existente(album.nome): return
        if len(self.albuns) == 0:
            album.album_id = 1
        else:
            album.album_id = self.albuns[-1].album_id + 1
        self.albuns.append(album)
    
    def remover_album(self, album_id):
        for i in range(len(self.albuns)):
            if self.albuns[i] == album_id:
                del self.albuns[i]
                return
    
    def album_existente(self, nome_album):
        for album in self.albuns:
            if album.nome.lower() == nome_album:
                return album
        
        return None
    
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
        
        
        
    
    