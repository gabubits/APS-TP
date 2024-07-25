from PySide6.QtGui import (
    QFontDatabase, QFont, QPixmap, QIcon, QScreen)

from PySide6.QtWidgets import (
    QWidget, QFrame, QSizePolicy, QLabel, QMainWindow,
    QPushButton, QHBoxLayout, QGridLayout, QLineEdit,
    QVBoxLayout, QApplication, QTextEdit, QFileDialog,
    QMessageBox, QTableWidget, QTableWidgetItem, QStackedWidget, QHeaderView)

from PySide6.QtCore import (
    Qt, QSize, QPoint)

import pathlib
import sys

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
    def __init__(self) -> None:
        super().__init__(parent=None, 
                         titulo="Streamy", 
                         tamanho=QSize(1500, 900))

        tela_largura = 1500
        tela_altura = 900

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        botao_fechar = QPushButton()
        botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_fechar.setText("S")
        botao_fechar.setMaximumSize(QSize(25,25))
        botao_fechar.clicked.connect(self.sair)

        botao_minimizar = QPushButton()
        botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_minimizar.setText("M")
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

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, 
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
        self.pilha_paginas.setMinimumSize(3 * (tela_largura / 4) - 50, tela_altura - 90)
        self.pilha_paginas.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        self.fonte_rotulo.setPointSize(25)

        # Definindo a página do modelo com tamanho inicial
        pagina_modelo = QWidget()
        layout = QGridLayout(pagina_modelo)

        # ------------ MODELAGEM COMEÇA AQUI -----------------------

        # Caixa de pesquisa
        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setPlaceholderText("Pesquisar música ou cantor...")
        self.caixa_pesquisa.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 10px;
                padding: 5px;
                font-size: 15px;
            }
        """)
        self.caixa_pesquisa.setMinimumHeight(40)  # Aumenta um pouco o tamanho
        self.caixa_pesquisa.textChanged.connect(self.filtrar_tabela)


        # Configura o QTableWidget
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Música", "Cantor", "Duração"])
        self.tabela.setStyleSheet("""
            QTableWidget {
                background-color: rgb(18, 18, 18);
                color: white;
            }
            QHeaderView::section {
                background-color: rgb(21, 21, 21);
                border: none;
                color: white;
            }
            QTableWidget::item {
                border: none;
                padding: 10px;
            }
            QTableWidget::item:selected {
                background-color: rgb(30, 30, 30);
            }
        """)
        self.tabela.setFont(QFont(self.fonte_principal, 15))
        
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        
        # Definindo o comportamento de seleção
        self.tabela.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        
        # Remove a marcação de índice das linhas e a grade
        self.tabela.setShowGrid(False)
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setVisible(False)
        
        # Adiciona os itens à tabela
        self.adicionar_album("musica 01musica 01musica 01", "cantor", "3:45")
        self.adicionar_album("musica 02", "cantor", "4:20")
        self.adicionar_album("musica 03", "cantor", "2:30")
        self.adicionar_album("musica 04", "cantor", "2:30")
        self.adicionar_album("musica 05", "cantorcantor", "3:45")
        self.adicionar_album("musica 06", "cantor", "4:20")
        self.adicionar_album("musica 07", "cantor", "2:30")
        self.adicionar_album("musica 08", "cantor", "2:30")
        self.adicionar_album("musica 09", "cantor", "3:45")
        self.adicionar_album("musica 10", "cantor", "4:20")
        self.adicionar_album("musica 11", "cantor", "2:30")
        self.adicionar_album("musica 12", "cantor", "2:30")

        # Adiciona a caixa de pesquisa e a tabela ao layout
        layout.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.tabela, 1, 0)

        layout.setRowStretch(1, 1)  # Permite que a tabela expanda verticalmente
        layout.setColumnStretch(0, 1)  # Permite que a tabela expanda horizontalmente
        # -----------------------------------------------------------

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
    
    def adicionar_album(self, nome_musica: str, cantor: str, duracao: str):
        row_position = self.tabela.rowCount()
        self.tabela.insertRow(row_position)
        self.tabela.setItem(row_position, 0, QTableWidgetItem(nome_musica))
        self.tabela.setItem(row_position, 1, QTableWidgetItem(cantor))
        self.tabela.setItem(row_position, 2, QTableWidgetItem(duracao))

    def filtrar_tabela(self):
        filtro = self.caixa_pesquisa.text().lower()
        for row in range(self.tabela.rowCount()):
            musica_item = self.tabela.item(row, 0).text().lower()
            cantor_item = self.tabela.item(row, 1).text().lower()
            if filtro in musica_item or filtro in cantor_item:
                self.tabela.setRowHidden(row, False)
            else:
                self.tabela.setRowHidden(row, True)

    def close(self) -> bool:
        sys.exit()
    
    def changePage(self, index: int):
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
