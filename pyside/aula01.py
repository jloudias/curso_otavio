# Conferir a instalação e versão atual
# import PySide6.QtCore
# print(PySide6.__version__)
# print(PySide6.QtCore.__version__)

import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QMainWindow,
    QHBoxLayout,
    QGridLayout,
)

# Criação da janela
app = QApplication(sys.argv)  # aplicação
window = QMainWindow()  # janela
central_widget = QWidget()  # central de widgets
layout = QGridLayout()  # layout
window.setCentralWidget(central_widget)  # atribui central a janela
central_widget.setLayout(layout)  # atribui layout a central de widgets

# Configuração da janela
window.setWindowTitle("PySide6 - My First App ")
window.setGeometry(10, 50, 400, 200)  # (x,y,width,height)

# Widgets
botao1 = QPushButton(text="Posição (1,1)")
botao1.setFixedSize(200, 60)
botao1.setToolTip("Clique para ver a mensagem.")

botao2 = QPushButton(text="Posição (2,2)")
botao2.setFixedSize(200, 60)

botao3 = QPushButton(text="Posição (3,1,1,2)")
botao3.setStyleSheet("font-size: 18px;")

# Adicionando widgets ao layout
layout.addWidget(botao1, 1, 1)
layout.addWidget(botao2, 2, 2)
layout.addWidget(botao3, 3, 1, 1, 2)  # colspan

# Exibe a janela e faz o loop
window.show()
app.exec()
