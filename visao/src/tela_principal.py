
from PySide6.QtWidgets import QStackedWidget
from .utils.tela_base import *
from .utils.entrada_pesquisa import *

class TelaPrincipal(TelaBase):
    def __init__(self, parent: QWidget | None, op_padrao: int = 0) -> None:
        super().__init__(parent = parent, 
                         titulo = "Streamy", 
                         tamanho = QSize(1500, 900))

        tela_largura = 1500
        tela_altura = 900
        self.historico_paginas: list[int] = []

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

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

        botao_voltar = QPushButton()
        botao_voltar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_voltar = QPixmap(pathlib.Path("visao/src/img/arrow-left-white.png").resolve())
        icon_voltar = QIcon(img_voltar)
        botao_voltar.setIcon(icon_voltar)
        botao_voltar.setIconSize(QSize(25,25))
        botao_voltar.setMaximumSize(QSize(25,25))
        botao_voltar.clicked.connect(self.rm_historico)

        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(5)
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        botoes_layout.addWidget(botao_minimizar)
        botoes_layout.addWidget(botao_fechar)

        botao_usuarios = QPushButton("Users")
        botao_cancoes = QPushButton("Songs")
        botao_albuns = QPushButton("Albums")
        botao_playlists = QPushButton("Playlists")
        botao_artistas = QPushButton("Artists")

        self.fonte_botao.setPointSize(15)

        botoes = [botao_usuarios, botao_cancoes, botao_albuns, \
                       botao_playlists, botao_artistas]

        barra_topo_layout = QGridLayout(barra_topo)

        barra_topo_layout.addWidget(botao_voltar, 0, 0, Qt.AlignmentFlag.AlignLeft)
        for i, botao in enumerate(botoes, 1):
            botao.setFixedSize(185, 35)
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setFont(self.fonte_botao)
            botao.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")
            barra_topo_layout.addWidget(botao, 0, i, Qt.AlignmentFlag.AlignCenter)
        
        botao_ver_perfil = QPushButton()
        botao_ver_perfil.setCursor(Qt.CursorShape.PointingHandCursor)
        img_perfil = QPixmap(pathlib.Path("visao/src/img/teste.jpg").resolve())
        icon_perfil = QIcon(img_perfil)
        botao_ver_perfil.setIcon(icon_perfil)
        botao_ver_perfil.setIconSize(QSize(25,25))
        #botao_ver_perfil.clicked.connect(self.showMinimized)

        barra_topo_layout.addWidget(botao_ver_perfil, 0, len(botoes) + 1, Qt.AlignmentFlag.AlignCenter)
        barra_topo_layout.addLayout(botoes_layout, 0, len(botoes) + 2, Qt.AlignmentFlag.AlignRight)

        self.pilha_paginas = QStackedWidget()
        self.pilha_paginas.setMinimumSize(3 * (tela_largura/4) - 50, tela_altura - 90)
        self.pilha_paginas.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        self.fonte_rotulo.setPointSize(25)

        pagina_usuarios = QWidget()
        pu_layout = QGridLayout(pagina_usuarios)

        pu_pesquisa = CaixaPesquisa()
        pu_pesquisa.setFixedSize(380, 30)
        pu_pesquisa.setStyleSheet("border-radius: 5px; background-color: rgb(18, 18, 18); border: 1px solid grey")
        pu_pesquisa.setAlignment(Qt.AlignmentFlag.AlignLeft)
        pu_pesquisa.setFont(self.fonte_entrada)
        
        pu_botao_remover = QPushButton("Remover usuario")
        pu_botao_remover.setFixedSize(170, 50)
        pu_botao_remover.setStyleSheet("background-color: red; border-radius: 25px; color: white")
        pu_botao_remover.setCursor(Qt.CursorShape.PointingHandCursor)
        pu_botao_remover.setFont(self.fonte_botao)

        pu_botao_adm = QPushButton("Promover a ADM")
        pu_botao_adm.setFixedSize(170, 50)
        pu_botao_adm.setStyleSheet("background-color: blue; border-radius: 25px; color: white")
        pu_botao_adm.setCursor(Qt.CursorShape.PointingHandCursor)
        pu_botao_adm.setFont(self.fonte_botao)

        pu_botoes_layout = QGridLayout()
        pu_botoes_layout.addWidget(pu_botao_remover, 0, 0, Qt.AlignmentFlag.AlignCenter)
        pu_botoes_layout.addWidget(pu_botao_adm, 0, 1, Qt.AlignmentFlag.AlignCenter)

        pu_layout.addWidget(pu_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        pu_layout.addLayout(pu_botoes_layout, 1, 0, Qt.AlignmentFlag.AlignBottom)
        self.pilha_paginas.addWidget(pagina_usuarios)
        botao_usuarios.clicked.connect(lambda: self.changePage(0))

        pagina_cancoes = QWidget()
        pc_layout = QGridLayout(pagina_cancoes)
        rotulo_cancoes = QLabel("Songs list")
        rotulo_cancoes.setFont(self.fonte_rotulo)
        pc_layout.addWidget(rotulo_cancoes, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.pilha_paginas.addWidget(pagina_cancoes)
        botao_cancoes.clicked.connect(lambda: self.changePage(1))

        pagina_albuns = QWidget()
        pal_layout = QGridLayout(pagina_albuns)
        rotulo_albuns = QLabel("Albums list")
        rotulo_albuns.setFont(self.fonte_rotulo)
        pal_layout.addWidget(rotulo_albuns, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.pilha_paginas.addWidget(pagina_albuns)
        botao_albuns.clicked.connect(lambda: self.changePage(2))

        pagina_playlists = QWidget()
        pp_layout = QGridLayout(pagina_playlists)
        rotulo_playlists = QLabel("Playlists list")
        rotulo_playlists.setFont(self.fonte_rotulo)
        pp_layout.addWidget(rotulo_playlists, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.pilha_paginas.addWidget(pagina_playlists)
        botao_playlists.clicked.connect(lambda: self.changePage(3))

        pagina_artistas = QWidget()
        par_layout = QGridLayout(pagina_artistas)
        rotulo_artistas = QLabel("Artists list")
        rotulo_artistas.setFont(self.fonte_rotulo)
        par_layout.addWidget(rotulo_artistas, 0, 0, Qt.AlignmentFlag.AlignCenter)
        self.pilha_paginas.addWidget(pagina_artistas)
        botao_artistas.clicked.connect(lambda: self.changePage(4))

        self.pilha_paginas.setCurrentIndex(0)
        
        pagina_tocando = QWidget()
        pagina_tocando.setMinimumSize(tela_largura/4, tela_altura - 90)
        pagina_tocando.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        pagina_tocando_layout = QGridLayout(pagina_tocando)

        nowPlayingLabel = QLabel("Now Playing Screen")
        nowPlayingLabel.setWordWrap(True)
        nowPlayingLabel.setFont(self.fonte_rotulo)

        pagina_tocando_layout.addWidget(nowPlayingLabel, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        self.widget_central_layout.addWidget(self.pilha_paginas, 1, 0)
        self.widget_central_layout.addWidget(pagina_tocando, 1, 1)
    
    def close(self) -> bool:
        sys.exit()

    def adc_historico(self):
        self.historico_paginas.append(self.pilha_paginas.currentIndex())
        return
    
    def rm_historico(self):
        if len(self.historico_paginas) == 0: return
        else:
            self.pilha_paginas.setCurrentIndex(self.historico_paginas.pop())
    
    def changePage(self, index: int):
        if self.pilha_paginas.currentIndex() == index: return
        self.adc_historico()
        self.pilha_paginas.setCurrentIndex(index)