import pytest
from typing import *
from src.entities import Tag

def test_initTag():
    t = Tag()
    assert isinstance(t, Tag)

def test_setTitleToString():
    t = Tag()
    t.title = "Test"
    assert t.title == "Test"

def test_setTitleToNumber():
    t = Tag()

    with pytest.raises(TypeError) as exc:
        t.title = 42
    assert "value must be a string" in str(exc.value)
