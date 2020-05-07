import src.mbgenerate.helpers as helpers

def _mockFileList():
    files = [
        './correct/01_epic/metadata.json',
        './correct/01_epic/01_feature/metadata.json',
        './correct/01_epic/01_feature/01_story/metadata.json',
        './correct/01_epic/01_feature/01_story/01_task/metadata.json',
        './correct/01_epic/01_feature/01_story/02_task/metadata.json',
        './correct/01_epic/01_feature/02_story/metadata.json',
        './correct/01_epic/01_feature/02_story/01_task/metadata.json',
        './correct/01_epic/02_feature/metadata.json',
        './correct/01_epic/03_feature/metadata.json',
        './correct/02_epic/metadata.json',
        './correct/02_epic/01_feature/metadata.json',
        './correct/02_epic/01_feature/01_story/metadata.json',
        './correct/02_epic/01_feature/01_story/01_task/metadata.json',
        './correct/02_epic/01_feature/01_story/02_task/metadata.json',
        './correct/02_epic/01_feature/02_story/metadata.json',
        './correct/02_epic/01_feature/02_story/01_task/metadata.json',
        './correct/02_epic/02_feature/metadata.json',
        './correct/03_epic/metadata.json',
        './correct/03_epic/01_feature/metadata.json'
    ]
    
    return files

def _mockParsedFileList():
    result = [
        {
            'epic' : './correct/01_epic/metadata.json',
            'features' : [
                {
                    'feature' : './correct/01_epic/01_feature/metadata.json',
                    'stories' : [
                        {
                            'story' : './correct/01_epic/01_feature/01_story/metadata.json',
                            'tasks' : [
                                { 'task' : './correct/01_epic/01_feature/01_story/01_task/metadata.json' },
                                { 'task' : './correct/01_epic/01_feature/01_story/02_task/metadata.json' }
                            ]
                        },
                        {
                            'story' : './correct/01_epic/01_feature/02_story/metadata.json',
                            'tasks' : [
                                { 'task' : './correct/01_epic/01_feature/02_story/01_task/metadata.json' }
                            ]
                        }
                    ]
                },
                { 'feature' : './correct/01_epic/02_feature/metadata.json' },
                { 'feature' : './correct/01_epic/03_feature/metadata.json' }
            ]
        },
        {
            'epic' : './correct/02_epic/metadata.json',
            'features' : [
                {
                    'feature' : './correct/02_epic/01_feature/metadata.json',
                    'stories' : [
                        {
                            'story' : './correct/02_epic/01_feature/01_story/metadata.json',
                            'tasks' : [
                                { 'task' : './correct/02_epic/01_feature/01_story/01_task/metadata.json' },
                                { 'task' : './correct/02_epic/01_feature/01_story/02_task/metadata.json' }
                            ]
                        },
                        {
                            'story' : './correct/02_epic/01_feature/02_story/metadata.json',
                            'tasks' : [
                                { 'task' : './correct/02_epic/01_feature/02_story/01_task/metadata.json' }
                            ]
                        }
                    ]
                },
                {
                    'feature' : './correct/02_epic/02_feature/metadata.json'
                }
            ]
        },
        {
            'epic' : './correct/03_epic/metadata.json',
            'features' : [
                { 'feature' : './correct/03_epic/01_feature/metadata.json' }
            ]
        }
    ]
    
    return result

def test_parse():
    p = helpers.Parser()
    assert p.links('This is a sample [link](http://google.com).') == 'This is a sample <a href="http://google.com">link</a>.'

def test_json():
    p = helpers.Parser()
    assert p.json('{}') == {}
    assert p.json('{ "test" : "" } ') == { "test" : "" }
    assert p.json('{ "test" : "lorem ipsum" } ') == { "test" : "lorem ipsum" }
    assert p.json('{ ')[0] == False
    assert len(p.json('{ ')[1]) == 1
    assert ("Expecting property name enclosed in double quotes" in p.json('{ ')[1][0]) == True

def test_validString():
    p = helpers.Parser()
    assert p.validString(None) == False
    assert p.validString("") == False
    assert p.validString(10) == False
    assert p.validString("     ") == False

def test_fileHierarchy():
    p = helpers.Parser()
    parsedFiles = p.fileHierarchy(_mockFileList())

    assert parsedFiles == _mockParsedFileList()

    