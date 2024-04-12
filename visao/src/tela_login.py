from .tela_cadastro import TelaCadastro
from .tela_opcoes import TelaOpcoes
from .utils.tela_base import *

class TelaLogin(TelaBase):
    def __init__(self):
        super().__init__(parent = None, 
                         titulo = 'Streamy', 
                         tamanho = QSize(600, 650))

        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        rotulo_boas_vindas = QLabel("Welcome to Streamy!")
        fonte_bv = QFont(self.fonte_principal, 20)
        fonte_bv.setWeight(QFont.Weight.DemiBold)
        rotulo_boas_vindas.setFont(fonte_bv)

        botao_fechar = QPushButton()
        botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        close_pixmap = QPixmap(pathlib.Path("visao/src/img/close.png").resolve())
        close_icon = QIcon(close_pixmap)
        botao_fechar.setIcon(close_icon)
        botao_fechar.setIconSize(QSize(25,25))
        botao_fechar.setMaximumSize(QSize(25,25))
        botao_fechar.clicked.connect(self.close)

        botao_minimizar = QPushButton()
        botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        minimize_pixmap = QPixmap(pathlib.Path("visao/src/img/minimize.png").resolve())
        minimize_icon = QIcon(minimize_pixmap)
        botao_minimizar.setIcon(minimize_icon)
        botao_minimizar.setIconSize(QSize(25,25))
        botao_minimizar.setMaximumSize(QSize(25,25))
        botao_minimizar.clicked.connect(self.showMinimized)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        botoes_layout.addWidget(botao_minimizar)
        botoes_layout.addWidget(botao_fechar)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(rotulo_boas_vindas, 0, 0)
        barra_topo_layout.addLayout(botoes_layout, 0, 1)

        form_login = QFrame()
        form_login.setMinimumSize(400, 500)
        form_login.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        form_login.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        form_login_layout = QGridLayout(form_login)

        rotulo_login = QLabel("Login")
        fonte_rotulo_l = QFont(self.fonte_principal, 30)
        fonte_rotulo_l.setWeight(QFont.Weight.DemiBold)
        rotulo_login.setFont(fonte_rotulo_l)
        rotulo_login.setContentsMargins(0, 40, 0, 40)

        rotulo_email = QLabel("E-mail Address")
        rotulo_email.setFont(self.fonte_rotulo)

        self.entrada_email = QLineEdit()
        self.entrada_email.setFixedSize(380, 30)
        self.entrada_email.setStyleSheet("border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey")
        self.entrada_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_senha = QLabel("Password")
        rotulo_senha.setFont(self.fonte_rotulo)
        rotulo_senha.setContentsMargins(0, 30, 0, 0)

        self.entrada_senha = QLineEdit()
        self.entrada_senha.setFixedSize(380, 30)
        self.entrada_senha.setStyleSheet("border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey")
        self.entrada_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.entrada_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        self.botao_logar = QPushButton("Sign In")
        self.botao_logar.setFixedSize(125, 50)
        self.botao_logar.setStyleSheet(estilo_botao)
        self.botao_logar.setFont(self.fonte_botao)
        self.botao_logar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_logar.clicked.connect(self.openOptionsWindow)

        rotulo_cadastrar = QLabel("Don't have an account?")
        rotulo_cadastrar.setFont(self.fonte_rotulo)
        rotulo_cadastrar.setContentsMargins(0, 50, 0, 0)

        self.botao_cadastrar = QPushButton("Create Account")
        self.botao_cadastrar.setFixedSize(150, 50)
        self.botao_cadastrar.setStyleSheet(estilo_botao)
        self.botao_cadastrar.setFont(self.fonte_botao)
        self.botao_cadastrar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_cadastrar.clicked.connect(self.openSignUpPage)
        
        form_login_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_login_layout.addWidget(rotulo_login, 0, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(rotulo_email, 1, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.entrada_email, 2, 0)
        form_login_layout.addWidget(rotulo_senha, 3, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.entrada_senha, 4, 0)
        form_login_layout.addWidget(self.botao_logar, 5, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(rotulo_cadastrar, 6, 0, Qt.AlignmentFlag.AlignCenter)
        form_login_layout.addWidget(self.botao_cadastrar, 7, 0, Qt.AlignmentFlag.AlignCenter)

        fll_ajuste = QVBoxLayout()
        fll_ajuste.addWidget(form_login, 0, Qt.AlignmentFlag.AlignCenter)
        fll_ajuste.setContentsMargins(0, 0, 0, 50)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addLayout(fll_ajuste, 1, 0, 1, 0, Qt.AlignmentFlag.AlignTop)
    
    def openSignUpPage(self):
        TelaCadastro(self).show()
        self.hide()
    
    def openOptionsWindow(self, info_usuario):
        TelaOpcoes(self, info_usuario).show()
        self.hide()
    
    def signInVerification(self):
        inputtedEmail = self.entrada_email.text()
        userInfo = ControleUsuario.buscar(inputtedEmail.rstrip())
        if not userInfo:
            errorMessage = QMessageBox(self)
            self.entrada_email.setText("")
            errorMessage.setIcon(QMessageBox.Icon.Critical)
            errorMessage.setWindowTitle("Authentication Failed!")
            errorMessage.setStandardButtons(QMessageBox.StandardButton.Ok)
            errorMessage.setText(f"{userInfo.email} is not signed up. Please, sign up!")
            errorMessage.exec()
            return
        
        if userInfo.password != self.entrada_senha.text():
            errorMessage = QMessageBox(self)
            self.entrada_senha.setText("")
            errorMessage.setIcon(QMessageBox.Icon.Critical)
            errorMessage.setWindowTitle("Authentication Failed!")
            errorMessage.setStandardButtons(QMessageBox.StandardButton.Ok)
            errorMessage.setText(f"Your password is incorrect!")
            errorMessage.exec()
            return
        
        self.openOptionsWindow(userInfo.name)
    
    def centralizarTela(self) -> None: return
