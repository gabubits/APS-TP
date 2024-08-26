from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from .tela_base import *

from modelo.cancao import Cancao
from modelo.usuario import Usuario

from datetime import datetime

class TelaEditar(TelaBase):
    def __init__(self, parent: QWidget | None, audios: list, controle: ControleContexto, usuario: Usuario) -> None:
        super().__init__(parent = parent, titulo="[Player]* - Edite suas canções", tamanho=QSize(600, 750))

        self.controle = controle
        self.usuario = usuario
        self.cancoes = []
        self.i = 0
        self.caixas_entrada = []

        self.form_musica = QStackedWidget()
        self.form_musica.setMinimumSize(400, 600)
        self.form_musica.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.form_musica.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        estilo_caixa_entrada = "border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey"
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        # Itera sobre as canções a serem adicionadas
        # Define seus dados da canção
        # Adiciona em um array essas informações para serem
        # adicionadas de uma vez no último clique
        # na última tela dos aúdios a serem adicionados
        for i in range(len(audios)):

            pagina_cancao = QWidget()
            pc_layout = QGridLayout(pagina_cancao)
            rotulo_nome = QLabel("Digite o nome da canção: ")
            rotulo_nome.setFont(self.fonte_rotulo)
            rotulo_nome.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_nome = QLineEdit()
            entrada_nome.setObjectName("Título da canção")
            entrada_nome.setFixedSize(380, 30)
            entrada_nome.setFont(self.fonte_entrada)
            entrada_nome.setStyleSheet(estilo_caixa_entrada)
            entrada_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixas_entrada.append(entrada_nome)

            rotulo_genero = QLabel("Digite o gênero da canção: ")
            rotulo_genero.setFont(self.fonte_rotulo)
            rotulo_genero.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            entrada_genero = QLineEdit()
            entrada_genero.setObjectName("Gênero da canção")
            entrada_genero.setFixedSize(380, 30)
            entrada_genero.setFont(self.fonte_entrada)
            entrada_genero.setStyleSheet(estilo_caixa_entrada)
            entrada_genero.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.caixas_entrada.append(entrada_genero)

            rotulo_album = QLabel("Digite o título do álbum: ")
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
            pc_layout.addWidget(rotulo_genero, 2, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_genero, 3, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_album, 4, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_album, 5, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_artista, 6, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_artista, 7, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(rotulo_caminho, 8, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(entrada_caminho, 9, 0, Qt.AlignmentFlag.AlignCenter)
            pc_layout.addWidget(botao_salvar, 10, 0, Qt.AlignmentFlag.AlignCenter)
            
            self.form_musica.addWidget(pagina_cancao)
        
        self.widget_central_layout.addWidget(self.form_musica, 0, 0)
    
    def salvar(self):
        
        ## Aqui será criada a lógica de adicionar canções

        self.i += 1
        # Todas as canções tiveram seus dados definidos
        # Hora de salvar na persistência e nos dados do usuário
        if self.i == self.form_musica.count():
            pass
            return
        
        self.form_musica.setCurrentIndex(self.i)

