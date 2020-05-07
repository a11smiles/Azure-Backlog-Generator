import json
from .filesystem import FileSystem
from .parser import Parser
from .validation import Validation
from .. import entities

class Backlog():

    def gatherWorkItems(self):
        fs = FileSystem()
        files = fs.getFiles('./workitems/caf')
        
        return files

    def generate(self):
        files = self.gatherWorkItems()
        

        """
        "
        " TODO: Figure out proper import and testing of json
        "
        """

        #val = Validation()
        #val.validateMetadata(files)