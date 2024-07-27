import json
from datetime import datetime

from modelo.album import Album
from modelo.artista import Artista
from modelo.cancao import Cancao
from modelo.cancao_id import CancaoId
from modelo.playlist import Playlist
from modelo.reproducao import Reproducao
from modelo.usuario import Usuario

import pathlib, os

class Persistencia:
    
    def __init__(self) -> bool:

        self.arquivo_bd = pathlib.Path("bd/bd.json").resolve()

        # Verifica se a pasta onde ficará o bd existe
        # Se não, cria
        if not self.arquivo_bd.parent.exists():
            os.mkdir(self.arquivo_bd.parent)
        
        # O arquivo de bd existe e não é vazio, carrega-o.
        # Se não existir, cria um array vazio.
        if self.arquivo_bd.exists() and self.arquivo_bd.stat().st_size != 0:
            self.usuarios: list[Usuario] = self.init_usuarios()
        else: 
            self.usuarios = []
    
    def obter_usuarios(self):
        return [[usuario.usuario_id, usuario.nome, usuario.username] for usuario in self.usuarios]

    def lista_usuarios_vazia(self):
        return not bool(len(self.usuarios))

    def atualizar_arquivo(self) -> None:
        if (self.lista_usuarios_vazia()): return
        with open(self.arquivo_bd, 'w') as arq:
            json.dump(self.to_dict(), arq, indent=4)
      
    def inserir_usuario(self, objeto: Usuario) -> None:
        if self.lista_usuarios_vazia():
            objeto.usuario_id = 1
        else:
            objeto.usuario_id = self.usuarios[-1].usuario_id + 1
        self.usuarios.append(objeto)

    def excluir_usuario(self, id_usuario) -> None:
        for i in range(len(self.usuarios)):
            if self.usuarios[i].usuario_id == id_usuario:
                del self.usuarios[i]
                return

    def buscar_username(self, username) -> int:
        for usuario in self.usuarios:
            if usuario.username.lower() == username.lower():
                return usuario.usuario_id
        return 0
    
    def buscar_id(self, id) -> Usuario:
        for usuario in self.usuarios:
            if usuario.usuario_id == id:
                return usuario
            
        return None
    
    def verificar_senha(self, id, entrada):
        return True if self.buscar_id(id).senha == entrada else False

    def obter_artistas(self, id):
        usuario = self.buscar_id(id)
        return [artista for artista in usuario.colecao]

    def excluir_artista(self, id, art_id):
        usuario = self.buscar_id(id)
        for i in range(len(usuario.colecao)):
            if usuario.colecao[i].artista_id == art_id:
                del usuario.colecao[i]
                return
            
    def obter_albuns(self, id_usuario):
        artistas = self.obter_artistas(id_usuario)
        resultado = []
        for artista in artistas:
            for album in artista.albuns:
                resultado.append([artista.artista_id, album.album_id, album.nome, album.artistas])
        return resultado

    def excluir_album(self, id_usuario, art_id, alb_id):
        artistas = self.obter_artistas(id_usuario)
        for i_art in range(len(artistas)):
            albuns = artistas[i_art].albuns
            for i_alb in range(len(albuns)):
                if artistas[i_art].artista_id == art_id and albuns[i_alb].album_id == alb_id:
                    del albuns[i_alb]
                    if not len(albuns): 
                        del artistas[i_art]
    
    def obter_cancoes(self, id_usuario):
        artistas = self.obter_artistas(id_usuario)
        resultado = []
        for artista in artistas:
            for album in artista.albuns:
                for cancao in album.cancoes:
                    resultado.append([artista.artista_id, album.album_id, cancao.cancao_id, cancao.titulo, cancao.artistas])
        return resultado

    def excluir_cancao(self, id_usuario, art_id, alb_id, can_id):
        artistas = self.obter_artistas(id_usuario)
        for i_art in range(len(artistas)):
            albuns = artistas[i_art].albuns
            for i_alb in range(len(albuns)):
                cancoes = albuns[i_alb].cancoes
                for i_can in range(len(cancoes)):
                    if artistas[i_art].artista_id == art_id and albuns[i_alb].album_id == alb_id and cancoes[i_can].cancao_id == can_id:
                        del cancoes[i_can]
                        if not len(cancoes): 
                            del albuns[i_alb]
                        if not len(albuns): 
                            del artistas[i_art]
                        return
    
    def adicionar_musicas(self, id_usuario: int, cancoes: list[Cancao]):
        usuario = self.buscar_id(id_usuario)
        for cancao in cancoes:
            artista = usuario.artista_na_colecao(cancao.artistas.lower())
            if not artista:
                artista = Artista(cancao.artistas, '', '', '', '', 0)
            album = artista.album_existente(cancao.album.lower())
            if not album:
                album = Album(cancao.album, '', '', '', '', '', cancao.adicao_ano, cancao.adicao_dia, cancao.adicao_mes, '', '', cancao.artistas, 0)
            can = album.cancao_existente(cancao.titulo.lower())
            if not can:
                album.adicionar_cancao(cancao)
                artista.adicionar_album(album)
                if not artista.artista_id:
                    usuario.add_colecao(artista)
            
    
    def init_usuarios(self) -> list[Usuario]:
        with open(self.arquivo_bd, 'r') as arq:
            data = json.load(arq)
        
        usuarios = []
        for user in data:
            colecao = []
            for artista in user['colecao']:
                albuns = []
                for album in artista['albuns']:
                    cancoes = []
                    for cancao in album['cancoes']:
                        reproducoes = [Reproducao(**rep) for rep in cancao.get('reproducoes', [])]
                        # Crie um dicionário de dados para Cancao
                        cancao_data = {
                            "titulo": cancao["titulo"],
                            "artistas": cancao["artistas"],
                            "genero": cancao["genero"],
                            "album": cancao["album"],
                            "diretorio_audio": cancao["diretorio_audio"],
                            "lancamento_ano": cancao["lancamento_ano"],
                            "lancamento_dia": cancao["lancamento_dia"],
                            "lancamento_mes": cancao["lancamento_mes"],
                            "adicao_ano": cancao["adicao_ano"],
                            "adicao_dia": cancao["adicao_dia"],
                            "adicao_mes": cancao["adicao_mes"],
                            "comentario": cancao["comentario"],
                            "cancao_id": cancao["cancao_id"],
                            "reproducoes": reproducoes
                        }
                        cancoes.append(Cancao(**cancao_data))
                        
                    album_data = {
                    'nome': album['nome'],
                    'descricao': album['descricao'],
                    'img_capa': album['img_capa'],
                    'lancamento_ano': album['lancamento_ano'],
                    'lancamento_dia': album['lancamento_dia'],
                    'lancamento_mes': album['lancamento_mes'],
                    'adicao_ano': album['adicao_ano'],
                    'adicao_dia': album['adicao_dia'],
                    'adicao_mes': album['adicao_mes'],
                    'type': album['type'],
                    'comentario': album['comentario'],
                    'artistas': album['artistas'],
                    'album_id': album['album_id'],
                    'cancoes': cancoes
                    }

                    albuns.append(Album(**album_data))
                    artista_data = {
                        'nome': artista['nome'],
                        'bio': artista['bio'],
                        'img_perfil': artista['img_perfil'],
                        'nacionalidade': artista['nacionalidade'],
                        'comentario': artista['comentario'],
                        'artista_id': artista['artista_id'],
                        'albuns': albuns
                    }
                
                colecao.append(Artista(**artista_data))

            playlists = []
            for playlist in user['playlists']:
                cancoes_playlist = [CancaoId(**cp) for cp in playlist.get('cancoes_playlist')]
                playlist_data = {
                    'nome': playlist['nome'],
                    'descricao': playlist['descricao'],
                    'img_capa': playlist['img_capa'],
                    'data_criacao': datetime.fromisoformat(playlist['data_criacao']),
                    'data_ultima_modif': datetime.fromisoformat(playlist['data_ultima_modif']),
                    'comentario': playlist['comentario'],
                    'playlist_id': playlist['playlist_id'],
                    'cancoes_playlist': cancoes_playlist
                }


        
                playlists.append(Playlist(**playlist_data))

            usuario_data = {
                'usuario_id': user['usuario_id'],
                'username':user['username'],
                'senha':user['senha'],
                'nome':user['nome'],
                'img_perfil':user['img_perfil'],
                'colecao': colecao,
                'playlists': playlists
            }

            usuarios.append(Usuario(**usuario_data))

        return usuarios
    
    def to_dict(self):
        return [u.to_dict() for u in self.usuarios]

