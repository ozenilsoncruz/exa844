import urllib.request

from bs4 import BeautifulSoup

with open('seeds.txt', 'r', encoding='UTF-8') as arquivo:
    seeds = arquivo.readlines()    
    
    
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<meta charset='UTF-8' />")
print(" <meta http-equiv='X-UA-Compatible' content='IE=edge' />")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0' />")
print("<title>Atividade 5</title>")
print("</head>")
print("<body>")

for link in seeds:
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(str(page.read().decode('utf-8')))

    print("<p>"+soup.title.string+"</p>")
    for img in soup.find_all('img'):
        img = img.attrs.get("src")
        if "https://" in img:
            print("<img width='500px' src='" + img + "'/>")
        else:
            print(f"<img width='500px' src='{link[:-1]+img}'/>")
        