from flask import Flask
from flask import render_template
from flask import request
import re


my_app = Flask(__name__) # application instance

@my_app.route("/", methods = ['GET', 'POST'])
def search():
    if request.method == "POST":
        text = request.form.get('str_input')
        string = request.form.get('exp_input')
        count = re.findall(string ,text)
        return render_template("base.html" , st = string, presence = count, cnt = len(count))

    return render_template("base.html")



if __name__ == "__main__":
    my_app.run(debug = True)