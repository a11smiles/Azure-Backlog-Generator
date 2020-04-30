from typing import *
from .userStory import UserStory

class Feature():

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value : str):
        self._title = value

    @property
    def stories(self) -> List[UserStory]:
        return self._stories

    @stories.setter
    def stories(self, value : List[UserStory]):
        self._stories = value