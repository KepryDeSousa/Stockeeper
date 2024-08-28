# models.py
class Produto:
    def __init__(self, id: int, nome: str, preco: float, quantidade: int):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

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
    