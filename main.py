from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
    return ("""add a /{game name} to the url to play that dos game
    
    right now supported games include:
    doom
    doom2
    wolfenstein

    planned for later implementation:
    castlevania
    quake

    """)

@app.route('/castlevania')
def castlevania():
    return render_template('castlevania.html')

#@app.route('/daggerfall')
#def daggerfall():
#    return render_template('daggerfall.html')

@app.route('/doom')
def doom():
  return render_template('index.html')

@app.route('/doom2')
def doom2():
    return render_template('doom2.html')

@app.route('/quake')
def quake():
    return render_template('quake.html')

@app.route('/wolfenstein')
def Wolf3D():
    return render_template('wolf.html')

@app.route('/in-dev')
def beta_world():
  return render_template('index[beta].html')

app.run(host = '0.0.0.0')