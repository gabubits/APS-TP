from persistencia.dao import DAO
from modelo.entidade import Entidade
from modelo.artista import Artista
from persistencia.cancao_pers import CancaoPers
from persistencia.album_pers import AlbumPers
from typing import List
from pathlib import Path
import os
import json
from dataclasses import asdict

class ArtistaPers(DAO):
    def __init__(self) -> None:
        super().__init__()
        if not getattr(self._instancia, "artistas", None):
            self.artistas: List[Entidade] = []
        else:
            self.artistas = self._instancia.artistas

    def carregar_dados(self) -> None:
        cp = CancaoPers()
        ap = AlbumPers()
        caminho_bd = Path("bd/artistas_bd.json").resolve()
        if not caminho_bd.parent.exists():
            os.mkdir(caminho_bd.parent)
        if caminho_bd.exists() and caminho_bd.stat().st_size != 0:
            with open(caminho_bd, 'r') as artistas_bd:
                dados = json.load(artistas_bd)
                for artista_dict in dados:
                    singles = [cp.pesquisar("id", str(id))[0] for id in artista_dict["singles"]]
                    albuns = [ap.pesquisar("id", str(id))[0] for id in artista_dict["albuns"]]
                    self.artistas.append(Artista.from_dict(artista_dict, albuns, singles))
    
    def atualizar_dados(self) -> None:
        if self.artistas:
            with open(Path("bd/artistas_bd.json").resolve(), 'w') as artistas_bd:
                json.dump([ent.asdict() for ent in self.artistas], artistas_bd, indent=4)
    
    def inserir(self, objeto: Entidade) -> None:
        if not len(self.artistas):
            objeto.id = 1
        else:
            objeto.id = self.artistas[-1].id + 1
        self.artistas.append(objeto)
    
    def remover(self, objeto_id: int) -> None:
        for artista_i in range(len(self.artistas)):
            if self.cancoes[artista_i].id == objeto_id:
                del self.cancoes[artista_i]
                return
    
    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        if atributo == 'id' or atributo == 'nome':
            for artista in self.artistas:
                if str(getattr(artista, atributo)) == valor:
                    return [artista]
    
        return [artista for artista in self.artistas if valor == str(getattr(artista, atributo))]

    def obter_tudo(self) -> List[Entidade]:
        return self.artistas