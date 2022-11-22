import string

class GrammarStats:
    def __init__(self, text):
        self.text = text
    
    def check(self):
        if self.text[-1] == '!' and self.text[0].isupper():
            return True
        elif self.text[-1] == '?' and self.text[0].isupper():
            return True
        elif self.text[-1] == '.' and self.text[0].isupper():
            return True
        else:
            return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        # pass

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass