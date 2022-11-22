from lib.check_codeword import check_codeword

def test_check ():

    """
If codeword is correct
Returns 'Correct! Come in'
"""

def test_correct_codeword ():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

"""
If codeword is wrong
Returns 'Wrong!'
"""

def test_wrong_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

"""
If codeword has correct first and last letter
Returns 'Close, but nope'
"""

def test_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

"""
If codeword has wrong first and right last letter
Returns 'Wrong!'
"""

def test_wrongfirst ():
    result = check_codeword("mouse")
    assert result == "WRONG!"

"""
If codeword has right first and wrong last letter
Returns 'Wrong!'
"""

def test_wrongsec ():
    result = check_codeword("hat")
    assert result == "WRONG!"