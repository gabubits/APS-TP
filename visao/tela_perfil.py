from PySide6.QtCore import (
    Qt, QEvent, QObject
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QTableWidget, QHeaderView, QHBoxLayout,
    QTableWidgetItem, QLabel, QFrame, QSizePolicy
)
from PySide6.QtGui import (
    QFont
)

from typing import Dict
from modelo.usuario import Usuario

from controle.controle_contexto import ControleContexto
from controle.usuario_controle import UsuarioControle

class QHLine(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setStyleSheet("background-color: white;")
        self.setLineWidth(3)

class UsuarioItemList(QListWidgetItem):
    def __init__(self, id, nome, username) -> None:
        super().__init__(f'{nome} ({username})')
        self.id = id

class TelaPerfil(QWidget):
    def __init__(self, parent,
                 fontes: Dict[str, QFont],
                 usuario: Usuario,
                 controle: ControleContexto) -> None:
        
        super().__init__(parent)

        self.controle = controle
        self.usuario = usuario
        layout = QGridLayout(self)

        rotulo_ola = QLabel("Olá!")
        rotulo_ola.setFont(fontes["lista"])

        rotulo_estatisticas = QLabel("Aqui serão exibidas estatísticas sobre as reproduções do usuário")
        rotulo_estatisticas.setFont(fontes["lista"])

        layout.addWidget(rotulo_ola, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QHLine(self), 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(rotulo_estatisticas, 2, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QHLine(self), 3, 0, Qt.AlignmentFlag.AlignCenter)

        if self.usuario.id == 1:
            self.caixa_pesquisa = QLineEdit()
            self.caixa_pesquisa.setFixedSize(380, 30)
            self.caixa_pesquisa.setStyleSheet(
                "border-radius: 15px;" +
                "background-color: rgb(18, 18, 18);" +
                "border: 1px solid grey"
            )
            self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixa_pesquisa.setPlaceholderText("Digite o nome do usuário :)")
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
            self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_usuario(self.caixa_pesquisa.text()))

            self.lista = QListWidget()
            self.lista.setStyleSheet(
                "border-radius: 5px;" +
                "background-color: rgb(18, 18, 18);" +
                "border: 1px solid grey"
            )
            self.lista.setFont(fontes["lista"])
            self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
            self.controle.tipo_controle = UsuarioControle()
            for usuario in self.controle.obter_tudo(): 
                if self.usuario.id != usuario.id:
                    self.lista.addItem(UsuarioItemList(usuario.id, usuario.nome, usuario.nome_de_usuario))
            self.lista.installEventFilter(self)

            layout_pesquisa = QGridLayout()
            layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
            layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

            layout.setSpacing(10)
            layout.addLayout(layout_pesquisa, 4, 0, Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(self.lista, 5, 0)
    
    def eventFilter(self, watched: QObject, event: QEvent):
        if event.type() == QEvent.Type.ContextMenu and watched is self.lista:
            menu = QMenu()
            acao_apagar = menu.addAction("Apagar perfil")
            acao_apagar.triggered.connect(self.remover_perfil)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)
    
    def remover_perfil(self):
        per_rem: UsuarioItemList = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        
        self.controle.tipo_controle = UsuarioControle()
        self.controle.remover(per_rem.id)

        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{per_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_usuario(self, texto: str):
        self.lista.clear()
        self.controle.tipo_controle = UsuarioControle()
        for usuario in self.controle.obter_tudo(): 
            if self.usuario.id != usuario.id:
                self.lista.addItem(UsuarioItemList(usuario.id, usuario.nome, usuario.nome_de_usuario))

        if len(texto.rstrip()) == 0:
            for index in range(self.lista.count()): 
                self.lista.item(index).setHidden(False)
            return
        for index in range(self.lista.count()):
            item = self.lista.item(index)
            if texto.rstrip() not in item.text(): 
                item.setHidden(True)
            else: item.setHidden(False)