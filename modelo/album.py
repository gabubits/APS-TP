from modelo.cancao import Cancao


class Album:
    def __init__(self, nome, descricao, img_capa, lancamento_ano, lancamento_dia, lancamento_mes, adicao_ano, adicao_dia,adicao_mes,type,comentario, artistas, album_id, cancoes:Cancao=[]) -> None:
        
        self.nome = nome
        self.descricao = descricao
        self.img_capa = img_capa
        self.lancamento_ano = lancamento_ano 
        self.lancamento_dia = lancamento_dia
        self.lancamento_mes = lancamento_mes
        self.adicao_ano = adicao_ano
        self.adicao_dia = adicao_dia
        self.adicao_mes = adicao_mes
        self.type = type
        self.comentario = comentario
        self.artistas = artistas
        self.album_id = album_id
        self.cancoes = cancoes
    
    def to_dict(self):
         return {
           'nome': self.nome,
            'descricao': self.descricao,
            'img_capa': self.img_capa,
            'lancamento_ano': self.lancamento_ano,
            'lancamento_dia': self.lancamento_dia,
            'lancamento_mes':  self.lancamento_mes,
            'adicao_ano': self.adicao_ano,
            'adicao_dia': self.adicao_dia,
            'adicao_mes': self.adicao_mes,
            'type': self.type,
            'comentario' : self.comentario,
            'artistas' : self.artistas,
            'album_id': self.album_id,
            'cancoes': [cancao.to_dict() for cancao in self.cancoes] 

         }
        
        
        