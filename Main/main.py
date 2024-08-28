from PyQt6.QtWidgets import QApplication
from views import MyWindow
from controllers import Controller

def apply_stylesheet(app):
    with open('Main/styles/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)

    # Inicializa o controlador e a visão
    controller = Controller()  # Inicializa o controlador
    view = MyWindow(controller)  # Passa o controlador para a visão
    controller.window = view  # Conecta o controlador à visão

    view.show()
    app.exec()