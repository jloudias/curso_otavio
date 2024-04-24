import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QMainWindow,
    QGridLayout,
)


def new_file():
    status_bar.showMessage("Você clicou em Arquivo>Novo.")


# Criação da janela
app = QApplication(sys.argv)  # aplicação
window = QMainWindow()  # janela
central = QWidget()  # central de widgets
layout = QGridLayout()  # layout
window.setCentralWidget(central)  # atribui central a janela
central.setLayout(layout)  # atribui layout a central de widgets

# Configuração da janela
window.setWindowTitle("PySide6 - My First App ")
window.setGeometry(10, 50, 400, 200)  # (x,y,width,height)

# QWindow permite adicionar barra de status, menu e outros elementos de uma janela.
#
# Barra de status
status_bar = window.statusBar()
status_bar.showMessage("Sou a barra de status da janela")

# Menu
menu = window.menuBar()
menu_file = menu.addMenu("Arquivo")
menu_file_new = menu_file.addAction("Novo")
menu_file_new.triggered.connect(new_file)
menu_file_open = menu_file.addAction("Abrir")
menu_file_save = menu_file.addAction("Salvar")
menu_file_saveas = menu_file.addAction("Salvar Como")


# Widgets
botao1 = QPushButton(text="Posição (1,1)")
botao1.setFixedSize(200, 60)
botao1.setToolTip("Clique para ver a mensagem.")

botao2 = QPushButton(text="Posição (2,2)")
botao2.setFixedSize(200, 60)

botao3 = QPushButton(text="Posição (3,1,1,2)")
botao3.setStyleSheet("font-size: 18px;height: 40px")

# Adicionando widgets ao layout
layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 2, 2)
layout.addWidget(botao3, 3, 1, 1, 2)  # colspan

# Exibe a janela e faz o loop
window.show()
app.exec()
