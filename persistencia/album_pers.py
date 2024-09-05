from persistencia.dao import DAO
from modelo.entidade import Entidade
from modelo.album import Album
from persistencia.cancao_pers import CancaoPers
from typing import List
from pathlib import Path
import os
import json
from dataclasses import asdict

class AlbumPers(DAO):
    def __init__(self):
        super().__init__()
        if not getattr(self._instancia, "albuns", None):
            self.albuns: List[Entidade] = []
        else:
            self.albuns = self._instancia.albuns

    def carregar_dados(self) -> None:
        cp = CancaoPers()
        caminho_bd = Path("bd/albuns_bd.json").resolve()
        if not caminho_bd.parent.exists():
            os.mkdir(caminho_bd.parent)
        if caminho_bd.exists() and caminho_bd.stat().st_size != 0:
            with open(caminho_bd, 'r') as albuns_bd:
                dados = json.load(albuns_bd)
                for album_dict in dados:
                    cancoes = [cp.pesquisar("id", str(id))[0] for id in album_dict["cancoes"]]
                    self.albuns.append(Album.from_dict(album_dict, cancoes))
    
    def atualizar_dados(self) -> None:
        if self.albuns:
            with open(Path("bd/albuns_bd.json").resolve(), 'w') as albuns_bd:
                json.dump([ent.asdict() for ent in self.albuns], albuns_bd, indent=4)
    
    def inserir(self, objeto: Entidade) -> None:
        if not len(self.albuns):
            objeto.id = 1
        else:
            objeto.id = self.albuns[-1].id + 1
        self.albuns.append(objeto)
    
    def remover(self, objeto_id: int) -> None:
        for album_i in range(len(self.albuns)):
            if self.cancoes[album_i].id == objeto_id:
                del self.cancoes[album_i]
                return
    
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        if atributo == 'id':
            for album in self.albuns:
                if str(getattr(album, atributo)) == valor:
                    return [album]
    
        return [album for album in self.albuns if valor == str(getattr(album, atributo))]

    def obter_tudo(self) -> List[Entidade]:
        return self.albuns