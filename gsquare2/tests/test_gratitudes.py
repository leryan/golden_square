from lib.gratitudes import *

"""
Adding 1st name to gratitude class
"""
def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Ryan")
    result = gratitudes.format()
    assert result == "Be grateful for: Ryan"

"""
Adding 2nd name to gratitude class
"""

def test_sec_name():
    gratitudes = Gratitudes()
    gratitudes.add("Ryan")
    gratitudes.add("Chenny")
    result = gratitudes.format()
    assert result == "Be grateful for: Ryan, Chenny"