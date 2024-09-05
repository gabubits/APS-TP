from PySide6.QtWidgets import QApplication
from persistencia.usuario_pers import UsuarioPers
from visao.tela_criar_playlist import TelaCriarPlaylist
from controle.controle_contexto import ControleContexto


import sys

class Programa:
    @staticmethod
    
    
    
    def inicializar():
        persistencia = UsuarioPers()
        persistencia.carregar_dados()
        print(persistencia.usuarios[0])
        
        app = QApplication(sys.argv)
        tela = TelaCriarPlaylist(usuario=persistencia.usuarios[0],parent=None)
        tela.show()
        app.exec()

Programa.inicializar()