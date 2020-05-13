import src.azbacklog.helpers as helpers

def test_validateMetadata():
    v = helpers.Validation()
    assert v.validateMetadata(None) == False
    assert v.validateMetadata({ 
        'description': 'lorem desc',
        'tags': 'lorem tags',
        'roles': []
    }) == False
    assert v.validateMetadata({ 
        'title' : 'lorem ipsum', 
        'tags': 'lorem tags',
        'roles': []
    }) == False
    assert v.validateMetadata({ 
        'title' : 'lorem ipsum', 
        'description': 'lorem desc',
        'roles': []
    }) == False
    assert v.validateMetadata({ 
        'title' : 'lorem ipsum', 
        'description': 'lorem desc',
        'tags': 'lorem tags'
    }) == False
    assert v.validateMetadata({ 
        'title' : 'lorem ipsum', 
        'description': 'lorem desc',
        'tags': 'lorem tags',
        'roles': []
    }) == True

def test_validateTitle():
    v = helpers.Validation()
    assert v._validateTitle({}) == False
    assert v._validateTitle({ 'title' : ''}) == False
    assert v._validateTitle({ 'title' : 10}) == False
    assert v._validateTitle({ 'title' : '     '}) == False
    assert v._validateTitle({ 'title' : 'lorem ipsum'}) == True

def test_validateDescription():
    v = helpers.Validation()
    assert v._validateDescription({}) == False
    assert v._validateDescription({ 'description' : ''}) == False
    assert v._validateDescription({ 'description' : 10}) == False
    assert v._validateDescription({ 'description' : '     '}) == False
    assert v._validateDescription({ 'description' : 'lorem ipsum'}) == True

def test_validateTags():
    v = helpers.Validation()
    assert v._validateTags({})[0] == False
    assert v._validateTags({ 'tags' : 'lorem ipsum'}) == True

def test_validateRoles():
    v = helpers.Validation()
    assert v._validateRoles({})[0] == False
    assert v._validateRoles({ 'roles' : 'lorem ipsum'}) == True

