import pytest
import json
import os
from mock import Mock, MagicMock
from pyfakefs import fake_filesystem
from mocks import _mockFileList, _mockParsedFileList, _mockCorrectFileSystem, _mockParsedFileList
import src.azbacklog.helpers as helpers
import src.azbacklog.entities as entities

def _contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

def test_gatherWorkItems(monkeypatch):
    def mockGatherWorkItemsReturnFileList(*args, **kwargs):
        return _mockFileList()

    monkeypatch.setattr(helpers.FileSystem, "getFiles", mockGatherWorkItemsReturnFileList)

    backlog = helpers.Backlog()
    assert backlog._gatherWorkItems('.') == _mockFileList()

def test_parseWorkItems(monkeypatch):
    def mockParseWorkItemsReturnFileList(*args, **kwargs):
        return _mockParsedFileList()

    monkeypatch.setattr(helpers.Parser, "fileHierarchy", mockParseWorkItemsReturnFileList)

    backlog = helpers.Backlog()
    assert backlog._parseWorkItems('.') == _mockParsedFileList()

def test_getAndValidateJson(monkeypatch, fs):
    _mockCorrectFileSystem(fs)

    def mockFileSystemReadFileReturnNone(*args, **kwargs):
        return None

    def mockParserJsonReturnJson(*args, **kwargs):
        content = None
        with open('./correct/01_folder/metadata.json', 'r') as reader:
            content = reader.read()
            reader.close()

        return json.loads(content)

    def mockValidationValidateMetadataReturnTrue(*args, **kwargs):
        return True

    def mockValidationValidateMetadataReturnFalse(*args, **kwargs):
        return False

    monkeypatch.setattr(helpers.FileSystem, "readFile", mockFileSystemReadFileReturnNone)
    monkeypatch.setattr(helpers.Parser, "json", mockParserJsonReturnJson)

    backlog = helpers.Backlog()

    monkeypatch.setattr(helpers.Validation, "validateMetadata", mockValidationValidateMetadataReturnTrue)
    assert backlog._getAndValidateJson('.') == mockParserJsonReturnJson()

    monkeypatch.setattr(helpers.Validation, "validateMetadata", mockValidationValidateMetadataReturnFalse)
    assert backlog._getAndValidateJson('.') == False

def test_buildWorkItems(fs):
    backlog = helpers.Backlog()
    backlog._buildEpic = MagicMock(return_value=None)
    workitems = backlog._buildWorkItems(_mockParsedFileList())

    backlog._buildEpic.assert_any_call(_mockParsedFileList()[0])
    backlog._buildEpic.assert_any_call(_mockParsedFileList()[1])
    backlog._buildEpic.assert_any_call(_mockParsedFileList()[2])
    assert workitems == []

    epic = entities.Epic()
    epic.title = "Foobar"
    epic.description = "Some Description"
    backlog._buildEpic = MagicMock(return_value=epic)
    workitems = backlog._buildWorkItems([_mockParsedFileList()[0]])
    assert len(workitems) == 1
    assert workitems[0] == epic
    assert workitems[0].title == "Foobar"
    assert workitems[0].description == "Some Description"


def test_createTag(fs):
    backlog = helpers.Backlog()
    tag = backlog._createTag("foo bar")

    assert isinstance(tag, entities.Tag) == True
    assert tag.title == "foo bar"

def test_buildEpic(fs):
    _mockCorrectFileSystem(fs)

    def mockParserJsonReturnEpicJson(*args, **kwargs):
        content = None
        with open('./correct/01_folder/02_folder/metadata.json', 'r') as reader:
            content = reader.read()
            reader.close()

        return json.loads(content)

    def mockBacklogBuildFeatureReturnFeature(*args, **kwargs):
        feature = entities.Feature()
        feature.title = "Some Feature"
        feature.description = "Some Description"
        
        return feature

    backlog = helpers.Backlog()

    backlog._getAndValidateJson = MagicMock(return_value=False)
    epic = backlog._buildEpic(_mockParsedFileList()[0])
    assert epic == None

    backlog._getAndValidateJson = MagicMock(return_value=mockParserJsonReturnEpicJson())
    backlog._buildFeature = MagicMock(return_value=None)
    epic = backlog._buildEpic(_mockParsedFileList()[0])
    assert epic.title == "Foo bar"
    assert epic.description == "Lorem Ipsum 01_folder/02_folder"
    assert len(epic.tags) == 3
    assert _contains(epic.tags, lambda tag: tag.title == "01_Folder") == True
    assert _contains(epic.tags, lambda tag: tag.title == "02_Folder") == True
    assert _contains(epic.tags, lambda tag: tag.title == "AppDev") == True
    assert len(epic.features) == 0
    
    backlog._buildFeature = MagicMock(return_value=mockBacklogBuildFeatureReturnFeature())
    epic = backlog._buildEpic(_mockParsedFileList()[0])
    assert len(epic.features) == 3  # should return 3 instances of the mocked feature since the mocked epic has 3 features
    assert epic.features[0].title == "Some Feature"
    assert epic.features[0].description == "Some Description"

