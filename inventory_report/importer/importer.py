from abc import ABC, abstractclassmethod


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, path, report_type):
        raise NotImplementedError
