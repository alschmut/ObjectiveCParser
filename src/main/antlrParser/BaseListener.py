from model.MethodModel import MethodModel
from typing import List

class BaseListener():
    methods: List[MethodModel] = None

    def __init__(self):
        self.methods = []

    def get_methods(self):
        return self.methods
    
    def add_method(self, name: str, line_start: int, line_stop: int):
        return self.methods.append(MethodModel(name, line_start, line_stop))