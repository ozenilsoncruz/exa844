#!/usr/bin/env python
import cgi
import cgitb
import os
import datetime

# Define o local do arquivo de mensagens
MESSAGE_FILE = "mensagens.txt"

# Habilita a exibição de informações de depuração em caso de erros
cgitb.enable()

# Define o cabeçalho HTTP para exibir uma página HTML
print("Content-Type: text/html\n\n")

# Processa os dados enviados pelo formulário
form = cgi.FieldStorage()
autor = form.getvalue("autor")
mensagem = form.getvalue("mensagem")

# Se o autor e a mensagem forem definidos, armazena-os no arquivo de mensagens
if autor and mensagem:
    with open(MESSAGE_FILE, "a") as f:
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{data} - {autor}: {mensagem}\n")

# Exibe o formulário de envio de mensagens
print("""
<html>
    <head>
    <meta charset="utf-8">
    <title>Blog</title>
  </head>
  <body>
    <h1>Blog</h1>
    <div style="display: flex; justify-content: center;">
        <form method="post" action="msg.py">
            <label for="autor">Autor:</label>
            <input type="text" id="autor" name="autor"><br>
            
            <label for="mensagem">Mensagem:</label><br>
            <textarea id="mensagem" name="mensagem"></textarea><br>
            <input type="submit" value="Enviar">
          </form>
    </div>
   
    <h2>Mensagens</h2>
""")

lista = []
# Exibe as mensagens armazenadas no arquivo de mensagens
if os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, "r") as f:
        for linha in reversed(list(f)):
            print(f"<p>{linha.strip()}</p>")

print("""
  </body>
</html>
""")
