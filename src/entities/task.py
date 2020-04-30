from typing import *
from .tag import Tag

class Task():

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value : str):
        self._title = value

    @property
    def tags(self) -> List[Tag]:
        return self._tags

    @tags.setter
    def tags(self, value : List[Tag]):
        self._tags = value
