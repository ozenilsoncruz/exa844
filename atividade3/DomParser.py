from xml.dom.minidom import parse
from time import time

BancoDocument = parse('map.osm')

print("Starting DOM Parser...")

start = time()
for n in BancoDocument.getElementsByTagName("node"):
    for t in n.getElementsByTagName("tag"):
        if t.getAttribute("k") == 'amenity':
            print("Tipo: ", t.getAttribute("v"))
            for t2 in n.getElementsByTagName("tag"):
                if t2.getAttribute("k") == 'name':
                    print("Nome: ", t2.getAttribute("v"))
                    print("Lat:", n.getAttribute("lat"))
                    print("Log:", n.getAttribute("lon"), '\n') 

print("Tempo de execução: ", time() - start)