from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

def setup_menu(window):
    # Adiciona ações aos botões do menu lateral
    menu_actions = {
        'Início': lambda: window.stacked_widget.setCurrentWidget(window.start_page),
        'Cadastro': window.show_cadastro_page,
        'Ferramentas': window.show_ferramentas_page,
        'Ajuda': window.show_ajuda_page
    }

    # Cria o widget do menu lateral
    menu_widget = QWidget()
    menu_layout = QVBoxLayout(menu_widget)

    # Botão de expansão
    toggle_button = QPushButton(">")
    toggle_button.clicked.connect(window.toggle_menu)

    # Adiciona os botões do menu e conecta as ações
    for item, action in menu_actions.items():
        button = QPushButton(item)
        button.clicked.connect(action)  # Conecta a ação ao botão
        button.setStyleSheet("font-size: 14px;")  # Ajuste do estilo dos botões
        menu_layout.addWidget(button)

    menu_layout.addStretch()  # Adiciona um espaçamento flexível no final do menu

    return menu_widget, toggle_button, menu_actions