from PyQt6.QtWidgets import QApplication
from views import MyWindow

class Controller:
    def __init__(self):
        self.app = QApplication([])
        self.window = MyWindow(self)
        self.window.show()
        self.app.exec()


    #aqui está acionando as funções de cada botão do menu (Principal)

    def show_caixa_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.caixa_page)

    def show_cadastro_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.cadastro_page)

    def show_consultas_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.consultas_page)

    def show_ferramentas_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.ferramentas_page)

    def show_ajuda_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.ajuda_page)
    
    #Submenu actions

    #Caixa
    def show_caixa_venda_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.caixa_venda_page)
    
    def show_fechamento_caixa_page(self):
        self.window.stacked_widget.setCurrentWidget(self.window.fechamento_caixa_page)

if __name__ == "__main__":
    controller = Controller()