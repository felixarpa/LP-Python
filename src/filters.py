import re
import datetime

def filter_by_key(expr, acte):
    if isinstance(expr, type(None)):
        return True
    elif isinstance(expr, list):
        return any(filter_by_key(e, acte) for e in expr)
    elif isinstance(expr, tuple):
        return all(filter_by_key(e, acte) for e in expr)
    elif isinstance(expr, str):
        is_in = lambda text: re.search(expr, text, re.IGNORECASE)
        return is_in(acte.name) or is_in(acte.address.name) or is_in(acte.address.district)

def filter_by_date(expr, acte):
    if isinstance(expr, type(None)):
        return True
    elif isinstance(expr, list):
        return any(filter_by_date(e, acte) for e in expr)
    elif isinstance(expr, tuple):
        date = datetime.datetime.strptime(expr[0], "%d/%m/%Y")
        min_date = date - datetime.timedelta(days = abs(expr[1]))
        max_date = date + datetime.timedelta(days = expr[2])
        return acte.date <= max_date and acte.date >= min_date
    elif isinstance(expr, str):
        min_date = datetime.datetime.strptime(expr + " 00.00", "%d/%m/%Y %H.%M")
        max_date = datetime.datetime.strptime(expr + " 23.59", "%d/%m/%Y %H.%M")
        return acte.date <= max_date and acte.date >= min_date

def filter_by_metro(expr, metro):
    if isinstance(expr, type(None)):
        return True
    elif isinstance(expr, list):
        return any(filter_by_metro(e, metro) for e in expr)
    elif isinstance(expr, tuple):
        return all(filter_by_metro(e, metro) for e in expr)
    elif isinstance(expr, str):
        is_in = lambda text: re.search(expr, text, re.IGNORECASE)
        return is_in(metro.name)