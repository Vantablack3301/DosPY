from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/wolfenstein')
def Wolf3D():
    return render_template('wolf.html')

@app.route('/in-dev')
def beta_world():
  return render_template('index[beta].html')

app.run(host = '0.0.0.0')