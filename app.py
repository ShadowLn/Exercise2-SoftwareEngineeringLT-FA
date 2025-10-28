from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fatemeh and Leila</title>
        <style>
            body {
                background-color: lightblue;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                color: #003366;
                font-size: 2em;
                text-align: center;
                font-size:3rem
            }
        </style>
    </head>
    <body>
        <div>This page is made by <b>Fatemeh Abniki & Leila Tahryzadeh</b></div>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)