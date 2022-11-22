from lib.string_builder import *

"""
First output is empty string
"""

def test_string_empty():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""

"""
When output gets added, output => string
"""

def test_string_add():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hey")
    assert stringbuilder.output() == "Hey"

"""
When output gets added, output => string
"""

def test_string_len():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hey there")
    assert stringbuilder.size() == 9

"""
Multiple strings get added together
"""

def test_multistring_add():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hey")
    stringbuilder.add(" ")
    stringbuilder.add("there")
    assert stringbuilder.output() == "Hey there"

"""
Multiple strings sizes summed together
"""

def test_string_len():
    stringbuilder = StringBuilder()
    stringbuilder.add("Hey there,")
    stringbuilder.add("I'm Ryan")
    stringbuilder.add("nice to meet you")
    assert stringbuilder.size() == 34