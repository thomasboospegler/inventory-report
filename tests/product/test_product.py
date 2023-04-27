from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1, "produto", "empresa", "01/01/2021",
        "01/01/2022", "123", "armazenamento"
    )
    assert produto.id == 1
    assert produto.nome_do_produto == "produto"
    assert produto.nome_da_empresa == "empresa"
    assert produto.data_de_fabricacao == "01/01/2021"
    assert produto.data_de_validade == "01/01/2022"
    assert produto.numero_de_serie == "123"
    assert produto.instrucoes_de_armazenamento == "armazenamento"

    assert (
        produto.__repr__() ==
        "O produto produto fabricado em 01/01/2021 por empresa com validade"
        " até 01/01/2022 precisa ser armazenado armazenamento."
    )
