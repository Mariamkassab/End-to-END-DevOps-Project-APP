from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <html>
        <head>
            <style>
                /* Add CSS styles here */
                body {
                    background-color: lightblue;
                }
                h1 {
                    color: red;
                }
                p {
                    color: green;
                }
            </style>
        </head>
        <body>
            <h1>Hello World, We are the Itian!</h1>
            <p>This is a colored paragraph.</p>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
