import numpy as np
import datetime as dt


class BaselineModel:
    def __init__(self, data, model_params):
        self.data = data
        pass

    def fit(self, start, end):
        pass

    def predict(self, start, end):
        indicies = self.data.get_subset(start, end).index
        return self.data.data.loc[min(indicies)-1:max(indicies)-1, 'Volume']
