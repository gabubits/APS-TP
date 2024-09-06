
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QStackedWidget
from .tela_base import *
from .tela_artistas import TelaArtistas
from .tela_albuns import TelaAlbuns
from .tela_cancoes import TelaCancoes
from .tela_perfil import TelaPerfil
from .tela_playlists import TelaPlaylists
from.tela_tocando import TelaTocando

from modelo.usuario import Usuario
from .tela_editar import TelaEditar

class TelaPrincipal(TelaBase):
    def __init__(self, parent: QWidget | None, op_padrao: int, controle: ControleContexto, usuario: Usuario) -> None:
        super().__init__(parent = parent,
                         titulo = "[Player]*",
                         tamanho = QSize(1500, 900))


        self.controle = controle
        self.usuario = usuario

        tela_largura = 1500
        tela_altura = 900

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.botao_fechar = QPushButton()
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_fechar = QPixmap(pathlib.Path("visao/imgs/close.png").resolve())
        icon_fechar = QIcon(img_fechar)
        self.botao_fechar.setIcon(icon_fechar)
        self.botao_fechar.setIconSize(QSize(25,25))
        self.botao_fechar.setMaximumSize(QSize(25,25))
        self.botao_fechar.clicked.connect(self.sair)

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
        botoes_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        botoes_layout.addWidget(self.botao_minimizar)
        botoes_layout.addWidget(self.botao_fechar)

        self.botao_perfil = QPushButton("Seu perfil")
        self.botao_cancoes = QPushButton("Canções")
        self.botao_albuns = QPushButton("Álbuns")
        self.botao_playlists = QPushButton("Playlists")
        self.botao_artistas = QPushButton("Artistas")

        self.fonte_botao.setPointSize(15)

        botoes = [self.botao_perfil, self.botao_cancoes, self.botao_albuns, \
                       self.botao_playlists, self.botao_artistas]

        barra_topo_layout = QGridLayout(barra_topo)

        for i, botao in enumerate(botoes, 0):
            botao.setFixedSize(185, 35)
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setFont(self.fonte_botao)
            botao.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")
            barra_topo_layout.addWidget(botao, 0, i, Qt.AlignmentFlag.AlignCenter)

        self.botao_adicionar_musica = QPushButton("+")
        self.botao_adicionar_musica.setFixedSize(100, 35)
        self.botao_adicionar_musica.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_adicionar_musica.setFont(self.fonte_botao)
        self.botao_adicionar_musica.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")
        self.botao_adicionar_musica.clicked.connect(self.adicionar_musica)

        barra_topo_layout.addWidget(self.botao_adicionar_musica, 0, len(botoes) + 1, Qt.AlignmentFlag.AlignRight)
        barra_topo_layout.addLayout(botoes_layout, 0, len(botoes) + 2, Qt.AlignmentFlag.AlignRight)

        self.pilha_paginas = QStackedWidget()
        self.pilha_paginas.setMinimumSize(3 * (tela_largura/4) - 50, tela_altura - 90)
        self.pilha_paginas.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        self.fonte_rotulo.setPointSize(25)

        pagina_tocando = TelaTocando(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "rotulo": self.fonte_rotulo},
             self.controle,
             tela_largura, tela_altura
        )

        pagina_perfil = TelaPerfil(
            self,
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             usuario,
             self.controle
        )

        self.pilha_paginas.addWidget(pagina_perfil)
        self.botao_perfil.clicked.connect(lambda: self.changePage(pagina_perfil))

        pagina_cancoes = TelaCancoes(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             usuario,
             self.controle,
             pagina_tocando.tocar_cancao
        )

        self.pilha_paginas.addWidget(pagina_cancoes)
        self.botao_cancoes.clicked.connect(lambda: self.changePage(pagina_cancoes))

        pagina_albuns = TelaAlbuns(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             usuario,
             self.controle,
             pagina_cancoes.pesquisar_cancao,
             self.pilha_paginas
        )

        self.pilha_paginas.addWidget(pagina_albuns)
        self.botao_albuns.clicked.connect(lambda: self.changePage(pagina_albuns))

        pagina_playlists = TelaPlaylists(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             usuario,
             self.controle,
             pagina_cancoes.exibir_playlist,
             self.pilha_paginas
        )

        self.pilha_paginas.addWidget(pagina_playlists)
        self.botao_playlists.clicked.connect(lambda: self.changePage(pagina_playlists))

        pagina_artistas = TelaArtistas(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             usuario,
             self.controle,
             pagina_albuns.pesquisar_album,
             self.pilha_paginas
        )

        self.pilha_paginas.addWidget(pagina_artistas)
        self.botao_artistas.clicked.connect(lambda: self.changePage(pagina_artistas))

        self.pilha_paginas.setCurrentIndex(op_padrao)

        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        self.widget_central_layout.addWidget(self.pilha_paginas, 1, 0)
        self.widget_central_layout.addWidget(pagina_tocando, 1, 1)

    def close(self) -> bool:
        sys.exit()

    def changePage(self, page: QWidget):
        if self.pilha_paginas.currentWidget == page: return
        self.pilha_paginas.setCurrentWidget(page)

    def sair(self):
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
        self.close()
        self.parentWidget().show()

    def adicionar_musica(self):
        audios_path, _ = QFileDialog.getOpenFileNames(self, "Importe suas músicas",
                                                  os.getcwd(), "*.mp3")

        TelaEditar(self, audios_path, self.controle, self.usuario).show()
