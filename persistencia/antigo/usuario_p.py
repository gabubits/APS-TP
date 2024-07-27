import json
import pathlib
import os

from modelo.usuario import Usuario

class UsuarioP:

    def __init__(self):
        self.caminho_arquivo_bd: pathlib.Path = pathlib.Path("bd/bd_usuarios.json").resolve()
        self.usuarios: list[Usuario] = []
        if not self.caminho_arquivo_bd.parent.exists():
            os.mkdir(self.caminho_arquivo_bd.parent)
        if self.caminho_arquivo_bd.exists() and self.caminho_arquivo_bd.stat().st_size != 0:
            with open(self.caminho_arquivo_bd, 'r') as bd:
                usuarios_json = json.load(bd)
            for usuario in usuarios_json:
                self.usuarios.append(Usuario(
                    usuario['nome'], usuario['email'],
                    usuario['senha'], usuario['bio'],
                    usuario['img_perfil'], usuario['eh_adm'],
                    usuario['historico_ouvidas'],
                    usuario['cancoes_favoritas'],
                    usuario['albuns_favoritos'],
                    usuario['artistas_favoritos'],
                    usuario['playlists'],
                    usuario['amigos'],
                    usuario['solicitacoes_amizade']
                ))

    def atualizar_arquivo(self):
        with open(self.caminho_arquivo_bd, 'w') as arquivo:
            json.dump(self.to_dict(), arquivo)
    
    def inserir(self, objeto: Usuario):
        self.usuarios.append(objeto)

    def excluir(self, objeto: Usuario):
        usuario = self.buscar_email(objeto.email)
        if not usuario: return False
        self.usuarios.remove(usuario[0])
        return True

    def alterar_adm(self, objeto: Usuario):
        resultado = self.buscar_email(objeto.email)
        resultado[0].eh_adm = 1

    def buscar_email(self, email):
        return [usuario for usuario in self.usuarios if usuario.email == email]
         
    def buscar_nome(self, nome):
        return [usuario for usuario in self.usuarios if usuario.nome == nome]

    def to_dict(self):
        return [usuario.to_dict() for usuario in self.usuarios]