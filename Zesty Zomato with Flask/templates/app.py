from flask import flask
app = Flask(__name__)

blogs=[]

@app.route("/read")
def read_blog():
    return blogs

# route for write
@app.route("/write", methods=['GET','POST'])
def write_blog():
    if method == 'POST':
        