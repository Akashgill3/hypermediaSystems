from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts")
def contacts():
    search = request.args.get("q")
    if search is not None:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all()
    return render_template("index.html", contacts=contacts_set)

@app.route("/contacts/new", methods=['GET'])
def contacts_new_get():
    return render_template("new.html", contact=Contact())
