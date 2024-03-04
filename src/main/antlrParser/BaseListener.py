from model.MethodModel import MethodModel
from model.IdentifierType import IdentifierType

class BaseListener():
    methods: [MethodModel] = None

    def __init__(self):
        self.methods = []

    def get_methods(self):
        return self.methods
    
    def add_method(self, name: str, line_start: int, line_stop: int, type: IdentifierType):
        return self.methods.append(MethodModel(name, line_start, line_stop, type))