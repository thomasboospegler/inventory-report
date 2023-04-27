from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products):
        oldest_date = SimpleReport.get_oldest_date(products)
        closest_date = SimpleReport.get_closest_date(products)
        company = SimpleReport.get_company_with_more_products(products)
        companies = CompleteReport.get_companies(products)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}\n"
            f"Produtos estocados por empresa:\n"
            f"{CompleteReport.get_companies_quantity(companies)}"
        )

    @staticmethod
    def get_companies(products):
        companies = {}
        for product in products:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 1
            else:
                companies[product["nome_da_empresa"]] += 1
        return companies

    @staticmethod
    def get_companies_quantity(companies):
        companies_quantity = ""
        for company in companies:
            companies_quantity += f"- {company}: {companies[company]}\n"
        return companies_quantity
