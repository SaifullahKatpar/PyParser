from Lexer import Lexer
from LexerError import LexerError
from SymbolTable import SymbolTable
from Token import Token
import pickle
rules = [
    ('//.*$',       'COMMENT'),
    ('int|float|long',  'DTYPE'),
    (';',   'DELIM'),
    (',',   'COMMA'),
    ('[_a-zA-Z][_a-zA-Z0-9]*',    'IDENTIFIER'),
    ('([0-9]*[.])?[0-9]+',             'NUMBER'),
    ('\+\+',              'INC'),
    ('\-\-',              'DEC'),
    ('\+',              'PLUS'),
    ('\-',              'MINUS'),
    ('\*',              'MULTIPLY'),
    ('\/',              'DIVIDE'),
    ('\(',              'LP'),
    ('\)',              'RP'),
    ('==',               'EQUAL'),
    ('=',               'ASSIGN'),
                    
]

lx = Lexer(rules, skip_whitespace=True)
inp = input('File name: ')
source = open(inp)
table = SymbolTable()

for line in source:
    lx.input(line)
    table.pos+=1
    try:
         for tok in lx.tokens():
            token = tok.getToken()
            table.insert(token)

    except LexerError as err:
         print('LexerError at position %s' % err.pos)

symbol_table = table.getTable()
with open('table.pickle', 'wb') as f:
	pickle.dump(symbol_table, f)

lexical_box = table.getLexicalBox()
output = open('output.txt','w')
for key,val in lexical_box.items():
    values = '<'+str(key[0])+','+str(key[1])+','+str(val)+'>'+' '
    output.write(values)
output.close()


