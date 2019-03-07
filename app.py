from flask import Flask, render_template

#Create instance of Flask App
app = Flask(__name__)

#Define Route and its content
@app.route("/")
def home():
    return render_template("index.html")

#Define 2nd route w/ content
@app.route("/about")
def about():
    return("About me")

#Running and controlling the script; still unclear what is happening here and how
if(__name__=="__main__"):
    app.run(debug=True)





#Project url: https://towardsdatascience.com/master-python-through-building-real-world-applications-part-4-7a72ae77e741