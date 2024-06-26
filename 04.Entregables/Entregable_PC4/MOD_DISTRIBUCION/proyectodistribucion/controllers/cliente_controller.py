from models.reparto import Reparto

class ClienteController:
    def __init__(self):
        self.reparto_model = Reparto()
    
    def listar_repartidores(self):
        return self.reparto_model.get_repartidores()
