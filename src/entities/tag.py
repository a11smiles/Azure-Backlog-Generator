class Tag():

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value : str):
        self._title = value