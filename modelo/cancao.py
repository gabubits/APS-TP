from modelo.reproducao import Reproducao


class Cancao:
     
      def __init__(self, titulo, artistas, genero, album, diretorio_audio, lancamento_ano, lancamento_dia, lancamento_mes, adicao_ano, adicao_dia, adicao_mes, comentario, cancao_id,reproducoes:Reproducao = []) -> None:
        self.titulo = titulo
        self.artistas = artistas
        self.genero = genero
        self.album = album
        self.diretorio_audio = diretorio_audio
        self.lancamento_ano = lancamento_ano
        self.lancamento_dia = lancamento_dia
        self.lancamento_mes = lancamento_mes
        self.adicao_ano = adicao_ano
        self.adicao_dia = adicao_dia
        self.adicao_mes = adicao_mes
        self.comentario = comentario
        self.cancao_id = cancao_id
        self.reproducoes = reproducoes
        
        
      def to_dict(self):
         return {
           'titulo': self.titulo,
            'artistas': self.artistas,
            'genero': self.genero,
            'album': self.album,
            'diretorio_audio': self.diretorio_audio,
            'lancamento_ano':  self.lancamento_ano,
            'lancamento_dia': self.lancamento_dia,
            'lancamento_mes': self.lancamento_mes,
            'adicao_ano': self.adicao_ano,
            'adicao_dia': self.adicao_dia,
            'adicao_mes': self.adicao_mes,
            'comentario': self.comentario,
            'cancao_id': self.cancao_id,
            'reproducoes' : [rep.to_dict() for rep in self.reproducoes]
         }