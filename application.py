from flask import Flask, redirect, render_template, request


app = Flask(__m__)

@app.route("/")
def home():
    return render_template("index.html")