from persistencia.dao import DAO
from modelo.entidade import Entidade
from modelo.cancao import Cancao
from typing import List
from pathlib import Path
import os
import json
from dataclasses import asdict

class CancaoPers(DAO):
    def __init__(self) -> None:
        super().__init__()
        if not getattr(self._instancia, "cancoes", None):
            self.cancoes: List[Entidade] = []
        else:
            self.cancoes = self._instancia.cancoes
            
    def carregar_dados(self) -> None:
        caminho_bd = Path("bd/cancoes_bd.json").resolve()
        if not caminho_bd.parent.exists():
            os.mkdir(caminho_bd.parent)
        if caminho_bd.exists() and caminho_bd.stat().st_size != 0:
            with open(caminho_bd, 'r') as cancoes_bd:
                dados = json.load(cancoes_bd)
                for cancao_dict in dados:
                    self.cancoes.append(Cancao.from_dict(cancao_dict))
    
    def atualizar_dados(self) -> None:
        if self.cancoes:
            with open(Path("bd/cancoes_bd.json").resolve(), 'w') as cancoes_bd:
                json.dump([asdict(ent) for ent in self.cancoes], cancoes_bd, indent=4)
    
    def inserir(self, objeto: Entidade) -> None:
        if not len(self.cancoes):
            objeto.id = 1
        else:
            objeto.id = self.cancoes[-1].id + 1
        self.cancoes.append(objeto)
    
    def remover(self, objeto_id: int) -> None:
        for cancao_i in range(len(self.cancoes)):
            if self.cancoes[cancao_i].id == objeto_id:
                del self.cancoes[cancao_i]
                return
    
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        if atributo == 'id':
            for cancao in self.cancoes:
                if str(getattr(cancao, atributo)) == valor:
                    return [cancao]
    
        return [cancao for cancao in self.cancoes if valor == str(getattr(cancao, atributo))]

    def obter_tudo(self) -> List[Entidade]:
        return self.cancoes