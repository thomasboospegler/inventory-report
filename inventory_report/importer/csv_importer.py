from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".csv"):
            with open(path, "r") as file:
                reader = csv.DictReader(file)
                return list(reader)
        else:
            raise ValueError("Arquivo inválido")
