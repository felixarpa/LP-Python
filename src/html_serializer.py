import datetime

def serialize_acte(acte):
    html = "<h2>" + acte.name + "</h2>\n"
    html += serialize_address(acte.address)
    html += serialize_time(acte.date.strftime("%d/%m/%Y %H.%M"))
    html += serialzie_train_stations(acte.train_stations)
    return html

def serialize_address(address):
    return "<p><em>" + address.name + "</em>: " + address.street + ", " \
            + address.number + ", " + address.zip_code + ", " \
            + address.district + ", " + address.city + "</p>\n"

def serialize_time(time):
    return "<p style=\"font-size:12px;color:#444\"><b>" + time + "</b></p>\n"

def serialzie_train_stations(train_stations):
    html = "<div style=\"margin-top:16px\">\n"
    for t in train_stations:
        html += "<p><b>" + t[0].line + "</b> | " + t[0].stop + "</p>\n"
    html += "</div>\n"
    return html

def serialize_actes(actes):
    html = "<div>"
    for acte in actes:
        html += serialize_acte(acte)
    html += "</div>"
    return html

def write_html(actes):
    file = open("index.html", "w")
    file.write("""<!DOCTYPE html>
<html>
    <head>
        <title>LP-Python</title>
        <meta charset="UTF-8" />
        <style>
            html { font-family: "HelveticaNeue-Light"; font-weight: 300; }
            div { margin-bottom:64px; margin-left:64px; margin-right:64px }
            h1 { font-size:32px; font-weight: bold; color:#444; }
            h2 { font-size:20px; color:#000; }
            p { font-size:16px; margin-top:8px; margin-bottom:8px }
            a { text-decoration: none; }
        </style>
    </head>
    <body>
    <div></div>
    <div style=\"margin-left:128px\"><a href="https://github.com/felixarpa/LP-Python/"><h1>Pràctica 3 de Llenguatges de Programació: Python</h1></a></div>
    <div></div>""")
    file.write(serialize_actes(actes))
    file.write("""
    </body>
</html>""")

