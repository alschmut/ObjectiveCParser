from model.MetricModel import MetricModel
from model.IdentifierType import IdentifierType

class MethodModel():
    name: str = None
    line_start: int = None
    line_stop: int = None
    type: IdentifierType = None

    def __init__(self, name: str, line_start: int, line_stop: int, type: IdentifierType):
        self.name = name
        self.line_start = line_start
        self.line_stop = line_stop
        self.type = type

    def metrics(self):
        return {
            "method_loc": self.line_stop - self.line_start
        }

    def to_csv(self, relative_path, name):
        csv_line = [relative_path + "/" + name]
        csv_line += [value for (key, value) in self.metrics().items()]
        csv_line_as_str = [str(line) for line in csv_line]
        return ";".join(csv_line_as_str) + "\n"

    def get_csv_header(self):
        csv_header = ["path"] 
        csv_header += [str(key) for (key, value) in self.metrics().items()]
        return ";".join(csv_header) + "\n"

    def get_name(self):
        return self.name