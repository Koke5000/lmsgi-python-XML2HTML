# libreria para leer XML
import xml.etree.ElementTree as ET

# tomamos el arbol de elementos del XML
tree = ET.parse('data/estudiantes.xml')

# accedemos a la raiz
root = tree.getroot()

# imprimimos todo el documento
print("Documento XML:")
print(root)

# recorremos los elementos que "cuelgan" del elemento raiz
print('Elementos que "cuelgan" de la raiz')
for elemento in root:
    # accedemos directamente al atributo que queremos
    print(elemento.attrib['nombre'])
