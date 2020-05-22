import os
import pytest
from pyfakefs import fake_filesystem
from mocks import _mockCorrectFileSystem, _mockParentPathHasFileFileSystem, _mockPathHasNoMetadataFileSystem
import src.azbacklog.helpers as helpers


def test_getFiles_CorrectFileSystem(fs):
    _mockCorrectFileSystem(fs)

    f = helpers.FileSystem()
    files = f.getFiles('./correct')
    assert len(files) == 9


def test_getFiles_ParentPathHasFileFileSystem(fs):
    _mockParentPathHasFileFileSystem(fs)

    f = helpers.FileSystem()
    with pytest.raises(FileExistsError) as exc:
        files = f.getFiles('./parentPathHasFile')  # NOQA
    assert "parent path should not contain any files" in str(exc.value)


def test_getFiles_PathHasNoMetadata(fs):
    _mockPathHasNoMetadataFileSystem(fs)

    f = helpers.FileSystem()
    with pytest.raises(FileNotFoundError) as exc:
        files = f.getFiles('./pathHasNoMetadata')  # NOQA
    assert "'metadata.json' does not exist in path './pathHasNoMetadata/01_folder'" in str(exc.value)


def test_readFile(fs):
    testContent = '{ "foo": "bar" }'
    fs.create_file('./testFilePath/testfile.json', contents=testContent)

    f = helpers.FileSystem()
    readContent = f.readFile('./testFilePath/testfile.json')

    assert readContent == testContent

    with pytest.raises(FileNotFoundError) as exc:
        content = f.readFile('./testFilePath/notexist.json')  # NOQA
    assert "'./testFilePath/notexist.json' does not exist" in str(exc.value)
