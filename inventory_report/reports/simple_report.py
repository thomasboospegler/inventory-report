from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products):
        oldest_date = SimpleReport.get_oldest_date(products)
        closest_date = SimpleReport.get_closest_date(products)
        company = SimpleReport.get_company_with_more_products(products)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company}"
        )

    @staticmethod
    def get_oldest_date(products):
        oldest_date = products[0]["data_de_fabricacao"]
        for product in products:
            if product["data_de_fabricacao"] < oldest_date:
                oldest_date = product["data_de_fabricacao"]
        return oldest_date

    @staticmethod
    def get_closest_date(products):
        today = datetime.now().strftime("%Y-%m-%d")
        closest_date = None
        for product in products:
            if product["data_de_validade"] >= today:
                if closest_date is None:
                    closest_date = product["data_de_validade"]
                elif product["data_de_validade"] < closest_date:
                    closest_date = product["data_de_validade"]
        return closest_date

    @staticmethod
    def get_company_with_more_products(products):
        companies = {}
        for product in products:
            if product["nome_da_empresa"] not in companies:
                companies[product["nome_da_empresa"]] = 1
            else:
                companies[product["nome_da_empresa"]] += 1
        return max(companies, key=companies.get)
