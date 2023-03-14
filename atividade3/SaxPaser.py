import xml.sax
from time import time

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.lat_prov = ""
    self.lon_prov = ""
    self.lat = ""
    self.lon = ""
    self.tipo = ""
    self.nome = ""

  def startElement(self, tag, attributes):    
    self.currentData = ""
    
    if tag == "node":
      self.lat_prov = attributes.get("lat")  
      self.lon_prov = attributes.get("lon")
    if tag == "tag":
      if attributes.get("k") == 'amenity':
        self.tipo =  attributes.get("v")
        self.lat = self.lat_prov
        self.lon = self.lon_prov
      elif attributes.get("k") == 'name':
        self.nome =  attributes.get("v")

  def endElement(self, tag):    
    if tag == "node" and self.tipo != '' and self.nome != '' and self.lat != '' and self.lon != '':	
      print("\nTipo:", self.tipo) 
      print("Nome:", self.nome) 
      print("Lat:", self.lat) 
      print("Lon:", self.lon)
      self.tipo = ''

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")

start = time()
parser.parse("map.osm")
print("\nTempo de execução: ", time() - start)