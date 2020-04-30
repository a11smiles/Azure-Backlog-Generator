from src.entities import *

class Backlog():

    def ValidateMetadata(self, files):
        raise NotImplementedError()

    def Generate(self, files):
        raise NotImplementedError()