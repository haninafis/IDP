import idp_lexer
import idp_parser
import idp_interpreter

from sys import *


lexer = idp_lexer.BasicLexer()
parser = idp_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    idp_interpreter.BasicExecute(tree, env)
