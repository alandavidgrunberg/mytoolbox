from mytoolbox.lib import sarcasticize, try_me

def test_try_me():
    assert type(try_me()) == str

def test_sarcasticize():
    assert len(sarcasticize('hello')) == len('hello')
