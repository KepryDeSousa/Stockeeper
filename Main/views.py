from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QLabel, QGroupBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLineEdit
from Models.produto_model import Produto

class MyWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui() #Starter interface function

    def init_ui(self):
        self.setup_window()
        self.setup_menu()
        self.setup_layout()

    def setup_window(self):
        icon = QIcon(QPixmap('Main/styles/Logo/WhatsApp Image 2024-08-16 at 8.00.15 PM (2).jpeg'))
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
            'Caixa': self.controller.show_caixa_page,
            'Cadastro': self.controller.show_cadastro_page,
            'Consultas': self.controller.show_consultas_page,
            'Ferramentas': self.controller.show_ferramentas_page,
            'Ajuda': self.controller.show_ajuda_page

        }

        self.menu_widget = QWidget()
        self.menu_layout = QVBoxLayout(self.menu_widget)
        self.menu_widget.setFixedWidth(0) 

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

        #Chamada das funções de cada botão do menu
        self.start_page = self.create_page("Bem-vindo ao Stockeeper")
        self.cadastro_page = self.create_cadastro_page()
        self.ferramentas_page = self.create_ferramentas_page()
        self.ajuda_page = self.create_ajuda_page()
        self.caixa_page = self.create_caixa_page()
        self.consultas_page = self.create_consultas_page()


        #Implementação das páginas
        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.caixa_page)
        self.stacked_widget.addWidget(self.consultas_page)
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


    # Menu 



    def create_cadastro_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Cadastro")

        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(14, 68, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")

        cadastro_options = {
            'Produtos': self.show_product_registration_page,
            'Fornecedores': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Fornecedores")),
            'Funcionários': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Funcionários")),
            'Administrador': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Administrador")),
        }
        
        for option, action in cadastro_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action) # Connect the button to the action when clicked
            group_box_layout.addWidget(button)

        
        '''      button = QPushButton(option)
                button = QPushButton('Produtos')
                button.setFixedWidth(150)
                button.setStyleSheet("font-size: 14px; margin: 5px;")
                button.clicked.connect(self.teste)
                group_box_layout.addWidget(button)
        '''
        layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page

  
        return 'teste de click'
    
    def create_caixa_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)# Vertical layout
        QLabel("Caixa")

        grupo_box= QGroupBox('Caixa')
        grupo_box_layout = QVBoxLayout(grupo_box)
        grupo_box_layout.setContentsMargins(10, 60, 10, 10)
        grupo_box.setStyleSheet("font-size: 16px; font-weight: bold;")
        caixa_options = {
            'Abrir Caixa': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Abrir Caixa")),
            'Fechar Caixa': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Fechar Caixa")),
        
            }
        for option, action in caixa_options.items():
            button = QPushButton(option)
            button.setFixedWidth(150)
            button.setStyleSheet("font-size: 14px; margin: 5px;")
            button.clicked.connect(action)
            grupo_box_layout.addWidget(button)

        layout.addWidget(grupo_box, alignment=Qt.AlignmentFlag.AlignCenter)
        return page
    
    def create_consultas_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        group_box = QGroupBox("Consultas")

        group_box_layout = QVBoxLayout(group_box)
        group_box_layout.setContentsMargins(14, 68, 10, 10)
        group_box.setStyleSheet("font-size: 16px; font-weight: bold;")
        ferramentas_options = {
            'Produtos': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Produtos")),
            'Vendas': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Vendas")),
            'Fornecedores': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Fornecedores")),
            'Funcionários': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Funcionários")),
            'Administrador': lambda: self.stacked_widget.setCurrentWidget(self.create_details_page("Administrador")),

        }

        for option, action in ferramentas_options.items():
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

    #Produtos : 
    def show_product_registration_page(self):
        # Cria a página de cadastro de produtos e adiciona ao QStackedWidget
        product_page = self.create_product_registration_page()

        # Verifica se a página já foi adicionada ao QStackedWidget
        if not self.stacked_widget.indexOf(product_page) != -1:
            self.stacked_widget.addWidget(product_page)  # Adiciona ao QStackedWidget se não estiver

        # Exibe a página
        self.stacked_widget.setCurrentWidget(product_page)
        
    def create_product_registration_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        label = QLabel("Cadastro de Produtos")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; margin-top: 20px;")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionar campos de entrada para o cadastro de produtos
        self.product_name_input = QLineEdit()
        self.product_name_input.setPlaceholderText("Nome do Produto")
        layout.addWidget(self.product_name_input)

        self.product_price_input = QLineEdit()
        self.product_price_input.setPlaceholderText("Preço")
        layout.addWidget(self.product_price_input)

        self.product_quantity_input = QLineEdit()
        self.product_quantity_input.setPlaceholderText("Quantidade")
        layout.addWidget(self.product_quantity_input)

        self.product_category_input = QLineEdit()
        self.product_category_input.setPlaceholderText("Categoria_id")
        layout.addWidget(self.product_category_input)

        # Botão para salvar o produto
        save_button = QPushButton("Salvar Produto")
        save_button.clicked.connect(self.save_product)
        layout.addWidget(save_button)

        return page

    def save_product(self):

        # Obter os valores dos campos de entrada
        product_name = self.product_name_input.text()
        product_price = self.product_price_input.text()
        product_quantity = self.product_quantity_input.text()
        product_category = self.product_category_input.text()

        # Validar os valores
        if not product_name or not product_price:
            print("Por favor, preencha todos os campos.")
            return

        try:
            product_price = float(product_price)
        except ValueError:
            print("Por favor, insira um preço válido.")
            return

        if not product_category:
            product_category = None

        # Criar uma instância do modelo de produto e salvar no banco de dados
        produto = Produto(nome=product_name, preco=product_price, quantidade=product_quantity, categoria_id=product_category)
        produto.salvar()
        return "Status : Operação concluida com sucesso"
    

       