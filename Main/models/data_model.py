class DataModel:
    def __init__(self):
        self.data = "Initial Data"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data