import src.mbgenerate.helpers as helpers

def test_validateMetadata():
    v = helpers.Validation()
    assert v.validateMetadata(None) == True

def test_validateTitle():
    v = helpers.Validation()
    assert v.validateTitle({}) == False
    assert v.validateTitle({ 'title' : ''}) == False
    assert v.validateTitle({ 'title' : 10}) == False
    assert v.validateTitle({ 'title' : '     '}) == False
    assert v.validateTitle({ 'title' : 'lorem ipsum'}) == True

def test_validateDescription():
    v = helpers.Validation()
    assert v.validateDescription({}) == False
    assert v.validateDescription({ 'description' : ''}) == False
    assert v.validateDescription({ 'description' : 10}) == False
    assert v.validateDescription({ 'description' : '     '}) == False
    assert v.validateDescription({ 'description' : 'lorem ipsum'}) == True

def test_validateTags():
    v = helpers.Validation()
    assert v.validateTags({})[0] == False
    assert v.validateTags({ 'tags' : 'lorem ipsum'}) == True

def test_validateRoles():
    v = helpers.Validation()
    assert v.validateRoles({})[0] == False
    assert v.validateRoles({ 'roles' : 'lorem ipsum'}) == True

