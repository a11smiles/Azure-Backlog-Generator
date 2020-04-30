from src.helpers import FileSystem

def test_getFiles():
    f = FileSystem()
    files = f.getFiles('./tests/helpers/sample_path')
    assert len(files) == 11