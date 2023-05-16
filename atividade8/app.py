from flask import Flask, render_template, request, make_response, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__)
app.secret_key = 'testando123...'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)

@app.route('/', methods=['POST', 'GET'])
def counter():
    tempo = 0
    nome = ''
    if request.method == 'POST':
        nome = request.form['nome']  # pega o nome submetido no formulário
        session['nome'] = nome  # salva o nome na sessão
        session['tempo'] = datetime.now(timezone.utc)
        
    if 'nome' in session and 'tempo' in session:
        tempo = app.permanent_session_lifetime -  (datetime.now(timezone.utc) - session.get('tempo'))
        nome = session['nome']
        
        
    counter_value = request.args.get('counter', default=0, type=int) + 1 #pega o valor do hidden
    
    if 'contador_cookies' in request.cookies:
        count = int(request.cookies.get('contador_cookies'))
    else:
        count = 1
        
    resp = make_response(render_template('index.html', contador_cookies=count, contador_escondido=counter_value, nome=nome, tempo=tempo))
    resp.set_cookie('contador_cookies', str(count + 1).encode('utf-8'), max_age=timedelta(seconds=30)) # Incrementa o contador em cookies
    
    return resp


if __name__ == '__main__':
    app.run(port=8080, debug=True)
