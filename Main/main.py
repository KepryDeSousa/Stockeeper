# main.py
from PyQt6.QtWidgets import QApplication
from View.views import MyWindow
from Controller.controller import ProductController

def apply_stylesheet(app):
    with open('View/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)

    # Inicializa o controlador e a visão
    controller = ProductController(None)  # Inicializa o controlador
    view = MyWindow(controller)  # Passa o controlador para a visão
    controller.view = view  # Conecta o controlador à visão

    view.show()
    app.exec()
