import pytest
from pyfakefs import fake_filesystem
import src.mbgenerate.helpers as helpers

def _mockCorrectFileSystem(fs):
    fs.create_file('./correct/01_folder/metadata.json')
    fs.create_file('./correct/01_folder/attachment.doc')
    fs.create_file('./correct/01_folder/01_folder/metadata.json')
    fs.create_file('./correct/01_folder/02_folder/metadata.json')
    fs.create_file('./correct/01_folder/03_folder/metadata.json')
    fs.create_file('./correct/01_folder/03_folder/attachment.doc')
    fs.create_file('./correct/02_folder/metadata.json')
    fs.create_file('./correct/02_folder/01_folder/metadata.json')
    fs.create_file('./correct/02_folder/02_folder/metadata.json')
    fs.create_file('./correct/03_folder/metadata.json')
    fs.create_file('./correct/03_folder/03_folder/metadata.json')

def _mockParentPathHasFileFileSystem(fs):
    fs.create_file('./parentPathHasFile/metadata.json')
    fs.create_file('./parentPathHasFile/01_folder/metadata.json')
    fs.create_file('./parentPathHasFile/01_folder/01_folder/metadata.json')

def _mockPathHasNoMetadataFileSystem(fs):
    fs.create_file('./pathHasNoMetadata/01_folder/01_folder/metadata.json')

def test_getFiles_CorrectFileSystem(fs):
    _mockCorrectFileSystem(fs)

    f = helpers.FileSystem()
    files = f.getFiles('./correct')
    assert len(files) == 9

def test_getFiles_ParentPathHasFileFileSystem(fs):
    _mockParentPathHasFileFileSystem(fs)

    f = helpers.FileSystem()
    with pytest.raises(FileExistsError) as exc:
        files = f.getFiles('./parentPathHasFile')
    assert "parent path should not contain any files" in str(exc.value)
    
def test_getFiles_PathHasNoMetadata(fs):
    _mockPathHasNoMetadataFileSystem(fs)

    f = helpers.FileSystem()
    with pytest.raises(FileNotFoundError) as exc:
        files = f.getFiles('./pathHasNoMetadata')
    assert "'metadata.json' does not exist in path './pathHasNoMetadata/01_folder'" in str(exc.value)

def test_readFile(fs):
    pass