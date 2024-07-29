
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QStackedWidget
import eyed3.mp3
from .utils.tela_base import *
from .stack_telas.tela_artistas import TelaArtistas
from .stack_telas.tela_albuns import TelaAlbuns
from .stack_telas.tela_cancoes import TelaCancoes
from .stack_telas.tela_perfil import TelaPerfil

from controle.controle import Controle
from modelo.usuario import Usuario
from .tela_editar import TelaEditar
class TelaPrincipal(TelaBase):
    def __init__(self, parent: QWidget | None, op_padrao: int, controle: Controle, id_usuario: int) -> None:
        super().__init__(parent = parent, 
                         titulo = "[Player]*", 
                         tamanho = QSize(1500, 900))


        self.controle = controle
        self.id_usuario = id_usuario

        tela_largura = 1500
        tela_altura = 900

        barra_topo = QFrame()
        barra_topo.setMinimumSize(tela_largura - 15, 40)
        barra_topo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        barra_topo.setStyleSheet("background-color: rgb(21, 21, 21); border-radius: 20px;")

        self.botao_fechar = QPushButton()
        self.botao_fechar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_fechar = QPixmap(pathlib.Path("visao/src/img/close.png").resolve())
        icon_fechar = QIcon(img_fechar)
        self.botao_fechar.setIcon(icon_fechar)
        self.botao_fechar.setIconSize(QSize(25,25))
        self.botao_fechar.setMaximumSize(QSize(25,25))
        self.botao_fechar.clicked.connect(self.sair)

        self.botao_minimizar = QPushButton()
        self.botao_minimizar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_minimizar = QPixmap(pathlib.Path("visao/src/img/minimize.png").resolve())
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

        pagina_perfil = TelaPerfil(
            self,
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             id_usuario,
             self.controle
        )

        self.pilha_paginas.addWidget(pagina_perfil)
        self.botao_perfil.clicked.connect(lambda: self.changePage(pagina_perfil))

        pagina_cancoes = TelaCancoes(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             id_usuario,
             self.controle
        )

        self.pilha_paginas.addWidget(pagina_cancoes)
        self.botao_cancoes.clicked.connect(lambda: self.changePage(pagina_cancoes))

        pagina_albuns = TelaAlbuns(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             id_usuario,
             self.controle
        )

        self.pilha_paginas.addWidget(pagina_albuns)
        self.botao_albuns.clicked.connect(lambda: self.changePage(pagina_albuns))

        pagina_playlists = QWidget()
        pp_layout = QGridLayout(pagina_playlists)
        rotulo_playlists = QLabel("Playlists")
        rotulo_playlists.setFont(self.fonte_rotulo)
        pp_layout.addWidget(rotulo_playlists, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.pilha_paginas.addWidget(pagina_playlists)
        self.botao_playlists.clicked.connect(lambda: self.changePage(pagina_playlists))

        pagina_artistas = TelaArtistas(
            {"entrada": self.fonte_entrada,
             "botao": self.fonte_botao,
             "lista": QFont(self.fonte_principal, 20, QFont.Weight.Normal)},
             id_usuario,
             self.controle
        )

        self.pilha_paginas.addWidget(pagina_artistas)
        self.botao_artistas.clicked.connect(lambda: self.changePage(pagina_artistas))

        self.pilha_paginas.setCurrentIndex(op_padrao)
        
        pagina_tocando = QWidget()
        pagina_tocando.setMinimumSize(tela_largura/4, tela_altura - 90)
        pagina_tocando.setStyleSheet("background-color: rgb(21,21,21); border-radius: 10px")

        pagina_tocando_layout = QGridLayout(pagina_tocando)

        nowPlayingLabel = QLabel("Tocando agora (tela)")
        nowPlayingLabel.setWordWrap(True)
        nowPlayingLabel.setFont(self.fonte_rotulo)

        pagina_tocando_layout.addWidget(nowPlayingLabel, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.widget_central_layout.addWidget(barra_topo, 0, 0, Qt.AlignmentFlag.AlignHCenter)
        self.widget_central_layout.addWidget(self.pilha_paginas, 1, 0)
        self.widget_central_layout.addWidget(pagina_tocando, 1, 1)
    
    def close(self) -> bool:
        sys.exit()
    
    def changePage(self, page: QWidget):
        if self.pilha_paginas.currentWidget == page: return
        self.pilha_paginas.setCurrentWidget(page)
        
    ''' Funções não utilizadas no momento
    def pesquisar_usuario(self, texto: str, list_widget: QListWidget):
        list_widget.clear()
        if len(texto.rstrip()) == 0:
            resultado = self.controle.getUsuarios()
        else:
            resultado = self.controle.buscar_nome(texto)
            if not resultado:
                resultado = self.controle.buscar_email(texto)
        
        list_widget.addItems([f'{usuario.nome} <{usuario.email}>' for usuario in resultado])
        self.resultados_pesquisa = resultado

    def promover_adm(self, list_widget: QListWidget):
        indices = [indice.row() for indice in list_widget.selectionModel().selectedIndexes()]
        for indice in indices:
            if self.resultados_pesquisa[indice].email == self.info_usuario.email: pass
            else:
                self.controle.alterar_adm(self.resultados_pesquisa[indice])

    def remover_usuarios(self, list_widget: QListWidget):
        indices = [indice.row() for indice in list_widget.selectionModel().selectedIndexes()]
        for indice in indices:
            if self.resultados_pesquisa[indice].email == self.info_usuario.email: pass
            else:
                self.controle.excluir(self.resultados_pesquisa[indice])
                item = list_widget.takeItem(indice)
                del item
    '''
    def sair(self):
        self.controle.atualizar_arquivo()
        self.close()
        self.parentWidget().show()
    
    def adicionar_musica(self):
        audios_path, _ = QFileDialog.getOpenFileNames(self, "Importe suas músicas", 
                                                  os.getcwd(), "*.mp3")
        
        TelaEditar(self, audios_path, self.controle, self.id_usuario).show()
        
