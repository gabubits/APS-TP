from PySide6.QtGui import QCloseEvent
from .tela_base import *

from .tela_opcoes import TelaOpcoes
from modelo.artista import Artista
from .tela_adicionar_album import AdicionarAlbum 

class TelaCadastro(TelaBase):
    def __init__(self, parent: QWidget | None, controle: ControleContexto) -> None:
        super().__init__(parent = parent,
                         titulo = "[Player]* - Adicionar Artista",
                         tamanho = QSize(600, 750))
        
        self.controle = controle
        
        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.rotulo_boas_vindas = QLabel("Adicionar Artista")
        fonte_bv = QFont(self.fonte_principal, 20)
        fonte_bv.setWeight(QFont.Weight.DemiBold)
        self.rotulo_boas_vindas.setFont(fonte_bv)

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
        barra_topo_layout.addWidget(self.rotulo_boas_vindas, 0, 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, 2)

        self.form_cadastro = QFrame()
        self.form_cadastro.setMinimumSize(400, 600)
        self.form_cadastro.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.form_cadastro.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        form_cadastro_layout = QGridLayout(self.form_cadastro)

        rotulo_inicial = QLabel("Cadastro")
        rotulo_inicial.setWordWrap(True)
        fonte_mi = QFont(self.fonte_principal, 20)
        fonte_mi.setWeight(QFont.Weight.DemiBold)
        rotulo_inicial.setFont(fonte_mi)
        rotulo_inicial.setContentsMargins(0, 15, 0, 20)

        estilo_caixa_entrada = "border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey"
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        rotulo_nome = QLabel("Nome do Artista*")
        rotulo_nome.setFont(self.fonte_rotulo)
        rotulo_nome.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        self.entrada_nome = QLineEdit()
        self.entrada_nome.setObjectName("Nome do Artista")
        self.entrada_nome.setFont(self.fonte_entrada)
        self.entrada_nome.setFixedSize(380, 30)
        self.entrada_nome.setStyleSheet(estilo_caixa_entrada)
        self.entrada_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #rotulo_album = QLabel("Nome do Álbum*")
        #rotulo_album.setFont(self.fonte_rotulo)
        #rotulo_album.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        #self.entrada_album = QLineEdit()
        #self.entrada_album.setObjectName("Nome do Álbum")
        #self.entrada_album.setFont(self.fonte_entrada)
        #self.entrada_album.setFixedSize(380, 30)
        #self.entrada_album.setStyleSheet(estilo_caixa_entrada)
        #self.entrada_album.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_adicionar_album = QPushButton("Adicionar Álbum")
        botao_adicionar_album.setStyleSheet(estilo_botao)
        botao_adicionar_album.setFont(self.fonte_botao)
        botao_adicionar_album.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_adicionar_album.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        botao_adicionar_album.setStyleSheet("border-radius: 5px; background-color: white; color: black;")
        botao_adicionar_album.clicked.connect(self.abrir_tela_adicionar_albuns)

        self.botao_salvar = QPushButton("Salvar")
        self.botao_salvar.setFixedSize(125, 50)
        self.botao_salvar.setStyleSheet(estilo_botao)
        self.botao_salvar.setFont(self.fonte_botao)
        self.botao_salvar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_salvar.clicked.connect(self.verificar_informacoes)

        form_cadastro_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_cadastro_layout.addWidget(rotulo_inicial, 0, 0, Qt.AlignmentFlag.AlignCenter)
        form_cadastro_layout.addWidget(rotulo_nome, 1, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_nome, 2, 0)
        #form_cadastro_layout.addWidget(rotulo_album, 3, 0, Qt.AlignmentFlag.AlignCenter)
        #form_cadastro_layout.addWidget(self.entrada_album, 4, 0)
        form_cadastro_layout.addWidget(botao_adicionar_album, 4, 0)
        form_cadastro_layout.addWidget(self.botao_salvar, 6, 0, Qt.AlignmentFlag.AlignCenter)

        fcl_ajuste = QVBoxLayout()
        fcl_ajuste.addWidget(self.form_cadastro, 0, Qt.AlignmentFlag.AlignCenter)
        fcl_ajuste.setContentsMargins(0, 0, 0, 50)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addLayout(fcl_ajuste, 1, 0, 1, 0, Qt.AlignmentFlag.AlignTop)
    
    def fechar_e_voltar(self):
        self.hide()
        self.parentWidget().show()

    def abrir_tela_adicionar_albuns(self):
        AdicionarAlbum(self, self.controle).show() 
        self.hide()
    
    def verificar_informacoes(self):
        mandatoryInputs = [self.entrada_nome]

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
        
        self.controle.tipo_controle = UsuarioControle()
        if self.controle.pesquisar('nome_de_usuario', self.entrada_username.text()):
            MessageBox(
                self,
                'Falha na autenticação!',
                QMessageBox.Icon.Warning,
                f'"{self.entrada_username.text()}"'
                'já está registrado.'
                'Por favor, escolha outro Artista.'
            ).exec()
            return
        
        novo_artista = Artista(
            id = -1,
            nome_de_usuario = self.entrada_username.text(),
            nome=self.entrada_nome.text(),
            album=[]
            #single=[]
        )
        
        self.controle.inserir(novo_artista)

        MessageBox(self,
                   f'O artista {self.entrada_nome.text()}',
                   QMessageBox.Icon.Information,
                   'Foi adicionado com sucesso!').exec()

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