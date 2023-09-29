from flask import *

app = Flask(__name__)

app.secret_key = "abc"

@app.route("/home")
def home():
   return render_template("index.html")



@app.route("/login", methods = ["POST", "Get"])
def login():
   error = None;
   if request.method == "POST":
     if request.form['pass'] != "AAA":
       error = "Invalid Password"

     else:
       flash("success")
       return redirect(url_for('home'))
   return render_template("log.html", error=error)


app.run(debug=True)

