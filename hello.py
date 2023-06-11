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
                .container {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                h1 {
                    color: blue;
                }
                p {
                    color: blue;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello World, We are the Itian! &#127881;</h1>
                <p>always Proud. &#127881;&#127882;</p>
            </div>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0')
