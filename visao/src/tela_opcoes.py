from .utils.tela_base import *
from .tela_principal import TelaPrincipal
from controle.usuario_controle import UsuarioControle
from modelo.usuario import Usuario

class TelaOpcoes(TelaBase):
    def __init__(self, parent: QWidget | None, info_usuario: Usuario, usuario_controle: UsuarioControle) -> None:
        super().__init__(parent = parent, 
                         titulo = 'Streamy', 
                         tamanho = QSize(1500, 900))

        self.info_usuario = info_usuario
        self.usuario_controle = usuario_controle

        barra_topo = QFrame()
        barra_topo.setMinimumSize(600, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        rotulo_boas_vindas = QLabel(f"Hey {self.info_usuario.nome}!")
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
        botao_fechar.clicked.connect(self.close)

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
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        botoes_layout.addWidget(botao_minimizar)
        botoes_layout.addWidget(botao_fechar)

        botao_ver_perfil = QPushButton()
        botao_ver_perfil.setCursor(Qt.CursorShape.PointingHandCursor)
        img_perfil = QPixmap(pathlib.Path(self.info_usuario.img_perfil).resolve())
        icon_perfil = QIcon(img_perfil)
        botao_ver_perfil.setIcon(icon_perfil)
        botao_ver_perfil.setIconSize(QSize(35, 35))
        #botao_ver_perfil.clicked.connect(self.showMinimized)

        barra_topo_layout = QGridLayout(barra_topo)
        barra_topo_layout.addWidget(rotulo_boas_vindas, 0, 0, Qt.AlignmentFlag.AlignLeft)
        barra_topo_layout.addWidget(botao_ver_perfil, 0, 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, 2, Qt.AlignmentFlag.AlignRight)
        
        menu_opcoes = QWidget()
        menu_opcoes.setFixedSize(500, 500)
        menu_opcoes.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        menu_opcoes.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 15px;")
        self.setContentsMargins(0, 0, 0, 80)

        botao_usuarios = QPushButton("Ver Users")
        botao_cancoes = QPushButton("Ver Songs")
        botao_albuns = QPushButton("Ver Albums")
        botao_playlists = QPushButton("Ver Playlists")
        botao_artistas = QPushButton("Ver Artists")

        self.fonte_botao.setPointSize(20)

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, \
                       botao_playlists, botao_artistas]

        menu_ops_layout = QGridLayout(menu_opcoes)
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
        self.widget_central_layout.addWidget(menu_opcoes, 1, 0, Qt.AlignmentFlag.AlignCenter)
        self.widget_central_layout.addWidget(botao_sair, 2, 0, Qt.AlignmentFlag.AlignCenter)

    def close(self) -> bool:
        sys.exit()
    
    def abrir_tela(self, indice_pagina: int):
        TelaPrincipal(parent = self.parentWidget(), 
                      op_padrao=indice_pagina,
                      usuario_controle=self.usuario_controle,
                      info_usuario=self.info_usuario).show()
        self.hide()
    
    def abrir_tela_login(self):
        self.parentWidget().show()
        self.hide()