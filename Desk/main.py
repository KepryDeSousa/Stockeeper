from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setup_window()
        self.create_menu()
        self.setup_layout()
    
    def setup_window(self):
        # Definir o ícone da janela
        icon = QIcon(QPixmap('Logo/WhatsApp Image 2024-08-16 at 8.00.15 PM (2).jpeg'))
        self.setWindowIcon(icon)
        self.setWindowTitle("Stockeeper")

        # Definindo o tamanho da janela
        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()

        width_percentage = 0.85
        height_percentage = 0.7

        width = int(screen_size.width() * width_percentage)
        height = int(screen_size.height() * height_percentage)

        x = int((screen_size.width() - width) / 2)
        y = int((screen_size.height() - height) / 2)

        self.setGeometry(x, y, width, height)

    def create_menu(self):
        # Criar o menu de cadastro
        menu = self.menuBar()
        menu_cadastro = menu.addMenu('Cadastro')

        actions = {
            'Clientes': self.clientes_action,
            'Produtos': self.produtos_action,
            'Fornecedores': self.fornecedores_action,
            'Funcionários': self.funcionarios_action,
            'Usuários': self.usuarios_action,
        }

        for action_name, action_func in actions.items():
            action = menu_cadastro.addAction(action_name)
            action.triggered.connect(action_func)

    def setup_layout(self):
        # Criando a interface
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

       
        label = QLabel("Bem-vindo ao Stockeeper")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

    def clientes_action(self):
        print("Ação Clientes ativada")

    def produtos_action(self):
        print("Ação Produtos ativada")

    def fornecedores_action(self):
        print("Ação Fornecedores ativada")

    def funcionarios_action(self):
        print("Ação Funcionários ativada")

    def usuarios_action(self):
        print("Ação Usuários ativada")


def apply_stylesheet(app):
    with open('Desk/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)
    window = MyWindow()
    window.setFixedSize(window.size())
    window.show()
    app.exec()
