from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from .utils.tela_base import *

from modelo.cancao import Cancao

from datetime import date

class TelaEditar(TelaBase):
    def __init__(self, parent: QWidget | None, audios,  controle, id_usuario) -> None:
        super().__init__(parent = parent, titulo="[Player]* - Edite suas canções", tamanho=QSize(600, 750))

        self.controle = controle
        self.id_usuario = id_usuario
        self.cancoes = []
        self.i = 0
        self.caixas_entrada = []

        self.form_musica = QStackedWidget()
        self.form_musica.setMinimumSize(400, 600)
        self.form_musica.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.form_musica.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        estilo_caixa_entrada = "border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey"
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        for i in range(len(audios)):

            pagina_cancao = QWidget()
            pc_layout = QGridLayout(pagina_cancao)
            rotulo_nome = QLabel("Digite o nome da canção: ")
            rotulo_nome.setFont(self.fonte_rotulo)
            rotulo_nome.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_nome = QLineEdit()
            entrada_nome.setObjectName("Nome da canção")
            entrada_nome.setFixedSize(380, 30)
            entrada_nome.setFont(self.fonte_entrada)
            entrada_nome.setStyleSheet(estilo_caixa_entrada)
            entrada_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixas_entrada.append(entrada_nome)

            rotulo_album = QLabel("Digite o nome do álbum: ")
            rotulo_album.setFont(self.fonte_rotulo)
            rotulo_album.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_album = QLineEdit()
            entrada_album.setObjectName("Nome do album")
            entrada_album.setFixedSize(380, 30)
            entrada_album.setFont(self.fonte_entrada)
            entrada_album.setStyleSheet(estilo_caixa_entrada)
            entrada_album.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixas_entrada.append(entrada_album)

            rotulo_artista = QLabel("Digite o nome do artista: ")
            rotulo_artista.setFont(self.fonte_rotulo)
            rotulo_artista.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_artista = QLineEdit()
            entrada_artista.setObjectName("Nome do artista")
            entrada_artista.setFixedSize(380, 30)
            entrada_artista.setFont(self.fonte_entrada)
            entrada_artista.setStyleSheet(estilo_caixa_entrada)
            entrada_artista.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixas_entrada.append(entrada_artista)

            rotulo_caminho = QLabel("Caminho do arquivo de audio:")
            rotulo_caminho.setFont(self.fonte_rotulo)
            rotulo_caminho.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_caminho = QLineEdit()
            entrada_caminho.setObjectName("Caminho audio")
            entrada_caminho.setFixedSize(380, 30)
            entrada_caminho.setFont(self.fonte_entrada)
            entrada_caminho.setStyleSheet(estilo_caixa_entrada)
            entrada_caminho.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entrada_caminho.setText(audios[i])
            entrada_caminho.setEnabled(False)
            self.caixas_entrada.append(entrada_caminho)

            if i == len(audios) - 1:
                botao_salvar = QPushButton("Salvar e finalizar")
                botao_salvar.setFixedSize(175, 50)
            else:
                botao_salvar = QPushButton("Salvar ->")
                botao_salvar.setFixedSize(125, 50)
            
            botao_salvar.clicked.connect(lambda: self.salvar())
            botao_salvar.setStyleSheet(estilo_botao)
            botao_salvar.setFont(self.fonte_botao)
            botao_salvar.setCursor(Qt.CursorShape.PointingHandCursor)

            pc_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            pc_layout.addWidget(rotulo_nome, 0, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_nome, 1, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_album, 2, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_album, 3, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_artista, 4, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_artista, 5, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_caminho, 6, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_caminho, 7, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(botao_salvar, 8, 0, Qt.AlignmentFlag.AlignCenter)
            
            self.form_musica.addWidget(pagina_cancao)
        
        self.widget_central_layout.addWidget(self.form_musica, 0, 0)
    
    def salvar(self):
        hoje = date.today()
        self.cancoes.append(Cancao(self.caixas_entrada[4 * self.i].text(),
                                   self.caixas_entrada[4 * self.i + 2].text(),
                                   'Pop',
                                   self.caixas_entrada[4 * self.i + 1].text(),
                                   self.caixas_entrada[4 * self.i + 3].text(),
                                   '', '', '', hoje.year, hoje.day, hoje.month,
                                   '', 0))
        self.i += 1
        if self.i == self.form_musica.count():
            self.controle.adicionar_musicas(self.id_usuario, self.cancoes)
            self.hide()
            return
        
        self.form_musica.setCurrentIndex(self.i)

