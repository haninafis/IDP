import idp_lexer
import idp_parser
import idp_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = idp_lexer.BasicLexer()
    parser = idp_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('IDP > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            idp_interpreter.BasicExecute(tree, env)
