from xml.dom.minidom import parse
from time import time
import json

BancoDocument = parse('map.osm')

print("Starting DOM Parser...\n")

geoJson = {
    "type": "FeatureCollection",
    "features": list()
}
        
start = time()
for n in BancoDocument.getElementsByTagName("node"):
    for t in n.getElementsByTagName("tag"):
        if t.getAttribute("k") == 'amenity':
            for t2 in n.getElementsByTagName("tag"):
                if t2.getAttribute("k") == 'name':
                    geoJson['features'].append(
                        {
                            "type": "Feature",
                            "geometry":
                            {
                                "type": "Point",
                                "coordinates": [
                                    float(n.getAttribute("lon")),
                                    float(n.getAttribute("lat"))
                                ]
                            },
                            "properties":
                                {
                                    "nome": t2.getAttribute("v"),
                                    "tipo": t.getAttribute("v"),
                                }
                        }
                    )

with open('geoJson.json', 'w') as arquivo:
    json.dump(geoJson, arquivo, indent=4)
    
print("Tempo de execução: ", time() - start)