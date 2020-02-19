from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
    return ("""add a /{game name} to the url to play that dos game
    
    right now supported games include:
    doom
    doom2
    dosbox
    wolfenstein
    castlevania
    prince of persia

    planned for later implementation:
    elderscrolls arena
    elderscrolls daggerfall 



    news:
    new additions to dospy include fixed images in css, added support for raw dosbox, and fixed some broken games

    """)

@app.route('/castlevania')
def castlevania():
    return render_template('castlevania.html')

#@app.route('/daggerfall')
#def daggerfall():
#    return render_template('daggerfall.html')

@app.route('/doom')
def doom():
  return render_template('doom.html')

@app.route('/doom2')
def doom2():
    return render_template('doom2.html')

@app.route('/dos')
def dosPanel():
    return render_template('dos.html')

@app.route('/prince_of_persia')
def POP():
    return render_template("prince.html")

@app.route('/quake')
def quake():
    return render_template('quake.html')

@app.route('/wolfenstein')
def Wolf3D():
    return render_template('wolf.html')

@app.route('/in-dev')
def beta_world():
  return render_template('index[beta].html')

app.run(debug=True, host = '0.0.0.0')