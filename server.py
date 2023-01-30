from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# to run flask flask --app filename run


#listening to the server for username 
@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 