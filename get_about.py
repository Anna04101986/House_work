import urls
from parser import Parser

class GetAbout:
    def __init__(self):
        self.for_man = []
        self.for_woman = []
        self.congr = ''


    def get_man(self, url: str):
        if not self.for_man:
            self.for_man = Parser.parser(url)
        congr = self.for_man.pop(0)
        amountM = len(self.for_man)
        print('for_man', congr)
        return congr, amountM

    def get_woman(self, url: str):
        if not self.for_woman:
            self.for_woman = Parser.parser(url)
        congr = self.for_woman.pop(0)
        amountW = len(self.for_woman)
        print(congr)
        return congr, amountW

