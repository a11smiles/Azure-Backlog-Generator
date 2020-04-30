import pytest
from typing import *
from src.entities import Epic, Feature

def test_initEpic():
    e = Epic()
    assert isinstance(e, Epic)
    assert isinstance(e.features, List)
    assert len(e.features) == 0

def test_setTitleToString():
    e = Epic()
    e.title = "Test"
    assert e.title == "Test"

def test_setTitleToNumber():
    e = Epic()

    with pytest.raises(TypeError) as exc:
        e.title = 42
    assert "value must be a string" in str(exc.value)

def test_setFeaturesToFeatureList():
    e = Epic()
    for r in range(5):
        f = Feature()
        e.addFeature(f)

    assert len(e.features) == 5
    assert isinstance(e.features, List)
    assert isinstance(e.features[0], Feature)

def test_setFeaturesToGenericList():
    e = Epic()
    with pytest.raises(TypeError) as exc:
        for r in range(5):
            e.addFeature(r)
    assert "value must be of type 'Feature'" in str(exc.value)

