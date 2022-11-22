from lib.report_length import report_length

def test_length ():
    result = report_length("This is banana's!")
    assert result == "This string was 17 characters long."