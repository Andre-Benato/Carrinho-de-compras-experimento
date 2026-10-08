import pytest

from src.carrinho import Carrinho


def test_adicionar_item_soma_quantidade_do_mesmo_nome():
    c = Carrinho()
    c.adicionar_item("Camiseta", 50.0, 2)
    c.adicionar_item("Camiseta", 50.0)
    assert c.show() == [{"nome": "Camiseta", "preco": 50.0, "quantidade": 3}]


def test_remover_item_e_erro_quando_nao_existe():
    c = Carrinho()
    c.adicionar_item("Camiseta", 50.0)
    c.remover_item("Camiseta")
    assert c.show() == []
    with pytest.raises(ValueError):
        c.remover_item("Camiseta")


def test_show_lista_todos_os_itens_na_ordem_de_insercao():
    c = Carrinho()
    c.adicionar_item("Camiseta", 50.0, 2)
    c.adicionar_item("Meia", 10.0)
    assert c.show() == [
        {"nome": "Camiseta", "preco": 50.0, "quantidade": 2},
        {"nome": "Meia", "preco": 10.0, "quantidade": 1},
    ]


def test_frete_cobrado_abaixo_de_150():
    c = Carrinho()
    c.adicionar_item("Camiseta", 50.0, 2)  # subtotal 100
    assert c.total() == 120.00


def test_frete_gratis_no_limite_exato_e_acima():
    c = Carrinho()
    c.adicionar_item("Teclado", 150.0)  # exatamente 150
    assert c.total() == 150.00

    c2 = Carrinho()
    c2.adicionar_item("Tenis", 220.0)
    assert c2.total() == 220.00


def test_frete_cobrado_logo_abaixo_do_limite_e_arredondamento():
    c = Carrinho()
    c.adicionar_item("Cabo", 49.99, 3)  # 149.97
    assert c.total() == 169.97


def test_carrinho_vazio_total_zero_sem_frete():
    assert Carrinho().total() == 0.00


def test_erros_de_validacao_na_adicao():
    c = Carrinho()
    with pytest.raises(ValueError):
        c.adicionar_item("x", -5)
    with pytest.raises(ValueError):
        c.adicionar_item("x", 10.0, 0)
    with pytest.raises(ValueError):
        c.adicionar_item("x", 10.0, -1)
    assert c.show() == []
