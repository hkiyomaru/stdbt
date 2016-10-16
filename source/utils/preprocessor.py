# -*- coding: utf-8 -*-
import re


class Preprocessor:
    def __init__(self):
        pass

    def __call__(self, string):
        # add space
        string += ' '
        # eliminate '@' pattern
        at_pattern = re.compile(u'@.*?\s|@.*?(?m)', re.S)
        string = at_pattern.sub('', string)
        # eliminate '#' pattern
        tag_pattern = re.compile(u'\#.*?\s|\#.*?(?m)', re.S)
        string = tag_pattern.sub('', string)
        # eliminate 'http' pattern
        string = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', '', string)
        # eliminate 'RT' pattern
        string = re.sub('RT', '', string)
        # eliminate symbol pattern
        symbol_pattern = re.compile(u'(?:\!|\?|\"|\'|\#|\$|\%|\&|\*|\(|\)|\`|\{|\}|\[|\]|\:|\;|\+|\/|\-|\=|\^|\~|\_|\\|\_|\>|\<|\,|\.|\|)')
        string = symbol_pattern.sub('', string)
        # eliminate \n \r
        string = re.sub(r'\n', '', string)
        string = re.sub(r'\r', '', string)
        alphabet_pattern = re.compile(u'[^a-zA-Z_\'\s]', re.I)
        string = alphabet_pattern.sub('', string)

        return string.lower()


if __name__ == "__main__":
    preprocessor = Preprocessor()
    string = "@xxx hi! I'm Hirokazu Kiyomaru! http://example.com #example1 #example2 #example3"
    print 'original:', string

    string = preprocessor(string)
    print 'output  :', string
