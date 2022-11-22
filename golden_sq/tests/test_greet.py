from lib.greet import greet

def test_ret_name():
    result = greet("Ryan")
    assert result == "Hello, Ryan!"