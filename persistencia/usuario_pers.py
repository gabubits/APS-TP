from persistencia.dao import DAO
from modelo.entidade import Entidade
from modelo.usuario import Usuario
from typing import List
from pathlib import Path
import os
import json
from dataclasses import asdict

class UsuarioPers(DAO):
    def __init__(self) -> None:
        super().__init__()
        if not getattr(self._instancia, "usuarios", None):
            self.usuarios: List[Entidade] = []
        else:
            self.usuarios = self._instancia.usuarios

    def carregar_dados(self) -> None:
        caminho_bd = Path("bd/usuarios_bd.json").resolve()
        if not caminho_bd.parent.exists():
            os.mkdir(caminho_bd.parent)
        if caminho_bd.exists() and caminho_bd.stat().st_size != 0:
            with open(caminho_bd, 'r') as usuarios_bd:
                dados = json.load(usuarios_bd)
                for usuario_dict in dados:
                    self.usuarios.append(Usuario.from_dict(usuario_dict))
    
    def atualizar_dados(self) -> None:
        if self.usuarios:
            with open(Path("bd/usuarios_bd.json").resolve(), 'w') as usuarios_bd:
                json.dump([asdict(ent) for ent in self.usuarios], usuarios_bd, indent=4)
    
    def inserir(self, objeto: Entidade) -> None:
        if not len(self.usuarios):
            objeto.id = 1
        else:
            objeto.id = self.usuarios[-1].id + 1
        self.usuarios.append(objeto)
    
    def remover(self, objeto_id: int) -> None:
        for usuario_i in range(len(self.usuarios)):
            if self.cancoes[usuario_i].id == objeto_id:
                del self.cancoes[usuario_i]
                return
    
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        if atributo == "id" or atributo == "nome_de_usuario":
            for usuario in self.usuarios:
                if str(getattr(usuario, atributo)) == valor:
                    return [usuario]
                    
        return [usuario for usuario in self.usuarios if valor in str(getattr(usuario, atributo))]

    def obter_tudo(self) -> List[Entidade]:
        return self.usuarios