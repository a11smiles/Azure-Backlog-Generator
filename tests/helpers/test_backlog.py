import pytest
from pyfakefs import fake_filesystem
from mocks import _mockCorrectFileSystem, _mockParentPathHasFileFileSystem, _mockPathHasNoMetadataFileSystem
import src.mbgenerate.helpers as helpers
import src.mbgenerate.entities as entities

def test_gatherWorkItems(fs):
    pass

def test_parseWorkItems(fs):
    pass

def test_getAndValidateJson(fs):
    pass

def test_buildWorkItems(fs):
    pass

def test_createTag(fs):
    backlog = helpers.Backlog()
    tag = backlog._createTag("foo bar")

    assert isinstance(tag, entities.Tag) == True
    assert tag.title == "foo bar"

def test_buildEpic(fs):
    pass

def test_buildFeature(fs):
    pass

def test_buildStory(fs):
    pass

def test_buildTask(fs):
    pass

def test_generate(fs):
    pass