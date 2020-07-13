from flask import Flask,render_template

app = Flask(__name__)

data = []

@app.route('/user/<username>')
def profile(username):
    data.append(username)
    return render_template('adduser.html', adduser=username)
    

@app.route('/list')
def profile2():
    return render_template('userlist.html', list=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
