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

    def _getAndValidateJson(self, path):
        fs = FileSystem()
        content = fs.readFile(path)

        parser = Parser()
        json = parser.json(content)

        val = Validation()
        if val.validateMetadata(json):
            return json
        else:
            return False

    def _buildWorkItems(self, parsedFiles):
        epics = []
        for epic in parsedFiles:
            builtEpic = self._buildEpic(epic)
            if builtEpic != None:
                epics.append(builtEpic)

        return epics

    def _createTag(self, title):
        tag = entities.Tag()
        tag.title = title

        return tag

    def _buildEpic(self, item):
        json = self._getAndValidateJson(item["epic"])
        if json != False:
            epic = entities.Epic()
            epic.title = json["title"]
            epic.description = json["description"]
            epic.addTag(self._createTag(json["tag"]))
            for role in json["roles"]:
                epic.addTag(self._createTag(role))
            
            if "features" in item.keys() and len(item["features"]) > 0:
                for feature in item["features"]:
                    builtFeature = self._buildFeature(feature)
                    if builtFeature != None:
                        epic.addFeature(builtFeature)

            return epic
        else:
            return None

    def _buildFeature(self, item):
        json = self._getAndValidateJson(item["feature"])
        if json != False:
            feature = entities.Feature()
            feature.title = json["title"]
            feature.description = json["description"]
            feature.addTag(self._createTag(json["tag"]))
            for role in json["roles"]:
                feature.addTag(self._createTag(role))
            
            if "stories" in item.keys() and len(item["stories"]) > 0:
                for story in item["stories"]:
                    builtStory = self._buildStory(story)
                    if builtStory != None:
                        feature.addUserStory(builtStory)

            return feature
        else:
            return None

    def _buildStory(self, item):
        json = self._getAndValidateJson(item["story"])
        if json != False:
            story = entities.UserStory()
            story.title = json["title"]
            story.description = json["description"]
            story.addTag(self._createTag(json["tag"]))
            for role in json["roles"]:
                story.addTag(self._createTag(role))
            
            if "tasks" in item.keys() and len(item["tasks"]) > 0:
                for task in item["tasks"]:
                    builtTask = self._buildTask(task)
                    if builtTask != None:
                        story.addTask(builtTask)

            return story
        else:
            return None

    def _buildTask(self, item):
        json = self._getAndValidateJson(item["task"])
        if json != False:
            task = entities.Task()
            task.title = json["title"]
            task.description = json["description"]
            task.addTag(self._createTag(json["tag"]))
            for role in json["roles"]:
                task.addTag(self._createTag(role))
 
            return task
        else:
            return None

    def generate(self):
        files = self._gatherWorkItems()
        parsedFiles = self._parseWorkItems(files)
        workItems = self._buildWorkItems(parsedFiles)

        