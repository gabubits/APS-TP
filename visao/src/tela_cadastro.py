from PySide6.QtGui import QCloseEvent
from .utils.tela_base import *

from .tela_opcoes import TelaOpcoes
from controle.usuario_controle import UsuarioControle
from modelo.usuario import Usuario

class TelaCadastro(TelaBase):
    def __init__(self, parent: QWidget | None, usuario_controle: UsuarioControle) -> None:
        super().__init__(parent = parent,
                         titulo = "Streamy",
                         tamanho = QSize(600, 750))
        
        self.usuario_controle = usuario_controle

        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        rotulo_boas_vindas = QLabel("Olá novo Streamy!")
        fonte_bv = QFont(self.fonte_principal, 20)
        fonte_bv.setWeight(QFont.Weight.DemiBold)
        rotulo_boas_vindas.setFont(fonte_bv)

        botao_fechar = QPushButton()
        botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_fechar = QPixmap(pathlib.Path("visao/src/img/close.png").resolve())
        icon_fechar = QIcon(img_fechar)
        botao_fechar.setIcon(icon_fechar)
        botao_fechar.setIconSize(QSize(25,25))
        botao_fechar.setMaximumSize(QSize(25,25))
        botao_fechar.clicked.connect(sys.exit)

        botao_minimizar = QPushButton()
        botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_minimizar = QPixmap(pathlib.Path("visao/src/img/minimize.png").resolve())
        icon_minimizar = QIcon(img_minimizar)
        botao_minimizar.setIcon(icon_minimizar)
        botao_minimizar.setIconSize(QSize(25,25))
        botao_minimizar.setMaximumSize(QSize(25,25))
        botao_minimizar.clicked.connect(self.showMinimized)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        botoes_layout.addWidget(botao_minimizar)
        botoes_layout.addWidget(botao_fechar)

        botao_voltar = QPushButton()
        botao_voltar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_voltar = QPixmap(pathlib.Path("visao/src/img/arrow-left-white.png").resolve())
        icon_voltar = QIcon(img_voltar)
        botao_voltar.setIcon(icon_voltar)
        botao_voltar.setIconSize(QSize(25,25))
        botao_voltar.setMaximumSize(QSize(25,25))
        botao_voltar.clicked.connect(self.fechar_e_voltar)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(botao_voltar, 0, 0)
        barra_topo_layout.addWidget(rotulo_boas_vindas, 0, 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, 2)

        form_cadastro = QFrame()
        form_cadastro.setMinimumSize(400, 600)
        form_cadastro.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        form_cadastro.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")

        form_cadastro_layout = QGridLayout(form_cadastro)

        rotulo_inicial = QLabel("Cadastro")
        rotulo_inicial.setWordWrap(True)
        fonte_mi = QFont(self.fonte_principal, 20)
        fonte_mi.setWeight(QFont.Weight.DemiBold)
        rotulo_inicial.setFont(fonte_mi)
        rotulo_inicial.setContentsMargins(0, 15, 0, 20)

        estilo_caixa_entrada = "border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey"
        estilo_botao = "background-color: white; border-radius: 25px; color: black"

        rotulo_nome = QLabel("Nome *")
        rotulo_nome.setFont(self.fonte_rotulo)
        rotulo_nome.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        
        self.entrada_nome = QLineEdit()
        self.entrada_nome.setObjectName("Nome")
        self.entrada_nome.setFont(self.fonte_entrada)
        self.entrada_nome.setFixedSize(380, 30)
        self.entrada_nome.setStyleSheet(estilo_caixa_entrada)
        self.entrada_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_email = QLabel("Endereço de e-mail *")
        rotulo_email.setFont(self.fonte_rotulo)
        rotulo_email.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        rotulo_email.setContentsMargins(0, 20, 0, 0)

        self.entrada_email = QLineEdit()
        self.entrada_email.setObjectName("Endereço de e-mail")
        self.entrada_email.setFixedSize(380, 30)
        self.entrada_email.setFont(self.fonte_entrada)
        self.entrada_email.setStyleSheet(estilo_caixa_entrada)
        self.entrada_email.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_senha = QLabel("Senha *")
        rotulo_senha.setFont(self.fonte_rotulo)
        rotulo_senha.setContentsMargins(0, 20, 0, 0)
        rotulo_senha.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.entrada_senha = QLineEdit()
        self.entrada_senha.setObjectName("Senha")
        self.entrada_senha.setFixedSize(380, 30)
        self.entrada_senha.setFont(self.fonte_entrada)
        self.entrada_senha.setStyleSheet(estilo_caixa_entrada)
        self.entrada_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.entrada_senha.setAlignment(Qt.AlignmentFlag.AlignCenter)

        rotulo_foto = QLabel("Foto de perfil")
        rotulo_foto.setFont(self.fonte_rotulo)
        rotulo_foto.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        rotulo_foto.setContentsMargins(0, 20, 0, 0)
    
        self.entrada_foto = QLineEdit()
        self.entrada_foto.setFixedSize(380, 30)
        self.entrada_foto.setFont(self.fonte_entrada)
        self.entrada_foto.setPlaceholderText("Caminho da imagem (.jpg ou .png)")
        self.entrada_foto.setStyleSheet(estilo_caixa_entrada)
        self.entrada_foto.setAlignment(Qt.AlignmentFlag.AlignCenter)

        botao_enviar_foto = QPushButton("Envie sua foto (.jpg, .png)")
        botao_enviar_foto.setStyleSheet(estilo_botao)
        botao_enviar_foto.setFont(self.fonte_botao)
        botao_enviar_foto.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_enviar_foto.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        botao_enviar_foto.setStyleSheet("border-radius: 5px; background-color: white; color: black;")
        botao_enviar_foto.clicked.connect(self.enviar_img)

        rotulo_bio = QLabel("Sua Biografia")
        rotulo_bio.setFont(self.fonte_rotulo)
        rotulo_bio.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        rotulo_bio.setContentsMargins(0, 20, 0, 0)

        self.entrada_bio = QTextEdit()
        self.entrada_bio.setFixedSize(380, 100)
        self.entrada_bio.setFont(self.fonte_entrada)
        self.entrada_bio.setStyleSheet(estilo_caixa_entrada)
        self.entrada_bio.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.botao_cadastrar = QPushButton("Cadastrar-se")
        self.botao_cadastrar.setFixedSize(125, 50)
        self.botao_cadastrar.setStyleSheet(estilo_botao)
        self.botao_cadastrar.setFont(self.fonte_botao)
        self.botao_cadastrar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_cadastrar.clicked.connect(self.verificar_informacoes)

        form_cadastro_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        form_cadastro_layout.addWidget(rotulo_inicial, 0, 0, Qt.AlignmentFlag.AlignCenter)
        form_cadastro_layout.addWidget(rotulo_nome, 1, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_nome, 2, 0)
        form_cadastro_layout.addWidget(rotulo_email, 3, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_email, 4, 0)
        form_cadastro_layout.addWidget(rotulo_senha, 5, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_senha, 6, 0)
        form_cadastro_layout.addWidget(rotulo_foto, 7, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_foto, 8, 0)
        form_cadastro_layout.addWidget(botao_enviar_foto, 9, 0)
        form_cadastro_layout.addWidget(rotulo_bio, 10, 0, Qt.AlignmentFlag.AlignHCenter)
        form_cadastro_layout.addWidget(self.entrada_bio, 11, 0)
        form_cadastro_layout.addWidget(self.botao_cadastrar, 12, 0, Qt.AlignmentFlag.AlignCenter)

        fcl_ajuste = QVBoxLayout()
        fcl_ajuste.addWidget(form_cadastro, 0, Qt.AlignmentFlag.AlignCenter)
        fcl_ajuste.setContentsMargins(0, 0, 0, 50)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addLayout(fcl_ajuste, 1, 0, 1, 0, Qt.AlignmentFlag.AlignTop)
    
    def fechar_e_voltar(self):
        self.hide()
        self.parentWidget().show()

    def enviar_img(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "Selecione sua imagem de perfil", 
                                                  os.getcwd(), "Image Files (*.png *.jpg *.jpeg)")
        self.entrada_foto.setText(img_path)
    
    def abrir_tela_opcoes(self):
        TelaOpcoes(self.parentWidget()).show()
        self.hide()
    
    def verificar_informacoes(self):
        mandatoryInputs = [self.entrada_nome, self.entrada_email, self.entrada_senha]
        optionalInputs = [self.entrada_bio, self.entrada_foto]

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
        
        if self.usuario_controle.buscar_email(self.entrada_email.text()):
            MessageBox(
                self,
                'Falha na autenticação!',
                QMessageBox.Icon.Warning,
                f'{self.entrada_email.text()}'
                'já está registrado.'
                'Por favor, escolha outro e-mail.'
            ).exec()
            return
        
        novo_usuario = Usuario(
            self.entrada_nome.text(),
            self.entrada_email.text(),
            self.entrada_senha.text(),
            self.entrada_bio.toPlainText()
        )

        if len(self.entrada_foto.text()) != 0:
            novo_usuario.img_perfil = self.entrada_foto.text()
            
        self.usuario_controle.inserir(novo_usuario)

        MessageBox(self,
                   f'Bem-vindo {self.entrada_nome.text()}',
                   QMessageBox.Icon.Information,
                   'Sua conta foi criada com sucesso.',
                   'Você pode fazer o login agora.').exec()

        self.fechar_e_voltar()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.usuario_controle.atualizar_arquivo()
    
    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_Return:
            self.verificar_informacoes()