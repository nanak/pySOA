import SOAPpy
import xml.etree.ElementTree as ET


tree = ET.parse('wissensdatenbank.xml')
root = tree.getroot()
def search(suchwort):
    for tags in root.findall('eintrag'):
        titel = tags.find('titel').text
        inhalt = tags.find('inhalt').text
        if titel.strip() == suchwort:
            return inhalt.strip()
        else:
            return "Kein Eintrag gefunden"
            
def insert(element, inhalt):
    return ""    
    
server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(search)
server.serve_forever()

