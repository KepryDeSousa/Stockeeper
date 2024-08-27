# main.py
from PyQt6.QtWidgets import QApplication
from View.views import MyWindow
from Controller.controller import ProductController



def apply_stylesheet(app):
    with open('Desk/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)

    # Inicializa o controlador e a visão
    controller = ProductController(None)  # Passaremos a visão depois
    view = MyWindow(controller)
    controller.view = view  # Conecta o controlador à visão

    view.show()
    app.exec()
