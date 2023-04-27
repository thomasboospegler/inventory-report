from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

colored_strings = [
    "\033[32mData de fabricação mais antiga:\033[0m",
    "\033[32mData de validade mais próxima:\033[0m",
    "\033[32mEmpresa com mais produtos:\033[0m",
    "\033[36m2021-03-10\033[0m",
    "\033[36m2023-05-09\033[0m",
    "\033[31mAmbev\033[0m",
]


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport).generate(
        [
            {
                "id": 1,
                "nome_do_produto": "Skol",
                "nome_da_empresa": "Ambev",
                "data_de_fabricacao": "2021-03-10",
                "data_de_validade": "2023-05-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Gelado",
            }
        ]
    )
    for string in colored_strings:
        assert string in report
