from flask import Flask
from flask import render_template


app = Flask(__name__)
default_name = 'Joe Bloggs'


@app.route('/')
def get_identicon():
    name = default_name

    return render_template('home.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
