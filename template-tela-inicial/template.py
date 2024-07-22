from PySide6.QtGui import (
    QFontDatabase, QFont, QMouseEvent, QPixmap, QIcon,
    QScreen, QPainterPath, QPainter)

from PySide6.QtWidgets import (
    QWidget, QFrame, QSizePolicy, QLabel, QMainWindow,
    QPushButton, QHBoxLayout, QGridLayout, QLineEdit,
    QVBoxLayout, QApplication, QTextEdit, QFileDialog,
    QMessageBox, QListWidget, QStackedWidget)

from PySide6.QtCore import (
    Qt, QSize, QPoint, qAbs)

import pathlib
import os
import sys

class TelaBase(QMainWindow):
    def __init__(self, parent: QWidget | None,
                 titulo: str, tamanho: QSize) -> None:
        super().__init__(parent = parent)

        # Se você usa WINDOWS, verifique o caminho. Windows pode ser \\ e não /
        # Faça a instalação da fonte, se não a aplicação não funciona.
        fonte_id = QFontDatabase.addApplicationFont(str(pathlib.Path("template-tela-inicial/SF-Pro.ttf").resolve()))
        if fonte_id < 0:
            raise Exception("Falha na importação da fonte")
        self.fonte_principal = QFontDatabase.applicationFontFamilies(fonte_id)[0]

        self.fonte_rotulo = QFont(self.fonte_principal, 10)
        self.fonte_rotulo.setWeight(QFont.Weight.Medium)

        self.fonte_entrada = QFont(self.fonte_principal, 10)
        self.fonte_entrada.setWeight(QFont.Weight.Normal)

        self.fonte_botao = QFont(self.fonte_principal, 15)
        self.fonte_botao.setWeight(QFont.Weight.DemiBold)

        self.setWindowTitle(titulo)
        self.setMinimumSize(tamanho)
        self.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        self.centralizarTela()

        widget_central = QWidget()
        self.widget_central_layout = QGridLayout(widget_central)
        self.setCentralWidget(widget_central)

        self.oldPos = self.pos()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
    
    def centralizarTela(self) -> None:
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

class TelaPrincipal(TelaBase):
    def __init__(self) -> None:
        super().__init__(parent = None, 
                         titulo = "Streamy", 
                         tamanho = QSize(1500, 900))

        tela_largura = 1500
        tela_altura = 900

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        botao_fechar = QPushButton()
        botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_fechar.setText("S")
        """ img_fechar = QPixmap(pathlib.Path("visao/src/img/close.png").resolve())
        icon_fechar = QIcon(img_fechar)
        botao_fechar.setIcon(icon_fechar)
        botao_fechar.setIconSize(QSize(25,25)) """
        botao_fechar.setMaximumSize(QSize(25,25))
        botao_fechar.clicked.connect(self.sair)

        botao_minimizar = QPushButton()
        botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_minimizar.setText("M")
        """ img_minimizar = QPixmap(pathlib.Path("visao/src/img/minimize.png").resolve())
        icon_minimizar = QIcon(img_minimizar)
        botao_minimizar.setIcon(icon_minimizar)
        botao_minimizar.setIconSize(QSize(25,25)) """
        botao_minimizar.setMaximumSize(QSize(25,25))
        botao_minimizar.clicked.connect(self.showMinimized)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        botoes_layout.addWidget(botao_minimizar)
        botoes_layout.addWidget(botao_fechar)

        botao_usuarios = QPushButton("Usuários")
        botao_cancoes = QPushButton("Canções")
        botao_albuns = QPushButton("Álbuns")
        botao_playlists = QPushButton("Playlists")
        botao_artistas = QPushButton("Artistas")

        self.fonte_botao.setPointSize(15)

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, \
                       botao_playlists, botao_artistas]

        barra_topo_layout = QGridLayout(barra_topo)

        for i, botao in enumerate(botoes, 0):
            botao.setFixedSize(185, 35)
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setFont(self.fonte_botao)
            botao.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")
            barra_topo_layout.addWidget(botao, 0, i, Qt.AlignmentFlag.AlignCenter)

        barra_topo_layout.addLayout(botoes_layout, 0, len(botoes) + 1, Qt.AlignmentFlag.AlignRight)

        self.pilha_paginas = QStackedWidget()
        self.pilha_paginas.setMinimumSize(3 * (tela_largura/4) - 50, tela_altura - 90)
        self.pilha_paginas.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        self.fonte_rotulo.setPointSize(25)

        pagina_modelo = QWidget()
        layout = QGridLayout(pagina_modelo)

# ------------ MODELAGEM COMEÇA AQUI -----------------------
        rotulo_usuarios = QLabel("Modele AQUI!")
        rotulo_usuarios.setFont(self.fonte_rotulo)
        layout.addWidget(rotulo_usuarios, 0, 0, Qt.AlignmentFlag.AlignCenter)
# -----------------------------------------------------------
        self.pilha_paginas.addWidget(pagina_modelo)
        botao_usuarios.clicked.connect(lambda: self.changePage(0))

        self.pilha_paginas.setCurrentIndex(0)
        
        pagina_tocando = QWidget()
        pagina_tocando.setMinimumSize(tela_largura/4, tela_altura - 90)
        pagina_tocando.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")
        pagina_tocando_layout = QGridLayout(pagina_tocando)

        nowPlayingLabel = QLabel("Tocando agora (tela)")
        nowPlayingLabel.setWordWrap(True)
        nowPlayingLabel.setFont(self.fonte_rotulo)

        pagina_tocando_layout.addWidget(nowPlayingLabel, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        self.widget_central_layout.addWidget(self.pilha_paginas, 1, 0)
        self.widget_central_layout.addWidget(pagina_tocando, 1, 1)
    
    def close(self) -> bool:
        sys.exit()
    
    def changePage(self, index: int):
        if self.pilha_paginas.currentIndex() == index: return
        self.pilha_paginas.setCurrentIndex(index)

    def sair(self):
        self.close()

class Template:
    def __init__(self): pass

    @staticmethod
    def inicializar():
        app = QApplication(sys.argv)
        tela = TelaPrincipal()
        tela.show()
        app.exec()

Template.inicializar()
