import pytest
from typing import *
from src.entities import Epic, Feature, Tag

def test_initEpic():
    e = Epic()
    assert isinstance(e, Epic)
    assert isinstance(e.features, List)
    assert len(e.features) == 0
    assert isinstance(e.tags, List)
    assert len(e.tags) == 0

def test_setTitleToString():
    e = Epic()
    e.title = "Test"
    assert e.title == "Test"

def test_setTitleToNumber():
    e = Epic()

    with pytest.raises(TypeError) as exc:
        e.title = 42
    assert "value must be a string" in str(exc.value)

def test_setDescriptionToString():
    e = Epic()
    e.description = "Test"
    assert e.description == "Test"

def test_setDescriptionToNumber():
    e = Epic()

    with pytest.raises(TypeError) as exc:
        e.description = 42
    assert "value must be a string" in str(exc.value)

def test_addFeaturesToFeatureList():
    e = Epic()
    for r in range(5):
        f = Feature()
        e.addFeature(f)

    assert len(e.features) == 5
    assert isinstance(e.features, List)
    assert isinstance(e.features[0], Feature)

def test_addGenericsToFeatureList():
    e = Epic()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            e.addFeature(r)
    assert "value must be of type 'Feature'" in str(exc.value)

def test_addTagsToTagList():
    e = Epic()
    for r in range(5):
        t = Tag()
        e.addTag(t)

    assert len(e.tags) == 5
    assert isinstance(e.tags, List)
    assert isinstance(e.tags[0], Tag)

def test_addGenericsToTagList():
    e = Epic()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            e.addTag(r)
    assert "value must be of type 'Tag'" in str(exc.value)
