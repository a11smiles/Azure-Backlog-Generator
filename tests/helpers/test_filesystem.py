import src.helpers as helpers

def test_getFiles():
    f = helpers.FileSystem()
    files = f.getFiles('./tests/helpers/sample_path')
    assert len(files) == 11