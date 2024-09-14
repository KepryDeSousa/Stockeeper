class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self._nome
        self._preco
        self._quantidade 

    def get_custo_total(self) -> float:
        return self.preco * self.quantidade

    @property
    def nome(self) -> str:
        return self._nome
    @property
    def preco(self) -> float:
        return self._preco
    @property
    def quantidade(self) -> int:
        return self._quantidade
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @preco.setter
    def preco(self, preco: float):
        self._preco = preco
    
    @quantidade.setter
    def quantidade(self, quantidade: int):
        self._quantidade = quantidade
