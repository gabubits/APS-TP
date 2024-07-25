import json
from datetime import datetime

from modelo.album import Album
from modelo.artista import Artista
from modelo.cancao import Cancao
from modelo.cancao_id import CancaoId
from modelo.playlist import Playlist
from modelo.reproducao import Reproducao
from modelo.usuario import Usuario

class UsuarioP:
    
    def __init__(self) -> None:
        self.arquivo = 'persistencia/usuario.json'
        self.usuarios = self.obter_usuarios()
        
    def atualizar_arquivo(self):
        with open(self.arquivo, 'w') as arq:
            json.dump(self.to_dict(), arq, indent=4)
            
      
    def inserir(self, objeto: Usuario):
        self.usuarios.append(objeto)
        return True

    def excluir_usuario(self, objeto: Usuario):
        usuario = self.buscar_id(objeto.usuario_id)
        if not usuario:
            return False
        self.usuarios.remove(usuario)
    
    def buscar_id(self, id_usuario):
        result = [usuario for usuario in self.usuarios if usuario.usuario_id == id_usuario]
        return result[0] if len(result) else []
    
    def obter_usuarios(self):
        with open(self.arquivo, 'r') as arq:
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
        
    def buscar_username(self, username):
        return [usuario for usuario in self.usuarios if usuario.username == username]
         
    def buscar_nome(self, nome):
        return [usuario for usuario in self.usuarios if usuario.nome == nome]
    
    def to_dict(self):
        return [u.to_dict() for u in self.usuarios]

