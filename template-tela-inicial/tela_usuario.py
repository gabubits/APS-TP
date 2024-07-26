from PySide6.QtGui import (
    QFontDatabase, QFont, QMouseEvent, QPixmap, QIcon,
    QScreen, QPainterPath, QPainter
)

from PySide6.QtWidgets import (
    QWidget, QFrame, QSizePolicy, QLabel, QMainWindow,
    QPushButton, QHBoxLayout, QGridLayout, QSpacerItem, QLineEdit,
    QVBoxLayout, QApplication, QTextEdit, QFileDialog,
    QMessageBox, QTableWidget,  QHeaderView,  QStackedWidget, QTableWidgetItem
)

from PySide6.QtCore import (
    Qt, QSize, QPoint, qAbs
)

from PySide6.QtCharts import QChart, QChartView, QPieSeries
import pathlib
import os
import sys
from persistencia.usuario_p import UsuarioP
from modelo.usuario import Usuario


class TelaBase(QMainWindow):
    def __init__(self, parent: QWidget | None,
                 titulo: str, tamanho: QSize) -> None:
        super().__init__(parent=parent)

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
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
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
    def __init__(self, usuario_p: UsuarioP) -> None:
        super().__init__(parent=None, titulo="Streamy", tamanho=QSize(1500, 900))

        tela_largura = 1500
        tela_altura = 900

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        botao_fechar = QPushButton()
        botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_fechar.setText("S")
        botao_fechar.setMaximumSize(QSize(25, 25))
        botao_fechar.clicked.connect(self.sair)

        botao_minimizar = QPushButton()
        botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_minimizar.setText("M")
        botao_minimizar.setMaximumSize(QSize(25, 25))
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

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, botao_playlists, botao_artistas]

        barra_topo_layout = QGridLayout(barra_topo)

        for i, botao in enumerate(botoes, 0):
            botao.setFixedSize(185, 35)
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setFont(self.fonte_botao)
            botao.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")
            barra_topo_layout.addWidget(botao, 0, i, Qt.AlignmentFlag.AlignCenter)

        barra_topo_layout.addLayout(botoes_layout, 0, len(botoes) + 1, Qt.AlignmentFlag.AlignRight)

        self.pilha_paginas = QStackedWidget()
        self.pilha_paginas.setMinimumSize(3 * (tela_largura / 4) - 50, tela_altura - 90)
        self.pilha_paginas.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        self.fonte_rotulo.setPointSize(25)

        pagina_modelo = QWidget()
        layout = QGridLayout(pagina_modelo)

        self.usuario_p = usuario_p
        self.usuario = self.usuario_p.buscar_email("streamy@streamy.com")[0]

        mensagem = QLabel("Bem-vindo, ")
        mensagem.setFont(self.fonte_rotulo)
        mensagem.setStyleSheet("margin-top:10px; font-size:25px; color:white;")
        layout.addWidget(mensagem, 0, 0, 1, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

    
       

        estilo_label = QLabel(" Seus estilos musicais mais ouvidos")
        estilo_label.setFont(self.fonte_rotulo)
        estilo_label.setStyleSheet("color: white; font-size: 25px; margin-top:10px; margin-bottom:5px;")
        layout.addWidget(estilo_label, 2, 0, 1, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        tabela = QTableWidget(5, 2)  
        tabela.setHorizontalHeaderLabels(["Estilo Musical", "Quantidade"])
        tabela.setItem(0, 0, QTableWidgetItem("Pop"))
        tabela.setItem(0, 1, QTableWidgetItem("10"))
        tabela.setItem(1, 0, QTableWidgetItem("Rock"))
        tabela.setItem(1, 1, QTableWidgetItem("8"))
        tabela.setItem(2, 0, QTableWidgetItem("Jazz"))
        tabela.setItem(2, 1, QTableWidgetItem("6"))
        tabela.setItem(3, 0, QTableWidgetItem("Clássica"))
        tabela.setItem(3, 1, QTableWidgetItem("5"))
        tabela.setItem(4, 0, QTableWidgetItem("Hip-Hop"))
        tabela.setItem(4, 1, QTableWidgetItem("7"))
        layout.addWidget(tabela, 3, 0, 1, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        layout.setRowStretch(5, 1)
        artistas = QLabel("Top Artistas desse mês")
        artistas.setFont(self.fonte_rotulo)
        artistas.setStyleSheet("color: white; font-size: 25px;margin-bottom:5px;")
        layout.addWidget(artistas, 4, 0, 1, 2, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
      


        tabela_artistas = QTableWidget(5, 3)  
        tabela_artistas.setHorizontalHeaderLabels(["Posição", "Artista", "Músicas"])
        
        
        dados = [
            ("1", "Artista 1", "15"),
            ("2", "Artista 2", "12"),
            ("3", "Artista 3", "10"),
            ("4", "Artista 4", "8"),
            ("5", "Artista 5", "7"),
        ]
        
        for i, (pos, artista, musicas) in enumerate(dados):
            tabela_artistas.setItem(i, 0, QTableWidgetItem(pos))
            tabela_artistas.setItem(i, 1, QTableWidgetItem(artista))
            tabela_artistas.setItem(i, 2, QTableWidgetItem(musicas))
        
        # Estilo para a tabela
        tabela_artistas.setStyleSheet("""
            QTableWidget {
                background-color: #121212;
                color: #FFFFFF;
                gridline-color: #3A3A3A;
                font-size: 14px;
                selection-background-color: #1DB954;
                margin:25px;
               
            }
            QHeaderView::section {
                background-color: #282828;
                color: #FFFFFF;
                padding: 4px;
                border: 1px solid #3A3A3A;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: #1DB954;
                color: white;
            }
        """)

        tabela_artistas.horizontalHeader().setStretchLastSection(True)
        tabela_artistas.verticalHeader().setVisible(False)
        tabela_artistas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(tabela_artistas)


# ------------ MODELAGEM TERMINA AQUI -----------------------

        self.pilha_paginas.addWidget(pagina_modelo)
        botao_usuarios.clicked.connect(lambda: self.changePage(0))

        self.pilha_paginas.setCurrentIndex(0)
        
        pagina_tocando = QWidget()
        pagina_tocando.setMinimumSize(tela_largura / 4, tela_altura - 90)
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
        usuario_p = UsuarioP()
        app = QApplication(sys.argv)
        tela = TelaPrincipal(usuario_p)
        tela.show()
        app.exec()


Template.inicializar()
