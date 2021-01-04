import sys
import ply.lex as lex
import ply.yacc as yacc
import math

tokens = ('NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN','SUT','POW','FOR','MODULO')

t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_EQUALS   = r'='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_SUT      = r'\*\*'
t_NAME     = r'[a-zA-Z][a-zA-Z0-9]*'
t_POW      = r'\^'
t_FOR      = r'for'
t_MODULO   = r'%'



def p_expression_binop(p):
    '''expression : expression PLUS expression
                          | expression MINUS expression
                          | expression TIMES expression
                          | expression DIVIDE expression
                          | expression MODULO expression
                          | expression POW expression
                          | expression SUT expression'''
    if p[2] == '+'  :
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = math.pow(p[1] , p[3])
    elif p[2] == '**':
        p[0] = math.pow(p[1] , 1 / p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]



def p_error(p):
    print("Syntax error in input!")
    
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break 
    if not s: continue
    result = parser.parse(s)
    print(result)
