from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome!"

# route that greets the user by their name
@app.route("/greet/<username>")
def greet(username):
    return "Hello, %s!" %username

# route that displays farewell meesage by their name
@app.route("/farewell/<username>")
def bye(username):
    return "Goodbye, %s!" %username
if __name__ == "__main__":
    app.run(debug=True)
