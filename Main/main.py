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

   
    controller = Controller()  
    view = MyWindow(controller) 
    controller.window = view  

    view.show()
