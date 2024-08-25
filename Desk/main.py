from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QMainWindow, QHBoxLayout, QStackedWidget, QGroupBox, QScrollArea
)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setup_window()
        self.setup_menu()
        self.setup_layout()

    def setup_window(self):
        icon = QIcon(QPixmap('Logo/WhatsApp Image 2024-08-16 at 8.00.15 PM (2).jpeg'))
        self.setWindowIcon(icon)
        self.setWindowTitle("Stockeeper")

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()

        width = int(screen_size.width() * 0.80)
        height = int(screen_size.height() * 0.7)

        x = int((screen_size.width() - width) / 2)
        y = int((screen_size.height() - height) / 2)

        self.setGeometry(x, y, width, height)

    def setup_menu(self):
        # Adiciona ações aos botões do menu lateral
        self.menu_actions = {
            'Início': lambda: self.stacked_widget.setCurrentWidget(self.start_page),
            'Cadastro': self.toggle_cadastro_options,
            'Ferramentas': self.show_ferramentas_page,
            'Ajuda': self.show_ajuda_page
        }

        # Cria o widget do menu lateral
        self.menu_widget = QWidget()
        self.menu_layout = QVBoxLayout(self.menu_widget)
        self.menu_widget.setFixedWidth(0)  # Inicialmente escondido

        # Botão de expansão
        self.toggle_button = QPushButton(">")
        self.toggle_button.clicked.connect(self.toggle_menu)

        # Adiciona os botões do menu e conecta as ações
        for item, action in self.menu_actions.items():
            button = QPushButton(item)
            button.clicked.connect(action)  # Conecta a ação ao botão
            button.setStyleSheet("font-size: 14px;")  # Ajuste do estilo dos botões
            self.menu_layout.addWidget(button)

        # Cria um container para as opções de cadastro
        self.cadastro_container = QGroupBox()
        self.cadastro_container.setStyleSheet("border: none;")
        self.cadastro_layout = QVBoxLayout(self.cadastro_container)
        self.cadastro_container.setVisible(False)  # Inicialmente escondido

        # Adiciona os botões de cadastro ao container
        cadastro_options = {
            'Clientes': self.show_clientes_page,
            'Produtos': self.show_produtos_page,
            'Fornecedores': self.show_fornecedores_page,
            'Funcionários': self.show_funcionarios_page,
            'Usuários': self.show_usuarios_page
        }
        
        for option, action in cadastro_options.items():
            button = QPushButton(option)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            self.cadastro_layout.addWidget(button)
        
        self.menu_layout.addWidget(self.cadastro_container)  # Adiciona o container ao menu lateral
        self.menu_layout.addStretch()  # Adiciona um espaçamento flexível no final do menu

    def setup_layout(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        # Adiciona o menu lateral e o botão de expansão
        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(self.toggle_button)

        # Cria a área de navegação central com QStackedWidget
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        # Adiciona páginas ao QStackedWidget
        self.start_page = self.create_page("Bem-vindo ao Stockeeper")
        self.ferramentas_page = self.create_page("Página de Ferramentas")
        self.ajuda_page = self.create_page("Página de Ajuda")

        # Adiciona os widgets ao QStackedWidget
        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.ferramentas_page)
        self.stacked_widget.addWidget(self.ajuda_page)

        self.setCentralWidget(central_widget)

    def toggle_menu(self):
        # Expande ou esconde o menu
        if self.menu_widget.width() == 0:
            self.menu_widget.setFixedWidth(200)  # Expande o menu
            self.toggle_button.setText("<")
        else:
            self.menu_widget.setFixedWidth(0)  # Esconde o menu
            self.toggle_button.setText(">")

    def toggle_cadastro_options(self):
        # Alterna a visibilidade do painel de opções de cadastro
        if self.cadastro_container.isVisible():
            self.cadastro_container.setVisible(False)
        else:
            self.cadastro_container.setVisible(True)

    def show_ferramentas_page(self):
        self.stacked_widget.setCurrentWidget(self.ferramentas_page)

    def show_ajuda_page(self):
        self.stacked_widget.setCurrentWidget(self.ajuda_page)

    def create_page(self, text):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

    def show_clientes_page(self):
        self.stacked_widget.setCurrentWidget(self.create_details_page("Clientes"))

    def show_produtos_page(self):
        self.stacked_widget.setCurrentWidget(self.create_details_page("Produtos"))

    def show_fornecedores_page(self):
        self.stacked_widget.setCurrentWidget(self.create_details_page("Fornecedores"))

    def show_funcionarios_page(self):
        self.stacked_widget.setCurrentWidget(self.create_details_page("Funcionários"))

    def show_usuarios_page(self):
        self.stacked_widget.setCurrentWidget(self.create_details_page("Usuários"))

    def create_details_page(self, title):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(f"Detalhes para {title}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

def apply_stylesheet(app):
    with open('Desk/styles.qss', 'r') as file:
        style = file.read()
    app.setStyleSheet(style)

if __name__ == "__main__":
    app = QApplication([])
    apply_stylesheet(app)
    window = MyWindow()
    window.show()
    app.exec()
