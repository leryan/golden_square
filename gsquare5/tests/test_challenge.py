from lib.challenge import GrammarStats

"""
Return true if text has a capital letter and punctuation mark at the end
Result ~ 'Hello!' = True
"""

def test_text_has_caps_and_punc():
    sentence = GrammarStats('Hello!')
    result = sentence.check()
    assert result == True

"""
Return false if text missing a capital letter at the end
Result ~ 'hello!' = True
"""

def test_text_missing_caps():
    sentence = GrammarStats('hello!')
    result = sentence.check()
    assert result == False

"""
Return false if text missing a punctuation at the end
Result ~ 'Hello' = False
"""

def test_text_missing_punct():
    sentence = GrammarStats('Hello')
    result = sentence.check()
    assert result == False

"""
Return number of texts that have passed as a %
Result ~ 33.33%
"""

def test_percent_good():
    good = (True)
    result = good.percentage_good()
    assert result == '33%'