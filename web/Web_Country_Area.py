import flask
from flask import *

# import model
from model import read_files
#local
qurey = read_files()

app =Flask(__name__)

@app.route("/")
def render():
    return render_template('index.html')

@app.route("/ShowArea",methods=['POST','GET'])
def ShowArea():
    if request.method == 'POST':
        # Go to model
        qurey_country = request.form['Country']
        GoToModel = qurey.read(qurey_country)
        return render_template('index.html',GoToModel = qurey.read(qurey_country))
        
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)