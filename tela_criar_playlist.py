from typing import List
from PySide6.QtGui import QCloseEvent

from modelo.cancao import Cancao
from modelo.playlist import Playlist
from .tela_base import *

from .tela_opcoes import TelaOpcoes
from modelo.usuario import Usuario

class TelaCriarPlaylist(TelaBase):
    def __init__(self,usuario:Usuario, parent:None, cancoes:List[Cancao]=[]) -> None:
        super().__init__(parent = parent,
                         titulo = "[Player]* - Cadastro de playlist",
                         tamanho = QSize(600, 750))
        self.controle = PlaylistControle()
        self.usuario_controle = UsuarioControle()
        self.cancoes = cancoes
        self.usuario = usuario
        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.rotulo_cadastro_playlist = QLabel("Criação de Playlist")
        fonte_bv = QFont(self.fonte_principal, 20)
        fonte_bv.setWeight(QFont.Weight.DemiBold)
        self.rotulo_cadastro_playlist.setFont(fonte_bv)

        self.botao_fechar = QPushButton()
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_fechar = QPixmap(pathlib.Path("visao/imgs/close.png").resolve())
        icon_fechar = QIcon(img_fechar)
        self.botao_fechar.setIcon(icon_fechar)
        self.botao_fechar.setIconSize(QSize(25,25))
        self.botao_fechar.setMaximumSize(QSize(25,25))
        self.botao_fechar.clicked.connect(sys.exit)

        self.botao_minimizar = QPushButton()
        self.botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_minimizar = QPixmap(pathlib.Path("visao/imgs/minimize.png").resolve())
        icon_minimizar = QIcon(img_minimizar)
        self.botao_minimizar.setIcon(icon_minimizar)
        self.botao_minimizar.setIconSize(QSize(25,25))
        self.botao_minimizar.setMaximumSize(QSize(25,25))
        self.botao_minimizar.clicked.connect(self.showMinimized)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        botoes_layout.addWidget(self.botao_minimizar)
        botoes_layout.addWidget(self.botao_fechar)

        self.botao_voltar = QPushButton()
        self.botao_voltar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_voltar = QPixmap(pathlib.Path("visao/imgs/arrow-left-white.png").resolve())
        icon_voltar = QIcon(img_voltar)
        self.botao_voltar.setIcon(icon_voltar)
        self.botao_voltar.setIconSize(QSize(25,25))
        self.botao_voltar.setMaximumSize(QSize(25,25))
        self.botao_voltar.clicked.connect(self.fechar_e_voltar)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(self.botao_voltar, 0, 0)
        barra_topo_layout.addWidget(self.rotulo_cadastro_playlist, 0, 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, 2)

        self.form_cadastro_playlist = QFrame()
        self.form_cadastro_playlist.setMinimumSize(400, 600)
        self.form_cadastro_playlist.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.form_cadastro_playlist.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        form_cadastro_playlist_layout = QGridLayout(self.form_cadastro_playlist)

        rotulo_inicial = QLabel("Nova Playlist")
        rotulo_inicial.setWordWrap(True)
        fonte_mi = QFont(self.fonte_principal, 20)
        fonte_mi.setWeight(QFont.Weight.DemiBold)
        rotulo_inicial.setFont(fonte_mi)
        rotulo_inicial.setContentsMargins(0, 15, 0, 20)

        estilo_caixa_entrada = "border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey"
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        rotulo_nome_playlist = QLabel("Nome da playlist *")
        rotulo_nome_playlist.setFont(self.fonte_rotulo)
        rotulo_nome_playlist.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        self.entrada_nome_playlist = QLineEdit()
        self.entrada_nome_playlist.setObjectName("Nome_playlist")
        self.entrada_nome_playlist.setFont(self.fonte_entrada)
        self.entrada_nome_playlist.setFixedSize(380, 30)
        self.entrada_nome_playlist.setStyleSheet(estilo_caixa_entrada)
        self.entrada_nome_playlist.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_descricao = QLabel("Descrição")
        rotulo_descricao.setFont(self.fonte_rotulo)
        rotulo_descricao.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        rotulo_descricao.setContentsMargins(0, 20, 0, 0)

        self.entrada_descricao = QTextEdit()
        self.entrada_descricao.setObjectName("Descricao")
        self.entrada_descricao.setFixedSize(380, 70)
        self.entrada_descricao.setFont(self.fonte_entrada)
        self.entrada_descricao.setStyleSheet(estilo_caixa_entrada)
        self.entrada_descricao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_foto_capa = QLabel("Foto da capa")
        rotulo_foto_capa.setFont(self.fonte_rotulo)
        rotulo_foto_capa.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        rotulo_foto_capa.setContentsMargins(0, 20, 0, 0)
    
        self.entrada_foto_capa = QLineEdit()
        self.entrada_foto_capa.setFixedSize(380, 30)
        self.entrada_foto_capa.setFont(self.fonte_entrada)
        self.entrada_foto_capa.setPlaceholderText("Caminho da imagem (.jpg ou .png)")
        self.entrada_foto_capa.setStyleSheet(estilo_caixa_entrada)
        self.entrada_foto_capa.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_enviar_foto_capa = QPushButton("Envie sa foto da capa (.jpg, .png)")
        botao_enviar_foto_capa.setStyleSheet(estilo_botao)
        botao_enviar_foto_capa.setFont(self.fonte_botao)
        botao_enviar_foto_capa.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_enviar_foto_capa.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        botao_enviar_foto_capa.setStyleSheet("border-radius: 5px; background-color: white; color: black;")
        botao_enviar_foto_capa.clicked.connect(self.enviar_img)

        self.botao_criar_playlist = QPushButton("Criar Playlist")
        self.botao_criar_playlist.setFixedSize(125, 50)
        self.botao_criar_playlist.setStyleSheet(estilo_botao)
        self.botao_criar_playlist.setFont(self.fonte_botao)
        self.botao_criar_playlist.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_criar_playlist.clicked.connect(self.verificar_informacoes)

        form_cadastro_playlist_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_cadastro_playlist_layout.addWidget(rotulo_inicial, 0, 0, Qt.AlignmentFlag.AlignCenter)
        form_cadastro_playlist_layout.addWidget(rotulo_nome_playlist, 1, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_playlist_layout.addWidget(self.entrada_nome_playlist, 2, 0)
        form_cadastro_playlist_layout.addWidget(rotulo_descricao, 3, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_playlist_layout.addWidget(self.entrada_descricao, 4, 0)
        form_cadastro_playlist_layout.addWidget(rotulo_foto_capa, 7, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_playlist_layout.addWidget(self.entrada_foto_capa, 8, 0)
        form_cadastro_playlist_layout.addWidget(botao_enviar_foto_capa, 9, 0)
        form_cadastro_playlist_layout.addWidget(self.botao_criar_playlist, 10, 0, Qt.AlignmentFlag.AlignCenter)

        fcl_ajuste = QVBoxLayout()
        fcl_ajuste.addWidget(self.form_cadastro_playlist, 0, Qt.AlignmentFlag.AlignCenter)
        fcl_ajuste.setContentsMargins(0, 0, 0, 50)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addLayout(fcl_ajuste, 1, 0, 1, 0, Qt.AlignmentFlag.AlignTop)
    
    
        
    def fechar_e_voltar(self):
        self.usuario_controle.atualizar_dados()
        self.hide()
        self.parentWidget().show()

    def enviar_img(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "Selecione sua imagem de perfil", 
                                                  os.getcwd(), "Image Files (*.png *.jpg *.jpeg)")
        self.entrada_foto_capa.setText(img_path)
    
    def verificar_informacoes(self):
        mandatoryInputs = [self.entrada_nome_playlist]

        emptyInputs =   [
                        _input.objectName() \
                        for _input in mandatoryInputs \
                        if len(_input.text().rstrip()) == 0
                        ]
        
        if emptyInputs:
            MessageBox(
                self,
                'Falha na autenticação!',
                QMessageBox.Icon.Critical,
                'Os campos obrigatórios não foram preenchidos:',
                emptyInputs
            ).exec()
            return
        
        if self.controle.pesquisar('nome', self.entrada_nome_playlist.text()):
            MessageBox(
                self,
                'Falha na autenticação!',
                QMessageBox.Icon.Warning,
                f'"{self.entrada_descricao.toPlainText()}"'
                'já está registrado.'
                'Por favor, escolha outro username.'
            ).exec()
            return       
        
        nova_playlist = Playlist(
            id= len(self.usuario.playlists),
            nome=self.entrada_nome_playlist.text(),
            descricao= self.entrada_descricao.toPlainText(),
            img_capa= self.entrada_foto_capa.text() if self.entrada_foto_capa.text()
                    else str(pathlib.Path('visao/imgs/playlist_padrao.jpg').resolve()),
                    cancoes=self.cancoes
                    
        )
        
        self.controle.inserir(nova_playlist)
        self.usuario_controle.inserir_playlist(self.usuario,nova_playlist)
        
        MessageBox(self,
                   'Playlist criada com sucesso!',
                   QMessageBox.Icon.Information,
                   'Você já pode ouviri sua nova playlist.').exec()

        self.fechar_e_voltar()
        
        

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.controle.tipo_controle = UsuarioControle()
        self.controle.atualizar_dados()
        self.controle.tipo_controle = AlbumControle()
        self.controle.atualizar_dados()
        self.controle.tipo_controle = CancaoControle()
        self.controle.atualizar_dados()
        self.controle.tipo_controle = ArtistaControle()
        self.controle.atualizar_dados()
        self.controle.tipo_controle = PlaylistControle()
        self.controle.atualizar_dados()
    
    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.verificar_informacoes()