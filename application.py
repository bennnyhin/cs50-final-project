from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        text = request.form.get("name")
        return render_template("index.html", text=text)
    

if __name__ == "__main__":
    app.run()