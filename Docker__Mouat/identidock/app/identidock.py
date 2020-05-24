from flask import Flask
from flask import render_template
from flask import Response
import requests


app = Flask(__name__)
default_name = 'Joe Bloggs'


@app.route('/')
def mainpage():
    name = default_name

    return render_template('home.html', name=name)


@app.route('/monster/<name>')
def get_identicon(name):
    request = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = request.content

    return Response(image, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
