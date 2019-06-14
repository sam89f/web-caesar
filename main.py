from caesar import encrypt
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/encrypt" method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <textarea name="text"></textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/encrypt", methods=['POST'])
def caesar():
    rotate = request.form['rot']
    text = request.form['text']
    return '<h1>' + encrypt(text, int(rotate)) +'</h1>'

app.run()