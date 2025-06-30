from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "get_verified_bitch"


# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
db = SQLAlchemy(app)

# Define a model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    
    elif request.method == "POST":
        name = session["username"]
        message = request.form["message"]
        new_entry = Submission(name=name, message=message)
        db.session.add(new_entry)
        db.session.commit()
        return redirect("/")

    all_submissions = Submission.query.order_by(Submission.id.desc()).limit(10).all()
    return render_template("home.html", submissions=all_submissions, username=session["username"])


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
