from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filter", methods=["POST"])
def filter():
    if request.method == "POST":
        source = request.form['source']
        con = sqlite3.connect('bakery.db')
        comm = "SELECT BakeryItem.ItemNumber, BakeryItem.Name, BakeryItem.Source FROM BakeryItem WHERE BakeryItem.Source = '{}'".format(source)
        result = con.execute(comm).fetchall()
        con.close()
        return render_template("Task_4_Dana.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)