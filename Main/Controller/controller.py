# controllers.py
from PyQt6.QtCore import Qt  # Adicione esta linha para importar Qt
from Main.Model.models import Produto
from ..View.views import MyWindow
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton

class ProductController:
    def __init__(self, view):
        self.view = view
        self.produtos = []

    def add_new_product(self, nome, preco):
        produto = Produto(len(self.produtos) + 1, nome, preco, 1)
        self.produtos.append(produto)
        # Atualize a view se necessário

    def show_cadastro_page(self):
        self.view.stacked_widget.setCurrentWidget(self.view.create_cadastro_page())

    def show_ferramentas_page(self):
        self.view.stacked_widget.setCurrentWidget(self.view.create_ferramentas_page())

    def show_ajuda_page(self):
        self.view.stacked_widget.setCurrentWidget(self.view.create_ajuda_page())

    def create_cadastro_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Escolha uma opção de Cadastro")
        group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Usa a constante Qt.AlignmentFlag.AlignCenter
        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(14, 68, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")
        group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cadastro_options = {
            'Produtos': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Produtos")),
            'Fornecedores': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Fornecedores")),
            'Funcionários': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Funcionários")),
            'Administrador': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Administrador")),
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
            'Backup': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Backup")),
            'Configurações': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Configurações")),
            'Relatórios': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Relatórios"))
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
            'Documentação': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Documentação")),
            'Suporte': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Suporte")),
            'Sobre': lambda: self.view.stacked_widget.setCurrentWidget(self.view.create_details_page("Sobre"))
        }

        for option, action in ajuda_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            group_box_layout.addWidget(button)

        layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page
