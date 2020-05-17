from flask import Flask
import json
from flask import render_template
from flask import request
import dbconfig
import dateparser
import datetime
import string
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper

app = Flask(__name__)
DB = DBHelper()

categories = ['mugging', 'break-in']


@app.route('/')
def home(error_message=None):
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template('home.html',
                           crimes=crimes,
                           categories=categories,
                           error_message=error_message)


@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as e:
        print(e)
    return home()


@app.route('/submitcrime', methods=['POST'])
def submitcrime():
    category = request.form.get('category')
    if category not in categories:
        return home()
    date = format_date(request.form.get('date'))
    if not date:
        return home('Invalid date. Please use yyyy-mm-dd format')
    try:
        latitude = float(request.form.get('latitude'))
        longtitude = float(request.form.get('longtitude'))
    except ValueError:
        return home()
    description = request.form.get('description')
    description = sanitize_string(request.form.get('description'))
    DB.add_crime(category, date, latitude, longtitude, description)
    return home()


def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, '%Y-%m-%d')
    except TypeError:
        return None


def sanitize_string(userinput):
    whitelist = string.ascii_letters + string.digits + ' !?$.,:-\'()&'
    return ''.join(list(filter(lambda x: x in whitelist, userinput)))


if __name__ == '__main__':
    app.run(port=5000, debug=True)