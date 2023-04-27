from inventory_report.inventory.product import Product


def test_relatorio_produto():
    produto = Product(
        "1",
        "Cerveja",
        "Ambev",
        "01/01/2020",
        "01/01/2021",
        "123456",
        "gelado",
    )
    assert (
        produto.__repr__() == (
            "O produto Cerveja fabricado em 01/01/2020 por Ambev com "
            "validade até 01/01/2021 precisa ser armazenado gelado."
        )
    )
