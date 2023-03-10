import urllib.request

from bs4 import BeautifulSoup

pagina = open('index.html', 'w', encoding='UTF-8')
pagina.write("<!DOCTYPE html>\n")
pagina.write("<html lang='en'>\n")
pagina.write("<head>\n")
pagina.write("  <meta charset='UTF-8' />\n")
pagina.write("  <meta http-equiv='X-UA-Compatible' content='IE=edge' />\n")
pagina.write("  <meta name='viewport' content='width=device-width, initial-scale=1.0' />\n")
pagina.write("  <title>Atividade 5</title>\n")
pagina.write("</head>\n")
pagina.write("<body>\n")

with open('seeds.txt', 'r', encoding='UTF-8') as arquivo:
    seeds = arquivo.readlines()    
    
for link in seeds:
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(str(page.read().decode('utf-8')))

    pagina.write("  <p>"+soup.title.string+"</p>\n")
    for img in soup.find_all('img'):
        img = img.attrs.get("src")
        if "https://" in img:
            pagina.write("  <img width='500px' src='" + img + "'/>\n\n")
        else:
            pagina.write(f"  <img width='500px' src='{link[:-1]+img}'/>\n\n")
pagina.write("</body>\n")
pagina.write("</html>\n")
        