from typing import *
from .feature import Feature

class Epic():

    def __init__(self):
        self._features = []

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value : str):
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        self._title = value

    @property
    def features(self) -> List[Feature]:
        return self._features

    def addFeature(self, value : Feature):
        if not isinstance(value, Feature):
            raise TypeError("value must be of type 'Feature'")
        self._features.append(value)