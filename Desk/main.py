from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Definir o ícone da janela
        icon = QIcon(QPixmap('Logo/WhatsApp Image 2024-08-16 at 8.00.15 PM (2).jpeg'))
        self.setWindowIcon(icon)
        self.setWindowTitle("Stockeeper")
        self.setGeometry(200, 100, 1600, 800)  # posição x e y, largura e altura

        # Criar e definir o layout
        layout = QVBoxLayout()
        label = QLabel("Bem-vindo ao Stockeeper!")
        layout.addWidget(label)
        layout.addWidget(QPushButton("Clique aqui!"))


        self.setLayout(layout)

    def tela(self):
        self.setQWindowTittle("Estoques")
        self.setGeometry(200, 100, 1600, 800)


def apply_stylesheet(app):
    with open('Desk/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)  # Aplica o estilo
    window = MyWindow()
    window.show()
    app.exec_()
