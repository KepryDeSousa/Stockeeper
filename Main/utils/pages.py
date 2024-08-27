from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QPushButton
from PyQt6.QtCore import Qt

def create_page(text):
    page = QWidget()
    layout = QVBoxLayout(page)
    label = QLabel(text)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 16px;")
    layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
    return page

def create_cadastro_page(window):
    page = QWidget()
    layout = QVBoxLayout(page)

    # Cria um QGroupBox para os botões de cadastro
    group_box = QGroupBox("Escolha uma opção de Cadastro")
    group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)

    group_box_layout = QVBoxLayout(group_box)

    # Ajusta o estilo e margens do QGroupBox
    group_box_layout.setContentsMargins(14, 68, 10, 10)  # Margem superior ajustada
    group_box.setStyleSheet("font-size: 16px; font-weight: bold;")
    group_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # Adiciona os botões de cadastro dentro do QGroupBox
    cadastro_options = {
        'Produtos': window.show_produtos_page,
        'Fornecedores': window.show_fornecedores_page,
        'Funcionários': window.show_funcionarios_page,
        'Administrador': window.show_adm_page,
    }
    
    for option, action in cadastro_options.items():
        button = QPushButton(option)
        button.setFixedWidth(150)  # Define a largura fixa dos botões
        button.setStyleSheet("font-size: 14px; margin: 5px;")
        button.clicked.connect(action)
        group_box_layout.addWidget(button)

    # Centraliza o QGroupBox na página de cadastro
    layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
    
    return page

def create_ferramentas_page(window):
    page = QWidget()
    layout = QVBoxLayout(page)

    # Cria um QGroupBox para as opções de ferramentas
    group_box = QGroupBox("Ferramentas")
    
    # Adiciona uma imagem à página de ferramentas

    group_box_layout = QVBoxLayout(group_box)

    # Ajusta o estilo e margens do QGroupBox
    group_box_layout.setContentsMargins(10, 60, 10, 10)  # Margem superior ajustada
    group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

    # Adiciona os botões de ferramentas dentro do QGroupBox
    ferramentas_options = {
        'Backup': window.show_backup_page,
        'Configurações': window.show_configuracoes_page,
        'Relatórios': window.show_relatorios_page
    }
    
    for option, action in ferramentas_options.items():
        button = QPushButton(option)
        button.setFixedWidth(150)  # Define a largura fixa dos botões
        button.setStyleSheet("font-size: 14px; margin: 5px;")
        button.clicked.connect(action)
        group_box_layout.addWidget(button)

    # Centraliza o QGroupBox na página de ferramentas
    layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
    
    return page

def create_ajuda_page(window):
    page = QWidget()
    layout = QVBoxLayout(page)

    # Cria um QGroupBox para as opções de ajuda
    group_box = QGroupBox("Ajuda")
    group_box_layout = QVBoxLayout(group_box)

    # Ajusta o estilo e margens do QGroupBox
    group_box_layout.setContentsMargins(10, 60, 10, 10)  # Margem superior ajustada
    group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

    # Adiciona os botões de ajuda dentro do QGroupBox
    ajuda_options = {
        'Documentação': window.show_documentacao_page,
        'Suporte': window.show_suporte_page,
        'Sobre': window.show_sobre_page
    }
    
    for option, action in ajuda_options.items():
        button = QPushButton(option)
        button.setFixedWidth(150)  # Define a largura fixa dos botões
        button.setStyleSheet("font-size: 14px; margin: 5px;")
        button.clicked.connect(action)
        group_box_layout.addWidget(button)

    # Centraliza o QGroupBox na página de ajuda
    layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
    
    return page