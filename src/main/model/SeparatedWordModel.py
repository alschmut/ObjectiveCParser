from model.MetricModel import MetricModel
from model.MetricType import MetricType

class SeparatedWordModel():

    vector = None
    lemmatized_word: str = None
    metrics: dict = None

    def __init__(self, name: str):
        self.metrics = {}
        self.metrics["word_frequency_per_file"] = MetricModel(MetricType.Absolute, 1)

    def bool_to_int(self, value: bool):
        return 1 if value else 0

    def get_metrics(self):
        return self.metrics

    def get_metric_by_key(self, key):
        return self.metrics.get(key)

    def to_print(self):
        return {
            "lemmatized_word": self.lemmatized_word,            
            "metrics": {key: metric_model.to_print() for (key, metric_model) in self.metrics.items()},
        }

    def increment_frequency(self):
        self.metrics["word_frequency_per_file"].increment_value_by_1()