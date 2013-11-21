#-*- coding: utf-8 -*-
import SOAPpy
import xml.etree.ElementTree as ET
"""
Module zur Umsetzung des Servers 
der Server verarbeitet die Anfragen des Clients je nach benötigter Methode
@author: Patrick Muehl, Nanak Tattyrek
"""
#Lesen der XML- Datei
tree = ET.parse('wissensdatenbank.xml')
#Das Root - Element heraussuchen
root = tree.getroot()
def search(suchwort):
    """
    Methode zum suchen in der geöffneten XML- Datei
    @param suchwort: der zu suchende Beitrag
    @return: Der Beitrag mit entfernten Leerzeichen 
    """
    for tags in root.findall('eintrag'):
        titel = tags.find('titel').text
        inhalt = tags.find('inhalt').text
        if titel.strip() == suchwort:
            return inhalt.strip()
        else:
            return "Kein Eintrag gefunden"
            
def insert(titel, inhalt, tag):
    """
    Funktion um Neue Inhalte in die XML- Datei einzufügen
    @param titel: Der Titel des Beitrages
    @param inhalt: Der Beitrag an sich 
    @param tag: Tag des Beitrages 
    @return: True wenn der Vorgang abgeschlossen wurde, False falls Probleme auftraten
    """
    a = ET.Element('eintrag')
    b = ET.SubElement(a, 'titel')
    b.text = titel
    c = ET.SubElement(a, 'inhalt')
    c.text= inhalt
    d = ET.SubElement(c, 'tags')
    d.text = tag
    root.append(a)
    tree.write('wissensdatenbank.xml', encoding='utf-8')
    return True
#definieren des Servers    
server = SOAPpy.SOAPServer(("localhost", 8080))
#Eintragen der Funktionen
server.registerFunction(search)
server.registerFunction(insert)
#Sagen wie lange der Server die Funktionen anbieten soll
server.serve_forever()

