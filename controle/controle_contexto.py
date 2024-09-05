# Classe que representa o contexto

from controle.tipo_controle import TipoControle
from modelo.entidade import Entidade
from typing import List

class ControleContexto:

    def __init__(self, tipo_controle: TipoControle) -> None:
        self.tipo_controle = tipo_controle
    
    def carregar_dados(self) -> None:
        return self.tipo_controle.persistencia.carregar_dados()
    
    def atualizar_dados(self) -> None:
        return self.tipo_controle.persistencia.atualizar_dados()
    
    def inserir(self, objeto: Entidade) -> None:
        return self.tipo_controle.persistencia.inserir(objeto)
    
    def remover(self, objeto: Entidade) -> None:
        return self.tipo_controle.persistencia.remover(objeto)
    
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        return self.tipo_controle.persistencia.pesquisar(atributo, valor)
    
    def obter_tudo(self) -> List[Entidade]:
        return self.tipo_controle.persistencia.obter_tudo()