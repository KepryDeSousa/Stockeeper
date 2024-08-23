# small_panel.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy

class SmallPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Configurar o painel reduzido
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.setFixedSize(200, 100)  # Tamanho reduzido

        # Layout do painel reduzido
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Adicionar widgets ao painel
        self.small_label = QLabel("Painel Reduzido")
        self.layout.addWidget(self.small_label)
