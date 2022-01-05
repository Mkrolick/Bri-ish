# -*- coding: utf-8 -*-
# Esolang compiler or something
# compiler yoinked from bonerplusplus

# read the input file (extension is '.british')

import sys

filename = sys.argv[1]

f = open(filename + '.british', 'r')

code = f.read()

# dictionary of words to be swapped

swap = {
            "for'nit" : 'for',
            "wh'le'nit" : 'while',
            "'nit" : 'in',
            "if'nit" : 'if',
            "else'nit" : 'else',
            "elif'nit" : 'elif',
            "try'nit" : 'try',
            "except'nit" : 'except',
            "break'nit" : 'break',
            "continue'nit" : 'continue',
            "input'nit" : 'input',
            "classy'nit" : 'class',
            "def'nit" : 'def',
            "return'nit" : 'return',
            "minus'nit" : '-',
            "plus'nit" : '+', 
            "modden'nit" : '%',
            "doubl'y equal'nit" : '==',
            " equal'nit " : ' = ',
            " less than'nit " : ' < ',
            " greater than'nit " : ' > ',
            " greater than or equal to'nit " : '<=',
            " less than or equal to'nit " : '>=',
            "and'nit" : 'and',
            "or'nit" : 'or',
            "is'nit" : 'is',
            "not'nit" : 'not',
            "import'n it" : 'import',
            "from'nit" : 'from',
            "as'nit" : 'as',
            "with'nit" : 'with',
            "True'nit" : 'True',
            "False'nit" : 'False',
            "None'nit" : 'None',
            "Delete'nit" : 'del',
            "Pri'nt" : 'print',
            "yield'nit" : 'yield',
            "lambda'nit" : 'lambda',
            "rais'nt" : 'raise',
            "pass'nit" : 'pass',
            "nonlocal'nit" : 'nonlocal', 
            "global'nit" : 'global',
            "finally'nit" : 'finally',
            "await'nit" : 'await',
            "assert'nit" : 'assert',
            "async'nit" : 'async',
            "dict'nit" : 'dict',
            "string'nit" : 'str',
            "int'nit" : 'int',
            "double'nit" : 'double',
            "float'nit" : 'float',
            "chr'nit" : 'chr',
            "map'nit" : 'map',
            "set'nit" : 'set',
            "max'nit" : 'max',
            "min'nit" : 'min',
            "range'nit" : 'range',
            "round'nit" : 'round',
            "sum'nit" : 'sum',
            "super'nit" : 'super',
            "tuple'nit" : 'tuple',
            "zipin'nit" : 'zip',
            "type'nit" : 'type',
            "len'it" : 'len',
            "list'nit" : 'list',
            "open'nit" : 'open',
            "join'nit" : 'join',
            "file'nit" : 'file',
            "split'nit" : 'split',
            "append'nit" : 'append',
            "run'it" : 'run',
            "message'nit" : 'message',
            "event'nit" : 'event'
}

new = code

for item in swap: new = new.replace(item, swap[item])

# now we just have regular python code

exec('# -*- coding: utf-8 -*-\n' + new)
