import xml.etree.ElementTree as ET

tree = ET.parse('data/estudiantes.xml')
root = tree.getroot()

file = open('output/estudiantes.html', 'w')
document = ''
document += '<html>'
document += '<body>'
document += '<ul>'

for elemento in root:
    document += "<li>" + elemento.attrib['nombre'] + "</li>"

document += '</ul>'
document += '</body>'
document += '</html>'
file.write(document)
