from models.data_model import DataModel
from views.window import MainWindow

class MainController:
    def __init__(self):
        self.model = DataModel()
        self.view = MainWindow()
        self.view.toggle_button.clicked.connect(self.update_data)

    def show_view(self):
        self.view.show()

    def update_data(self):
        new_data = "Updated Data"
        self.model.set_data(new_data)
        self.view.set_label_text(self.model.get_data())