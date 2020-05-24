from flask import Flask, request
from flask import render_template
from flask import Response
import requests
import hashlib


app = Flask(__name__)
salt = 'UNIQUE_SALT'
default_name = 'Joe Bloggs'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
    name = default_name

    if request.method == 'POST':
        name = request.form['name']

    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    return render_template('home.html', name=name, name_hash=name_hash)


@app.route('/monster/<name>')
def get_identicon(name):
    request = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = request.content

    return Response(image, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
