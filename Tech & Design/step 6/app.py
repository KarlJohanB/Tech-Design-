from flask import Flask, render_template, request
from classes import Author
from classes import Bucket
from models import User
from database import db_session, init_db


app = Flask("app")

def create_dummy_buckets():
    buckets = []

    # Buckets need an author
    author_1 = Author("Anna")
    author_2 = Author("Kalle")

    # Buckets
    bucket_1 = Bucket(author_1, "Bucket 1")
    bucket_2 = Bucket(author_2, "Bucket 2")

    buckets.append(bucket_1)
    buckets.append(bucket_2)

    return buckets

@app.route("/")
def main():

    return render_template("signup.html",
                           title="Login page",
                           buckets=create_dummy_buckets())

@app.route("/showSignup", methods=["GET", "POST"])

def showSignup():
    if request.method == "POST":
        name = request.form["inputName"]
        email = request.form["inputEmail"]
        password = request.form["inputPassword"]

        if name and email and password:
            user = User(name, email, password)
            db_session.add(user)
            db_session.commit()

            return render_template("signup.html",
                                   title="Sign up",
                                   success=True)
        else:
            return render_template("signup.html",
                                   title="Sign up",
                                   success=False)
    else:
        return render_template("signup.html",
                               title="Sign up")

app.run(debug=True)
