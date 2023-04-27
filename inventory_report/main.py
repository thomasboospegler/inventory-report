from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def main():
    try:
        _, file, type = sys.argv

        report_types = {"simples": SimpleReport, "completo": CompleteReport}

        content = get_importer(file)

        content.import_data(file, type)

        sys.stdout.write(report_types[type].generate(content.data))

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")


def get_importer(file):
    if ".csv" in file:
        return InventoryRefactor(CsvImporter)
    elif ".json" in file:
        return InventoryRefactor(JsonImporter)
    elif ".xml" in file:
        return InventoryRefactor(XmlImporter)
    else:
        raise ValueError
