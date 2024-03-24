from flask import Flask, render_template
from flask_mail import Mail, Message
from config import email,senha

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)