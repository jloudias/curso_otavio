import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QMainWindow,
    QGridLayout,
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        central = QWidget()  # central de widgets
        layout = QGridLayout()  # layout
        self.setCentralWidget(central)  # atribui central a janela
        central.setLayout(layout)  # atribui layout a central de widgets

        # Configuração da janela
        self.setWindowTitle("PySide6 - My First App ")
        self.setGeometry(10, 50, 400, 200)  # (x,y,width,height)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Sou a barra de status da janela")

        # Menu
        menu = self.menuBar()
        menu_file = menu.addMenu("Arquivo")
        menu_file_new = menu_file.addAction("Novo")
        menu_file_new.triggered.connect(self.new_file)
        menu_file_open = menu_file.addAction("Abrir")
        menu_file_save = menu_file.addAction("Salvar")
        menu_file_saveas = menu_file.addAction("Salvar Como")
        self.botao1 = self.make_button("Botão 1", "Posição (1,1)")
        self.botao2 = self.make_button("Botão 3", "Posição (2,2)")
        self.botao3 = self.make_button("Botão 3 - Colspan", "Posição (3,1,1,2)")

        # Adicionando widgets ao layout
        layout.addWidget(self.botao1, 1, 1, 1, 1)
        layout.addWidget(self.botao2, 2, 2, 1, 1)
        layout.addWidget(self.botao3, 3, 1, 1, 2)  # colspan

    def make_button(self, text, tooltip="Hot tip.."):
        button = QPushButton(self, text=text)
        button.setFixedHeight(60)
        button.setToolTip(tooltip)
        return button

    def new_file(self):
        self.status_bar.showMessage("Você clicou em Arquivo>Novo.")


if __name__ == "__main__":

    # Exibe a janela e faz o loop

    app = QApplication(sys.argv)  # aplicação
    window = MyWindow()
    window.show()
    app.exec()
