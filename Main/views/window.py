from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QMainWindow, QStackedWidget, QWidget, QHBoxLayout, QApplication
import sys
sys.path.append('Main/utils')  # Replace 'path/to/utils' with the actual path to the 'utils' module

from menu import setup_menu
from pages import create_page, create_cadastro_page, create_ferramentas_page, create_ajuda_page

class MainWindow(QMainWindow):
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
        self.setWindowOpacity(0.90)

        screen = QApplication.primaryScreen()
        screen_size = screen.availableGeometry()

        width = int(screen_size.width() * 0.80)
        height = int(screen_size.height() * 0.7)
        x = int((screen_size.width() - width) / 2)
        y = int((screen_size.height() - height) / 2)

        self.setGeometry(x, y, width, height)

    def setup_menu(self):
        self.menu_widget, self.toggle_button, self.menu_actions = setup_menu(self)
        self.menu_widget.setFixedWidth(0)  # Inicialmente escondido

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
        self.start_page = create_page("Bem-vindo ao Stockeeper")
        self.cadastro_page = create_cadastro_page(self)
        self.ferramentas_page = create_ferramentas_page(self)
        self.ajuda_page = create_ajuda_page(self)

        # Adiciona os widgets ao QStackedWidget
        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.cadastro_page)
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

    def set_label_text(self, text):
        self.start_page.findChild(QLabel).setText(text)