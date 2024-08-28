from PyQt6.QtWidgets import QApplication
from views import MyWindow

class Controller:
    def __init__(self):
        self.app = QApplication([])
        self.window = MyWindow(self)
        self.window.show()
        self.app.exec()

    def show_cadastro_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.cadastro_page)

    def show_ferramentas_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.ferramentas_page)

    def show_ajuda_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.ajuda_page)

if __name__ == "__main__":
    controller = Controller()