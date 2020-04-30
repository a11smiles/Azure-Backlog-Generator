import pytest
from typing import *
from src.entities import Task, Tag

def test_initEpic():
    task = Task()
    assert isinstance(task, Task)
    assert isinstance(task.tags, List)
    assert len(task.tags) == 0

def test_setTitleToString():
    task = Task()
    task.title = "Test"
    assert task.title == "Test"

def test_setTitleToNumber():
    task = Task()

    with pytest.raises(TypeError) as exc:
        task.title = 42
    assert "value must be a string" in str(exc.value)

def test_setDescriptionToString():
    task = Task()
    task.description = "Test"
    assert task.description == "Test"

def test_setDescriptionToNumber():
    task = Task()

    with pytest.raises(TypeError) as exc:
        task.description = 42
    assert "value must be a string" in str(exc.value)

def test_addTagsToTagList():
    task = Task()
    for r in range(5):
        t = Tag()
        task.addTag(t)

    assert len(task.tags) == 5
    assert isinstance(task.tags, List)
    assert isinstance(task.tags[0], Tag)

def test_addGenericsToTagList():
    task = Task()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            task.addTag(r)
    assert "value must be of type 'Tag'" in str(exc.value)
