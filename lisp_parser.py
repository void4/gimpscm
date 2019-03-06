#!/usr/bin/python

# turn lisp statements into an AST

# going off a super basic grammar:
# - atoms are numbers or symbols

from string import whitespace

Number = (int, float)
Symbol = str
Atom = (Number, Symbol)

def parse(program):
  # lex
  tokens = tokenize(program)
  # and parse
  #print(tokens)
  ast = build_ast(tokens)
  return ast

def tokenize(program):
  "turn a string into a series of tokens"
  #return program.replace('(', ' ( ').replace(')', ' ) ').split()
  l = []
  isstr = False
  word = ""


  for i,c in enumerate(program):
    if c in "()":
      if not isstr:
          l.append(c)
      else:
          word += c
    elif c in whitespace:
      if isstr:
        word += c
      else:
        if word or isstr:
          l.append(word)
          word = ""
    elif c == '"':
      if program[i-1] == "\\":
        word += c
      else:
        if isstr:
            l.append(word)
            word = ""
        isstr = not isstr
    else:
      word += c

  return l

def build_ast(tokens):
  "build an expression from lexed tokens"
  ast = []
  if len(tokens) == 0:
    raise SyntaxError('unexpected EOF while reading string')

  tok = tokens.pop(0)
  if tok == '(':
    subtree = []
    while tokens[0] != ')': # peek to see if we've hit the end of the expression
      subtree.append(build_ast(tokens))
    tokens.pop(0) # pop off the ')'
    return subtree
  elif tok == ')':
    # hit the end of an expression without an (
    raise SyntaxError('unexpected ) while reading string')

  else:
    return atom(tok)


def atom(token):
  try:
    return int(token)
  except ValueError:
    try:
      return float(token)
    except ValueError:
      if token.startswith('"') and token.endswith('"'):
        token = token[1:-1]
      return Symbol(token)
