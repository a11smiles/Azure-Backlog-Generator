from pyfakefs import fake_filesystem
import src.mbgenerate.helpers as helpers

def _mockCorrectFileSystem(fs):
    fs.create_file('./correct/metadata.json')
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

def test_getFiles(fs):
    _mockCorrectFileSystem(fs)

    f = helpers.FileSystem()
    files = f.getFiles('./correct')
    assert len(files) == 10