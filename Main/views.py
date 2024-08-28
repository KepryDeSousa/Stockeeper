from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLabel, QGroupBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
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
        self.menu_actions = {
            'Início': lambda: self.stacked_widget.setCurrentWidget(self.start_page),
            'Cadastro': self.controller.show_cadastro_page,
            'Ferramentas': self.controller.show_ferramentas_page,
            'Ajuda': self.controller.show_ajuda_page
        }

        self.menu_widget = QWidget()
        self.menu_layout = QVBoxLayout(self.menu_widget)
        self.menu_widget.setFixedWidth(0)  # Inicialmente escondido

        self.toggle_button = QPushButton(">")
        self.toggle_button.clicked.connect(self.toggle_menu)

        for item, action in self.menu_actions.items():
            button = QPushButton(item)
            button.clicked.connect(action)
            button.setStyleSheet("font-size: 14px;")
            self.menu_layout.addWidget(button)

        self.menu_layout.addStretch()

    def setup_layout(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(self.toggle_button)

        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.start_page = self.create_page("Bem-vindo ao Stockeeper")
        self.cadastro_page = self.create_cadastro_page()
        self.ferramentas_page = self.create_ferramentas_page()
        self.ajuda_page = self.create_ajuda_page()

        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.cadastro_page)
        self.stacked_widget.addWidget(self.ferramentas_page)
        self.stacked_widget.addWidget(self.ajuda_page)

        self.setCentralWidget(central_widget)

    def toggle_menu(self):
        if self.menu_widget.width() == 0:
            self.menu_widget.setFixedWidth(200)
            self.toggle_button.setText("<")
        else:
            self.menu_widget.setFixedWidth(0)
            self.toggle_button.setText(">")

    def create_page(self, text):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 16px;")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

    def create_details_page(self, title):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(f"Detalhes para {title}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

    def create_cadastro_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Escolha uma opção de Cadastro")
        group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(14, 68, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

        cadastro_options = {
            'Produtos': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Produtos")),
            'Fornecedores': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Fornecedores")),
            'Funcionários': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Funcionários")),
            'Administrador': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Administrador")),
        }

        for option, action in cadastro_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            group_box_layout.addWidget(button)

        layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

    def create_ferramentas_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Ferramentas")
        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(10, 60, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

        ferramentas_options = {
            'Backup': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Backup")),
            'Relatórios': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Relatórios")),
            'Estoque': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Estoque")),
            'Configurações': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Configurações")),
        }

        for option, action in ferramentas_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            group_box_layout.addWidget(button)

        layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

    def create_ajuda_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Ajuda")
        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(10, 60, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

        ajuda_options = {
            'Documentação': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Documentação")),
            'Suporte': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Suporte")),
            'Sobre': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Sobre"))
        }

        for option, action in ajuda_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            group_box_layout.addWidget(button)

        layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page
