from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        text=request.form.get("text")
        print (text)
        return render_template("test.html", text=text)

@app.route("/test")
def test():
    test = ["joe", "bob", "rob"]
    return render_template("test.html", text=test)   

if __name__ == "__main__":
    app.run()