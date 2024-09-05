from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QDialog, QLabel, QLineEdit, QComboBox, QWidget, QHBoxLayout

class Cancao:
    def __init__(self, titulo, artista, album, genero, duracao):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.duracao = duracao

class AddCancaoDialog(QDialog):
    def __init__(self, artistas_existentes):
        super().__init__()
        self.setWindowTitle("Adicionar Canção")
        layout = QVBoxLayout()

        # Campo para o título da canção
        self.titulo_label = QLabel("Digite o título da canção:")
        self.titulo_input = QLineEdit()
        layout.addWidget(self.titulo_label)
        layout.addWidget(self.titulo_input)

        # ComboBox para o artista
        self.artista_label = QLabel("Selecione o artista da canção:")
        self.artista_combo = QComboBox()
        self.artista_combo.addItems(artistas_existentes + ["Adicionar artista"])
        self.artista_combo.currentIndexChanged.connect(self.carregar_albuns)
        layout.addWidget(self.artista_label)
        layout.addWidget(self.artista_combo)

        # ComboBox para o álbum (inicialmente desativado)
        self.album_label = QLabel("Selecione o álbum da canção:")
        self.album_combo = QComboBox()
        self.album_combo.setEnabled(False)  # Desativa até o artista ser selecionado
        layout.addWidget(self.album_label)
        layout.addWidget(self.album_combo)

        # Campo para o gênero
        self.genero_label = QLabel("Digite o gênero da canção:")
        self.genero_input = QLineEdit()
        layout.addWidget(self.genero_label)
        layout.addWidget(self.genero_input)

        # Campo para a duração
        self.duracao_label = QLabel("Digite a duração da canção (min:seg):")
        self.duracao_input = QLineEdit()
        layout.addWidget(self.duracao_label)
        layout.addWidget(self.duracao_input)

        # Botão de salvar
        self.save_button = QPushButton("Salvar Canção")
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def carregar_albuns(self):
        artista_selecionado = self.artista_combo.currentText()
        if artista_selecionado == "Adicionar artista":
            # Lógica para adicionar um novo artista
            pass
        else:
            # Suponha que aqui você consulta os álbuns desse artista
            albuns_do_artista = ["Álbum 1", "Álbum 2"]  # Exemplo de álbuns do artista
            self.album_combo.clear()
            self.album_combo.addItems(albuns_do_artista + ["Adicionar álbum"])
            self.album_combo.setEnabled(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Biblioteca de Canções")
        self.setGeometry(200, 200, 400, 200)

        self.artistas_existentes = ["Artista 1", "Artista 2"]

        # Layout principal
        layout = QVBoxLayout()

        # Botão para adicionar canção
        self.add_cancao_button = QPushButton("Adicionar Canção")
        self.add_cancao_button.clicked.connect(self.abrir_add_cancao_dialog)
        layout.addWidget(self.add_cancao_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_add_cancao_dialog(self):
        dialog = AddCancaoDialog(self.artistas_existentes)
        dialog.exec()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
