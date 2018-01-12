#!/usr/bin/python3

import urllib.request
import xml.etree.ElementTree as ET

EVENTS_URL = "http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=203"
METRO_URL = "http://opendata-ajuntament.barcelona.cat/resources/bcn/TRANSPORTS%20GEOXML.xml"

def get_xml(url):
    sock = urllib.request.urlopen(url)
    xmlSource = sock.read()
    sock.close()
    return xmlSource

def get_actes_as_xml():
    root = ET.fromstring(get_xml(EVENTS_URL))
    return root.find('body').find('resultat').find('actes')