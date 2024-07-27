from PySide6.QtCore import (
    Qt, QEvent, QObject
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QTableWidget, QHeaderView, QHBoxLayout,
    QTableWidgetItem
)
from PySide6.QtGui import (
    QFont
)

from typing import Dict

class AlbumItemList(QListWidgetItem):
    def __init__(self, artista_id, album_id, album_nome, album_artistas) -> None:
        super().__init__(f'{album_nome} - {album_artistas}')
        self.art_id = artista_id
        self.alb_id = album_id

class TelaAlbuns(QWidget):
    def __init__(self,
                 fontes: Dict[str, QFont],
                 id_usuario,
                 controle) -> None:
        
        super().__init__()

        self.controle = controle
        self.id_usuario = id_usuario

        layout = QGridLayout(self)

        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setFixedSize(380, 30)
        self.caixa_pesquisa.setStyleSheet(
            "border-radius: 15px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caixa_pesquisa.setPlaceholderText("Digite o nome do álbum :)")
        self.caixa_pesquisa.setFont(fontes["entrada"])

        self.botao_pesquisar = QPushButton("Pesquisar")
        self.botao_pesquisar.setFixedSize(200, 30)
        self.botao_pesquisar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_pesquisar.setFont(fontes["botao"])
        self.botao_pesquisar.setStyleSheet(
            "background-color: rgba(255,255,255,0.9);" +
            "color: black;" +
            "border-radius: 15px;"
        )
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_album(self.caixa_pesquisa.text()))

        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        for album in self.controle.obter_albuns(self.id_usuario): 
            self.lista.addItem(AlbumItemList(album[0], album[1], album[2], album[3]))
        self.lista.installEventFilter(self)

        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lista, 1, 0)
    
    def eventFilter(self, watched: QObject, event: QEvent):
        if event.type() == QEvent.Type.ContextMenu and watched is self.lista:
            menu = QMenu()
            acao_apagar = menu.addAction("Apagar álbum")
            acao_apagar.triggered.connect(self.remover_album)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)
    
    def remover_album(self):
        alb_rem = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        self.controle.excluir_album(self.id_usuario, alb_rem.art_id, alb_rem.alb_id)
        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{alb_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_album(self, texto: str):
        self.lista.clear()
        for album in self.controle.obter_albuns(self.id_usuario): 
            self.lista.addItem(AlbumItemList(album[0], album[1], album[2], album[3]))

        if len(texto.rstrip()) == 0:
            for index in range(self.lista.count()): 
                self.lista.item(index).setHidden(False)
            return
        for index in range(self.lista.count()):
            item = self.lista.item(index)
            if texto.rstrip() not in item.text(): 
                item.setHidden(True)
            else: item.setHidden(False)

        """ self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Álbum", "Artista(s)"])
        self.tabela.setStyleSheet("""
        """ QTableWidget {
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
            } """
        """)
        self.tabela.setFont(fontes['tabela'])
        
        header = self.tabela.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        
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
        self.adicionar_album("musica 05", "cantor", "3:45")
        self.adicionar_album("musica 06", "cantor", "4:20")
        self.adicionar_album("musica 07", "cantor", "2:30")
        self.adicionar_album("musica 08", "cantor", "2:30")
        self.adicionar_album("musica 09", "cantor", "3:45")
        self.adicionar_album("musica 10", "cantor", "4:20")
        self.adicionar_album("musica 11", "cantor", "2:30")
        self.adicionar_album("musica 12", "cantor", "2:30")

        # Adiciona a tabela ao layout
        layout.addWidget(self.tabela, 1, 0, 1, 2)

        # Adiciona a seção de pesquisa
        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setPlaceholderText("Digite o nome da música ou artista : ")
        self.caixa_pesquisa.setStyleSheet("""
        """ QLineEdit {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 15px;
                padding: 5px;
                font-size: 15px;
            } """
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
    
    def adicionar_album(self, album, artista):
        rowPosition = self.tabela.rowCount()
        self.tabela.insertRow(rowPosition)
        self.tabela.setItem(rowPosition, 0, QTableWidgetItem(nome))
        self.tabela.setItem(rowPosition, 1, QTableWidgetItem(cantor))
        self.tabela.setItem(rowPosition, 2, QTableWidgetItem(duracao))

    def filtrar_tabela(self, texto: str) -> None:
        for row in range(self.tabela.rowCount()):
            item_nome = self.tabela.item(row, 0)
            item_cantor = self.tabela.item(row, 1)
            if texto.lower() in item_nome.text().lower() or texto.lower() in item_cantor.text().lower():
                self.tabela.setRowHidden(row, False)
            else:
                self.tabela.setRowHidden(row, True) """