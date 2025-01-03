from PySide6.QtGui import QCloseEvent, QKeyEvent
from .tela_cadastro import TelaCadastro
from .tela_opcoes import TelaOpcoes
from .tela_base import *

class TelaLogin(TelaBase):
    def __init__(self):
        super().__init__(parent = None, 
                         titulo = '[Player]* - Login', 
                         tamanho = QSize(600, 650))
        
        # Carregamento do banco de dados de usuários
        self.controle = ControleContexto(CancaoControle())
        self.controle.carregar_dados()
        self.controle.tipo_controle = PlaylistControle()
        self.controle.carregar_dados()
        self.controle.tipo_controle = AlbumControle()
        self.controle.carregar_dados()
        self.controle.tipo_controle = ArtistaControle()
        self.controle.carregar_dados()
        self.controle.tipo_controle = UsuarioControle()
        self.controle.carregar_dados()

        # Todos os componentes da tela são, agora, escritos com self
        # para que entrem nos modelos e fique visível, diagramaticamente,
        # o que a tela tem.

        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.rotulo_boas_vindas = QLabel("Bem-vindo ao [Player]*")
        fonte_bv = QFont(self.fonte_principal, 20)
        fonte_bv.setWeight(QFont.Weight.DemiBold)
        self.rotulo_boas_vindas.setFont(fonte_bv)

        self.botao_fechar = QPushButton()
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        close_pixmap = QPixmap(pathlib.Path("visao/imgs/close.png").resolve())
        close_icon = QIcon(close_pixmap)
        self.botao_fechar.setIcon(close_icon)
        self.botao_fechar.setIconSize(QSize(25,25))
        self.botao_fechar.setMaximumSize(QSize(25,25))
        self.botao_fechar.clicked.connect(self.close)

        self.botao_minimizar = QPushButton()
        self.botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        minimize_pixmap = QPixmap(pathlib.Path("visao/imgs/minimize.png").resolve())
        minimize_icon = QIcon(minimize_pixmap)
        self.botao_minimizar.setIcon(minimize_icon)
        self.botao_minimizar.setIconSize(QSize(25,25))
        self.botao_minimizar.setMaximumSize(QSize(25,25))
        self.botao_minimizar.clicked.connect(self.showMinimized)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        botoes_layout.addWidget(self.botao_minimizar)
        botoes_layout.addWidget(self.botao_fechar)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(self.rotulo_boas_vindas, 0, 0)
        barra_topo_layout.addLayout(botoes_layout, 0, 1)

        self.form_login = QFrame()
        self.form_login.setMinimumSize(400, 500)
        self.form_login.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.form_login.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        form_login_layout = QGridLayout(self.form_login)

        rotulo_login = QLabel("Login")
        fonte_rotulo_l = QFont(self.fonte_principal, 30)
        fonte_rotulo_l.setWeight(QFont.Weight.DemiBold)
        rotulo_login.setFont(fonte_rotulo_l)
        rotulo_login.setContentsMargins(0, 40, 0, 40)

        rotulo_username = QLabel("Username")
        rotulo_username.setFont(self.fonte_rotulo)

        self.entrada_username = QLineEdit()
        self.entrada_username.setFixedSize(380, 30)
        self.entrada_username.setStyleSheet("border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey")
        self.entrada_username.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_senha = QLabel("Senha")
        rotulo_senha.setFont(self.fonte_rotulo)
        rotulo_senha.setContentsMargins(0, 30, 0, 0)

        self.entrada_senha = QLineEdit()
        self.entrada_senha.setFixedSize(380, 30)
        self.entrada_senha.setStyleSheet("border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey")
        self.entrada_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.entrada_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        self.botao_logar = QPushButton("Entrar")
        self.botao_logar.setFixedSize(125, 50)
        self.botao_logar.setStyleSheet(estilo_botao)
        self.botao_logar.setFont(self.fonte_botao)
        self.botao_logar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_logar.clicked.connect(self.verificacao_login)

        rotulo_cadastrar = QLabel("Não tem uma conta? Crie agora!")
        rotulo_cadastrar.setFont(self.fonte_rotulo)
        rotulo_cadastrar.setContentsMargins(0, 50, 0, 0)

        self.botao_cadastrar = QPushButton("Criar conta")
        self.botao_cadastrar.setFixedSize(150, 50)
        self.botao_cadastrar.setStyleSheet(estilo_botao)
        self.botao_cadastrar.setFont(self.fonte_botao)
        self.botao_cadastrar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_cadastrar.clicked.connect(self.abrir_tela_cadastro)
        
        form_login_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_login_layout.addWidget(rotulo_login, 0, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(rotulo_username, 1, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.entrada_username, 2, 0)
        form_login_layout.addWidget(rotulo_senha, 3, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.entrada_senha, 4, 0)
        form_login_layout.addWidget(self.botao_logar, 5, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(rotulo_cadastrar, 6, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.botao_cadastrar, 7, 0, Qt.AlignmentFlag.AlignCenter)

        fll_ajuste = QVBoxLayout()
        fll_ajuste.addWidget(self.form_login, 0, Qt.AlignmentFlag.AlignCenter)
        fll_ajuste.setContentsMargins(0, 0, 0, 50)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addLayout(fll_ajuste, 1, 0, 1, 0, Qt.AlignmentFlag.AlignTop)
    
    def abrir_tela_cadastro(self):
        self.entrada_username.setText("")
        self.entrada_senha.setText("")
        TelaCadastro(self, self.controle).show()
        self.hide()
    
    def abrir_tela_ops(self, usuario):
        TelaOpcoes(self, usuario, self.controle).show()
        self.hide()
    
    def verificacao_login(self):
        username = self.entrada_username.text().rstrip()
        usuario = self.controle.pesquisar('nome_de_usuario', username)
        if not usuario:
            errorMessage = QMessageBox(self)
            errorMessage.setIcon(QMessageBox.Icon.Critical)
            errorMessage.setWindowTitle("Falha na autenticação!")
            errorMessage.setStandardButtons(QMessageBox.StandardButton.Ok)
            if len(username) != 0:
                errorMessage.setText(f"{username} não está cadastrado no sistema!")
            else:
                errorMessage.setText(f"Preencha os campos de cadastro!")
            self.entrada_username.setText("")
            errorMessage.exec()
            return
        # ******************
        if usuario[0].senha != self.entrada_senha.text().rstrip():
            errorMessage = QMessageBox(self)
            errorMessage.setIcon(QMessageBox.Icon.Critical)
            errorMessage.setWindowTitle("Falha na autenticação!")
            errorMessage.setStandardButtons(QMessageBox.StandardButton.Ok)
            errorMessage.setText(f"Sua senha está incorreta!")
            self.entrada_senha.setText("")
            errorMessage.exec()
            return
        
        self.abrir_tela_ops(usuario[0])
    
    def centralizarTela(self) -> None: return
    
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

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.verificacao_login()
