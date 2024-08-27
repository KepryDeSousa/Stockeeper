from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication([])
    controller = MainController()
    controller.show_view()
    app.exec()