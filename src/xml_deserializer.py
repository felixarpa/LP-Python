from acte import Acte
from address import Address
from coordinates import Coordinates
from metro import Metro
import datetime
import xml.etree.ElementTree as ET
from ast import literal_eval

address_path = "./lloc_simple/adreca_simple"

def text_str(text):
    return "" if text == None else text

def find_text(node, path):
    return text_str(node.find(path).text)

def find_attr(node, path, attr):
    return text_str(node.find(path).attrib[attr])

def deserialize_acte(xml):
    date = str(find_text(xml, "./data/data_proper_acte"))
    date_format = "%d/%m/%Y %H.%M"
    return Acte.Builder() \
        .name(find_text(xml, "./nom")) \
        .address(
            Address.Builder().name(find_text(xml, "./lloc_simple/nom")) \
            .street(find_text(xml, address_path + "/carrer")) \
            .number(find_text(xml, address_path + "/numero")) \
            .zip_code(find_text(xml, address_path + "/codi_postal")) \
            .district(find_text(xml, address_path + "/districte")) \
            .city(find_text(xml, address_path + "/municipi")) \
            .build()) \
        .coordinates(Coordinates.Builder()
            .lat(get_float(xml, "lat")) \
            .lon(get_float(xml, "lon")) \
            .build()) \
        .date(datetime.datetime.strptime(date, date_format)) \
        .build()

def deserialize_metro(xml):
    return Metro.Builder() \
        .name(find_text(xml, "./Tooltip")) \
        .lat(float(find_text(xml, "./Coord/Latitud"))) \
        .lon(float(find_text(xml, "./Coord/Longitud"))) \
        .build()

def get_float(xml, attrib):
    try:
        return float(xml.find(address_path + "/coordenades/googleMaps").attrib[attrib])
    except ValueError as err:
        return 0.0
