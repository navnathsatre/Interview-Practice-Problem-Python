from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return "Welcome to the Web Applications"


@app.route('/home/<name>')
def Hello(name):
    return "Hello " + name;


@app.route('/empid/<int:id>')
def empInfo(id):
    return "Your emp ID is : {}".format(id)


@app.route('/info/')
def informations():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)
