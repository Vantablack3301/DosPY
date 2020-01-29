from flask import Flask, render_template, request, redirect, url_for, flash, make_response

def num_there(s):
    return any(i.isdigit() for i in s)



app = Flask(__name__)

@app.route('/')
def index():
    token = request.cookies.get('token')
    if 'country' in request.cookies:
        return render_template('index.html')
    else:
        excel = input("please enter a valid string")
        if num_there(excel) == True:
            resp = make_response(render_template('index.html'))
            return render_template('index.html')
            resp.set_cookie('username', 'the username')
            return resp
        else:
            print("invalid code, shutting down")



    if __name__ == '__main__':
        app.run()


