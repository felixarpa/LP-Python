from ast import literal_eval
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--date")
parser.add_argument("--metro")
args = parser.parse_args()

def eval_dates(expr, pos):
    if pos >= len(expr):
        return ''.join(expr)
    if expr[pos] == '[' or expr[pos] == '(':    # [dd/mm/YYYY,...]
        expr.insert(pos + 1, '\"')              # [*dd/mm/YYYY,...]     * <<-- "
        expr.insert(pos + 12, '\"')             # ["dd/mm/YYYY*,...]    * <<-- "
        return eval_dates(expr, pos + 14)       # ["dd/mm/YYYY",*...]
    else:
        return eval_dates(expr, pos + 1)

def eval_metro(expr, pos):
    if pos >= len(expr):
        return ''.join(expr)
    if expr[pos] == '[' or expr[pos] == ',':
        expr.insert(pos + 1, '\"')
        expr.insert(pos + 4, '\"')
        return eval_metro(expr, pos + 5)
    else:
        return eval_metro(expr, pos + 1)

keys   = [] if args.key   == None else literal_eval(args.key)
dates  = [] if args.date  == None else literal_eval(eval_dates(list(args.date), 0))
metros = [] if args.metro == None else literal_eval(eval_metro(list(args.metro), 0))

print(keys)
print(dates)
print(metros)