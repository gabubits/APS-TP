from modelo.cancao import Cancao


class Album:
    def __init__(self, nome, descricao, img_capa, lancamento_ano, lancamento_dia, lancamento_mes, adicao_ano, adicao_dia,adicao_mes,type,comentario, artistas, album_id, cancoes:list[Cancao]=[]) -> None:
        
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

    def cancao_existente(self, titulo_cancao):
        for cancao in self.cancoes:
            if cancao.titulo.lower() == titulo_cancao:
                return True

        return False
    
    def adicionar_cancao(self, cancao: Cancao):
        if self.cancao_existente(cancao.titulo): return
        if len(self.cancoes) == 0:
            cancao.cancao_id = 1
        else:
            cancao.cancao_id = self.cancoes[-1].cancao_id + 1
        self.cancoes.append(cancao)
    
    def remover_cancao(self, cancao_id):
        for i in range(len(self.cancoes)):
            if self.cancoes[i] == cancao_id:
                del self.cancoes[i]
                return

    
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
        
        
        