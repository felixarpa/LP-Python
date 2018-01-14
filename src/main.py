import xml_deserializer
import html_serializer
import urllib.request
import xml.etree.ElementTree as ET
import argparse
from ast import literal_eval
from filters import filter_by_key, filter_by_date, filter_by_metro


################
# ARGS PARSING #
################

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--date")
parser.add_argument("--metro")
args = parser.parse_args()

def eval_dates(expr, pos):
    if len(expr) == 10:                         # és només un valor
        expr.insert(0, '\"')
        expr.insert(11, '\"')
        return ''.join(expr)
    if pos >= len(expr):
        return ''.join(expr)
    if expr[pos] == '[' or expr[pos] == '(':    # [dd/mm/YYYY,...]
        expr.insert(pos + 1, '\"')              # [*dd/mm/YYYY,...]     * <<-- "
        expr.insert(pos + 12, '\"')             # ["dd/mm/YYYY*,...]    * <<-- "
        return eval_dates(expr, pos + 14)       # ["dd/mm/YYYY",*...]
    else:
        return eval_dates(expr, pos + 1)

def eval_metro(expr, pos):
    if len(expr) == 2:
        expr.insert(0, '\"')
        expr.insert(3, '\"')
        return ''.join(expr)
    if pos >= len(expr):
        return ''.join(expr)
    if expr[pos] == '[' or expr[pos] == ',':
        expr.insert(pos + 1, '\"')
        expr.insert(pos + 4, '\"')
        return eval_metro(expr, pos + 5)
    else:
        return eval_metro(expr, pos + 1)

keys   = None if args.key   == None else literal_eval(args.key)
dates  = None if args.date  == None else literal_eval(eval_dates(list(args.date), 0))
metros = None if args.metro == None else literal_eval(eval_metro(list(args.metro), 0))


###################
# DATA COLLECTION #
###################

EVENTS_URL = "http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=199"
METRO_URL = "http://opendata-ajuntament.barcelona.cat/resources/bcn/TRANSPORTS%20GEOXML.xml"

def get_xml(url):
    sock = urllib.request.urlopen(url)
    xml = ET.fromstring(sock.read())
    sock.close()
    return xml

actes_xml = get_xml(EVENTS_URL)
actes = [ a for a in map(xml_deserializer.deserialize_acte, actes_xml.iter("acte")) ]
metro_xml = get_xml(METRO_URL)
metro_st = [ a for a in map(xml_deserializer.deserialize_metro, metro_xml.iter("Punt")) ]


#############
# FILTERING #
#############

arg_filter = lambda acta: filter_by_key(keys, acta) and filter_by_date(dates, acta)
metro_filter = lambda metro: filter_by_metro(metros, metro)

filtered_data =     [ a for a in actes    if arg_filter(a) ] #filter(arg_filter, actes)
filtered_stations = [ m for m in metro_st if metro_filter(m) ]


##############
# CONCORDING #
##############

for a in filtered_data:
    for m in filtered_stations:
        a.add_train_station(m)


##############
# PRINT HTML #
##############
html_serializer.write_html(filtered_data)
#print(html_serializer.serialize_actes(filtered_data))





