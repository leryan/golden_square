from lib.counter import Counter

def test_show_zero():
    counter = Counter()
    assert counter.report()=="Counted to 0 so far."
