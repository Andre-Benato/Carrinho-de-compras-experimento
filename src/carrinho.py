"""Carrinho com frete calculado sobre o subtotal dos itens."""

from math import isfinite


class Carrinho:
    def __init__(self):
        self._itens = {}

    def adicionar_item(self, nome, preco, quantidade=1):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido")
        if (isinstance(preco, bool) or not isinstance(preco, (int, float))
                or not isfinite(preco) or preco < 0):
            raise ValueError("Preço inválido")
        if (isinstance(quantidade, bool) or not isinstance(quantidade, int)
                or quantidade <= 0):
            raise ValueError("Quantidade inválida")

        if nome in self._itens:
            self._itens[nome]["quantidade"] += quantidade
        else:
            self._itens[nome] = {
                "nome": nome, "preco": preco, "quantidade": quantidade,
            }

    def remover_item(self, nome):
        if nome not in self._itens:
            raise ValueError("Item inexistente")
        del self._itens[nome]

    def show(self):
        return [item.copy() for item in self._itens.values()]

    def total(self):
        if not self._itens:
            return 0.0
        subtotal = sum(
            item["preco"] * item["quantidade"] for item in self._itens.values()
        )
        frete = 0 if subtotal >= 150 else 20
        return round(float(subtotal + frete), 2)
