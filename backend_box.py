import flask
import subprocess 


app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template("page.html")

@app.route('/submit', methods=['POST'])
def submit():
    timezone = flask.request.form.get('timezone')
    try:
        command = f"timedatectl list-timezones | grep {timezone}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
    except Exception as e:
        output = str(e)
    return flask.render_template("page.html", output=output, timezone=timezone)



app.config['SERVER_NAME'] = f"box.localhost"
app.run(debug=True)
