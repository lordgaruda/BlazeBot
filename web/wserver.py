from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>BlazeBot</title>
        </head>
        <body>
            <h1>BlazeBot is running on Heroku</h1>
        </body>
    </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
