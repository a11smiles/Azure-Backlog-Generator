import src.mbgenerate.helpers as helpers

def test_parse():
    p = helpers.Parser()
    assert p.links('This is a sample [link](http://google.com).') == 'This is a sample <a href="http://google.com">link</a>.'