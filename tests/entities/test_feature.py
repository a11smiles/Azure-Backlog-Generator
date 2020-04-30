import pytest
from typing import *
from src.entities import Feature, UserStory, Tag

def test_initFeature():
    f = Feature()
    assert isinstance(f, Feature)
    assert isinstance(f.userStories, List)
    assert len(f.userStories) == 0
    assert isinstance(f.tags, List)
    assert len(f.tags) == 0

def test_setTitleToString():
    f = Feature()
    f.title = "Test"
    assert f.title == "Test"

def test_setTitleToNumber():
    f = Feature()

    with pytest.raises(TypeError) as exc:
        f.title = 42
    assert "value must be a string" in str(exc.value)

def test_setDescriptionToString():
    f = Feature()
    f.description = "Test"
    assert f.description == "Test"

def test_setDescriptionToNumber():
    f = Feature()

    with pytest.raises(TypeError) as exc:
        f.description = 42
    assert "value must be a string" in str(exc.value)

def test_addStoriesToUserStoryList():
    f = Feature()
    for r in range(5):
        s = UserStory()
        f.addUserStory(s)

    assert len(f.userStories) == 5
    assert isinstance(f.userStories, List)
    assert isinstance(f.userStories[0], UserStory)

def test_addGenericsToUserStoryList():
    f = Feature()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            f.addUserStory(r)
    assert "value must be of type 'UserStory'" in str(exc.value)

def test_addTagsToTagList():
    f = Feature()
    for r in range(5):
        t = Tag()
        f.addTag(t)

    assert len(f.tags) == 5
    assert isinstance(f.tags, List)
    assert isinstance(f.tags[0], Tag)

def test_addGenericsToTagList():
    f = Feature()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            f.addTag(r)
    assert "value must be of type 'Tag'" in str(exc.value)
