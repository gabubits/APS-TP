class Reproducao:
    
    def __init__(self, hora, minuto, segundo, dia, mes, ano):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def to_dict(self):
         return {
            'hora': self.hora,
            'minuto': self.minuto,
            'segundo': self.segundo,
            'dia': self.dia,
            'mes': self.mes,
            'ano':  self.ano,
         }
        
        
        