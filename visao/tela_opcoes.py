from .tela_base import *
from .tela_principal import TelaPrincipal
from modelo.usuario import Usuario
from controle.usuario_controle import UsuarioControle

class TelaOpcoes(TelaBase):
    def __init__(self, parent: QWidget | None, usuario: Usuario, controle: ControleContexto) -> None:
        super().__init__(parent = parent, 
                         titulo = '[Player]* - Opções', 
                         tamanho = QSize(1500, 900))

        self.controle = controle
        self.usuario = usuario

        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.controle.tipo_controle = UsuarioControle()
        self.rotulo_boas_vindas = QLabel(f"Hey {self.usuario.nome}!")
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
        self.botao_fechar.clicked.connect(self.close)

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
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        botoes_layout.addWidget(self.botao_minimizar)
        botoes_layout.addWidget(self.botao_fechar)

        self.botao_ver_perfil = QPushButton()
        self.botao_ver_perfil.setCursor(Qt.CursorShape.PointingHandCursor)
        img_perfil = QPixmap(pathlib.Path(usuario.img_perfil).resolve())
        icon_perfil = QIcon(img_perfil)
        self.botao_ver_perfil.setIcon(icon_perfil)
        self.botao_ver_perfil.setIconSize(QSize(35, 35))
        #self.botao_ver_perfil.clicked.connect(self.showMinimized)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(self.rotulo_boas_vindas, 0, 0, Qt.AlignmentFlag.AlignLeft)
        barra_topo_layout.addWidget(self.botao_ver_perfil, 0, 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, 2, Qt.AlignmentFlag.AlignRight)
        
        self.menu_opcoes = QWidget()
        self.menu_opcoes.setFixedSize(500, 500)
        self.menu_opcoes.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.menu_opcoes.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")
        self.setContentsMargins(0, 0, 0, 80)

        botao_usuarios = QPushButton("Seu perfil")
        botao_cancoes = QPushButton("Canções")
        botao_albuns = QPushButton("Álbuns")
        botao_playlists = QPushButton("Playlists")
        botao_artistas = QPushButton("Artistas")

        self.fonte_botao.setPointSize(20)

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, \
                       botao_playlists, botao_artistas]

        menu_ops_layout = QGridLayout(self.menu_opcoes)
        for i, botao in enumerate(botoes):
            botao.setFixedSize(400, 80)
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setFont(self.fonte_botao)
            botao.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 25px;")
            menu_ops_layout.addWidget(botao, i, 0, Qt.AlignmentFlag.AlignCenter)
        
        botao_usuarios.clicked.connect(lambda: self.abrir_tela(0))
        botao_cancoes.clicked.connect(lambda: self.abrir_tela(1))
        botao_albuns.clicked.connect(lambda: self.abrir_tela(2))
        botao_playlists.clicked.connect(lambda: self.abrir_tela(3))
        botao_artistas.clicked.connect(lambda: self.abrir_tela(4))

        botao_sair = QPushButton("Sair")
        botao_sair.setFixedSize(150, 50)
        botao_sair.setStyleSheet("background-color: white; border-radius: 25px; color: black")
        botao_sair.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_sair.setFont(self.fonte_botao)
        botao_sair.clicked.connect(self.abrir_tela_login)

        self.fonte_botao.setPointSize(15)

        botao_sair.setFont(self.fonte_botao)

        self.widget_central_layout.setSpacing(0)
        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignTop)
        self.widget_central_layout.addWidget(self.menu_opcoes, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.widget_central_layout.addWidget(botao_sair, 2, 0, Qt.AlignmentFlag.AlignCenter)

    def close(self) -> bool:
        sys.exit()
    
    def abrir_tela(self, indice_pagina: int):
        TelaPrincipal(parent = self, 
                      op_padrao=indice_pagina,
                      controle=self.controle,
                      usuario=self.usuario).show()
        self.hide()
    
    def abrir_tela_login(self):
        self.parentWidget().show()
        self.hide()