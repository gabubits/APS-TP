from PySide6.QtGui import (
    QFontDatabase, QFont, QMouseEvent, QPixmap, QIcon,
    QScreen, QPainterPath, QPainter)

from PySide6.QtWidgets import (
    QWidget, QFrame, QSizePolicy, QLabel, QMainWindow,
    QPushButton, QHBoxLayout, QGridLayout, QLineEdit,
    QVBoxLayout, QApplication, QTextEdit, QFileDialog,
    QMessageBox, QListWidget, QStackedWidget, QTableWidget, QHeaderView, QTableWidgetItem)

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
        fonte_id = QFontDatabase.addApplicationFont(str(pathlib.Path("SF-Pro.ttf").resolve()))
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

        # Adiciona a seção de pesquisa
        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setPlaceholderText("Digite o que deseja filtrar: ")
        self.caixa_pesquisa.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                padding: 5px;
                font-size: 15px;
            }
        """)
        self.caixa_pesquisa.setFixedSize(380, 30)
        self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caixa_pesquisa.textChanged.connect(self.filtrar_tabela)

        self.botao_pesquisar = QPushButton("Pesquisar")
        self.botao_pesquisar.setFixedSize(200, 30)
        self.botao_pesquisar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_pesquisar.setFont(self.fonte_botao)
        self.botao_pesquisar.setStyleSheet(
            "background-color: rgba(255,255,255,0.9);" +
            "color: black;" +
            "border-radius: 15px;"
        )
        self.botao_pesquisar.clicked.connect(lambda: self.filtrar_tabela(self.caixa_pesquisa.text()))

        layout_pesquisa = QHBoxLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa)
        layout_pesquisa.addWidget(self.botao_pesquisar)

        layout.addLayout(layout_pesquisa, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        
        # Criação da tabela
        self.tabela = QTableWidget()
        layout.addWidget(self.tabela)

        # Configuração das dimensões da tabela
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels(["", "# Título", "Artista", "Gênero"])
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: rgb(18, 18, 18);
                color: white;
            }
            QHeaderView::section {
                background-color: rgb(21, 21, 21);
                border: none;
                color: white;
                text-align: left; 
                padding-left: 10px;
            }
            QTableWidget::item {
                border: none;
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: rgb(30, 30, 30)
            }
        """)
        self.tabela.setFont(QFont(self.fonte_principal, 15))

        # Ajusta as colunas para o tamanho do conteúdo
        self.tabela.setColumnWidth(0, 100)
        self.tabela.setColumnWidth(1, 300)
        self.tabela.setColumnWidth(2, 300)
        self.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

        # Mostrar apenas a linha de grade horizontal do cabeçalho
        cabecalho = self.tabela.horizontalHeader()
        cabecalho.setStyleSheet("border-bottom: 1px solid white; border-right: none;")

        fonte_cabecalho = QFont(self.fonte_principal, 15, QFont.Bold)
        self.tabela.horizontalHeader().setFont(fonte_cabecalho)
        self.tabela.horizontalHeader().setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # Definindo o comportamento de seleção
        self.tabela.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        
        # Remove a marcação de índice das linhas e a grade
        self.tabela.setShowGrid(False)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setVisible(True)

        # Ícones
        icone_play = QTableWidgetItem()
        icone_play.setIcon(QIcon("play.png"))

        # Adiciona os itens à tabela
        self.adicionar_cancao("Tudo", "Liniker", "Bom demais é")
        self.adicionar_cancao("MY HOUSE", "Beyoncé", "POP")
        self.adicionar_cancao("Rockstar", "LISA", "K-Pop")
        
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


    def adicionar_cancao(self, titulo, artista, genero):
        icone_play = QTableWidgetItem() 
        icone_play.setIcon(QIcon("play.png")) # caminho para o Ícone
        rowPosition = self.tabela.rowCount()
        self.tabela.insertRow(rowPosition)
        self.tabela.setItem(rowPosition, 0, icone_play)
        self.tabela.setItem(rowPosition, 1, QTableWidgetItem(titulo))
        self.tabela.setItem(rowPosition, 2, QTableWidgetItem(artista))
        self.tabela.setItem(rowPosition, 3, QTableWidgetItem(genero))

    def filtrar_tabela(self, texto: str) -> None:
        for row in range(self.tabela.rowCount()):
            item_titulo = self.tabela.item(row, 1)
            item_artista = self.tabela.item(row, 2)
            item_genero = self.tabela.item(row, 3)
            if texto.lower() in item_titulo.text().lower() or texto.lower() in item_genero.text().lower() or texto.lower() in item_artista.text().lower():
                self.tabela.setRowHidden(row, False)
            else:
                self.tabela.setRowHidden(row, True)
    
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
