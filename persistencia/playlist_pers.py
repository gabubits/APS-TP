from persistencia.dao import DAO
from modelo.entidade import Entidade
from modelo.playlist import Playlist
from persistencia.cancao_pers import CancaoPers
from typing import List
from pathlib import Path
import os
import json
from dataclasses import asdict

class PlaylistPers(DAO):
    def __init__(self) -> None:
        super().__init__()
        if not getattr(self._instancia, "playlists", None):
            self.playlists: List[Entidade] = []
        else:
            self.playlists = self._instancia.playlists

    def carregar_dados(self) -> None:
        cp = CancaoPers()
        caminho_bd = Path("bd/playlists_bd.json").resolve()
        if not caminho_bd.parent.exists():
            os.mkdir(caminho_bd.parent)
        if caminho_bd.exists() and caminho_bd.stat().st_size != 0:
            with open(caminho_bd, 'r') as playlists_bd:
                dados = json.load(playlists_bd)
                for playlist_dict in dados:
                    cancoes = [cp.pesquisar("id", str(id))[0] for id in playlist_dict["cancoes"]]
                    self.playlists.append(Playlist.from_dict(playlist_dict, cancoes))

    def atualizar_dados(self) -> None:
        with open(Path("bd/playlists_bd.json").resolve(), 'w') as playlists_bd:
            json.dump([ent.asdict() for ent in self.playlists], playlists_bd, indent=4)

    def inserir(self, objeto: Entidade) -> None:
        if not len(self.playlists):
            objeto.id = 1
        else:
            objeto.id = self.playlists[-1].id + 1
        self.playlists.append(objeto)

    def remover(self, objeto: Entidade) -> None:
        for playlist_i in range(len(self.playlists)):
            if self.playlists[playlist_i].id == objeto.id:
                del self.playlists[playlist_i]
                return

    def pesquisar(self, atributo: str, valor: str) -> List[Entidade]:
        if atributo == 'id':
            for playlist in self.playlists:
                if str(getattr(playlist, atributo)) == valor:
                    return [playlist]

        return [playlist for playlist in self.playlists if valor == str(getattr(playlist, atributo))]

    def obter_tudo(self) -> List[Entidade]:
        return self.playlists
