def _mockCorrectFileSystem(fs):
    fs.create_file('./correct/01_folder/metadata.json', 
        contents = '{ \
                      \
                    }')
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