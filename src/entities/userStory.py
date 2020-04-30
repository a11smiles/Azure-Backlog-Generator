from typing import *
from .task import Task

class UserStory():

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value : str):
        self._title = value

    @property
    def tasks(self) -> List[Task]:
        return self._tasks

    @tasks.setter
    def tasks(self, value : List[Task]):
        self._tasks = value