def test_buildFeature(fs):
    _mockCorrectFileSystem(fs)

    def mockParserJsonReturnFeatureJson(*args, **kwargs):
        content = None
        with open('./correct/01_folder/02_folder/metadata.json', 'r') as reader:
            content = reader.read()
            reader.close()

        return json.loads(content)

    def mockBacklogBuildStoryReturnStory(*args, **kwargs):
        story = entities.UserStory()
        story.title = "Some Story"
        story.description = "Some Description"
        
        return story

    def mockFeature(*args, **kwargs):
        return _mockParsedFileList()[0]["features"][0]

    backlog = helpers.Backlog()

    backlog._getAndValidateJson = MagicMock(return_value=False)
    feature = backlog._buildFeature(mockFeature())
    assert feature == None

    backlog._getAndValidateJson = MagicMock(return_value=mockParserJsonReturnFeatureJson())
    backlog._buildStory = MagicMock(return_value=None)
    feature = backlog._buildFeature(mockFeature())
    assert feature.title == "Foo bar"
    assert feature.description == "Lorem Ipsum 01_folder/02_folder"
    assert len(feature.tags) == 3
    assert _contains(feature.tags, lambda tag: tag.title == "01_Folder") == True
    assert _contains(feature.tags, lambda tag: tag.title == "02_Folder") == True
    assert _contains(feature.tags, lambda tag: tag.title == "AppDev") == True
    assert len(feature.userStories) == 0
    
    backlog._buildStory = MagicMock(return_value=mockBacklogBuildStoryReturnStory())
    feature = backlog._buildFeature(mockFeature())
    assert len(feature.userStories) == 2  # should return 2 instances of the mocked feature since the mocked feature has 2 user stories
    assert feature.userStories[0].title == "Some Story"
    assert feature.userStories[0].description == "Some Description"

def test_buildStory(fs):
    _mockCorrectFileSystem(fs)

    def mockParserJsonReturnUserStoryJson(*args, **kwargs):
        content = None
        with open('./correct/01_folder/02_folder/metadata.json', 'r') as reader:
            content = reader.read()
            reader.close()

        return json.loads(content)

    def mockBacklogBuildTaskReturnTask(*args, **kwargs):
        task = entities.Task()
        task.title = "Some Task"
        task.description = "Some Description"
        
        return task

    def mockUserStory(*args, **kwargs):
        return _mockParsedFileList()[0]["features"][0]["stories"][0]

    backlog = helpers.Backlog()

    backlog._getAndValidateJson = MagicMock(return_value=False)
    story = backlog._buildStory(mockUserStory())
    assert story == None

    backlog._getAndValidateJson = MagicMock(return_value=mockParserJsonReturnUserStoryJson())
    backlog._buildTask = MagicMock(return_value=None)
    story = backlog._buildStory(mockUserStory())
    assert story.title == "Foo bar"
    assert story.description == "Lorem Ipsum 01_folder/02_folder"
    assert len(story.tags) == 3
    assert _contains(story.tags, lambda tag: tag.title == "01_Folder") == True
    assert _contains(story.tags, lambda tag: tag.title == "02_Folder") == True
    assert _contains(story.tags, lambda tag: tag.title == "AppDev") == True
    assert len(story.tasks) == 0
    
    backlog._buildTask = MagicMock(return_value=mockBacklogBuildTaskReturnTask())
    story = backlog._buildStory(mockUserStory())
    print(mockUserStory())
    assert len(story.tasks) == 2  # should return 2 instances of the mocked story since the mocked story has 2 tasks
    assert story.tasks[0].title == "Some Task"
    assert story.tasks[0].description == "Some Description"

def test_buildTask(fs):
    _mockCorrectFileSystem(fs)

    def mockParserJsonReturnTaskJson(*args, **kwargs):
        content = None
        with open('./correct/01_folder/02_folder/metadata.json', 'r') as reader:
            content = reader.read()
            reader.close()

        return json.loads(content)

    def mockTask(*args, **kwargs):
        return _mockParsedFileList()[0]["features"][0]["stories"][0]["tasks"][0]

    backlog = helpers.Backlog()

    backlog._getAndValidateJson = MagicMock(return_value=False)
    task = backlog._buildTask(mockTask())
    assert task == None

    backlog._getAndValidateJson = MagicMock(return_value=mockParserJsonReturnTaskJson())
    task = backlog._buildTask(mockTask())
    assert task.title == "Foo bar"
    assert task.description == "Lorem Ipsum 01_folder/02_folder"
    assert len(task.tags) == 3
    assert _contains(task.tags, lambda tag: tag.title == "01_Folder") == True
    assert _contains(task.tags, lambda tag: tag.title == "02_Folder") == True
    assert _contains(task.tags, lambda tag: tag.title == "AppDev") == True

def test_generate():
    def mockGatherWorkItemsReturnFileList(*args, **kwargs):
        return _mockFileList()
    
    def mockParseWorkItemsReturnFileList(*args, **kwargs):
        return _mockParsedFileList()
    
    backlog = helpers.Backlog()
    backlog._gatherWorkItems = MagicMock(return_value=mockGatherWorkItemsReturnFileList())
    backlog._parseWorkItems = MagicMock(return_value=mockParseWorkItemsReturnFileList())
    backlog._buildWorkItems = MagicMock(return_value=None)
    backlog.generate('./path')

    backlog._gatherWorkItems.assert_called_with('./path')
    backlog._parseWorkItems.assert_called_with(mockGatherWorkItemsReturnFileList())
    backlog._buildWorkItems.assert_called_with(mockParseWorkItemsReturnFileList())
