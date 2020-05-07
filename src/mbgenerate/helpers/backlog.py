import json
from .filesystem import FileSystem
from .parser import Parser
from .validation import Validation
from .. import entities

"""
"
" - 1. Get all files ("gatherWorkItems")
" - 2. Parse work item heirarchy ("parseWorkItems)
"   2.1. Validate each metadata file
"   2.2. Create workitem objects
" 3. Create backlog
"
"""

class Backlog():

    def _gatherWorkItems(self):
        fs = FileSystem()
        files = fs.getFiles('./workitems/caf')
        
        return files

    def _parseWorkItems(self, files):
        parser = Parser()
        parsedFiles = parser.fileHierarchy(files)

        return parsedFiles

    def generate(self):
        files = self._gatherWorkItems()
        parsedFiles = self._parseWorkItems(files)

        print(parsedFiles)