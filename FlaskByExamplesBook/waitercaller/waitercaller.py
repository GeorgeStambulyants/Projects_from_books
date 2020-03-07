from flask import (
    Flask, render_template, redirect, url_for, request
)
from flask_login import (
    LoginManager, login_required, login_user, logout_user
)
from mockdbhelper import (
    MockDBHelper as DBHelper,
)
from user import (
    User,
)
from passwordhelper import (
    PasswordHelper,
)


app = Flask(__name__)
app.secret_key = 'PopsZqs41yburEp4q4GzhybXXo9pRY3KSMQ6xZHxV \
                    rZLhp9R0rSPxdg413ACQ2GAz5eQhgFDf4p2KOQnPRzQYvBZcW1jkSf'
login_manager = LoginManager(app)
DB = DBHelper()
PH = PasswordHelper()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/account')
@login_required
def account():
    return render_template('account.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    stored_user = DB.get_user(email)
    with open('log.txt', 'w') as f:
        f.write('email: ' + email + '\n')
        f.write('password: ' + password + '\n') 
        f.write('stored_user: ' + password + '\n')  
    if stored_user and PH.validate_password(password,
        stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    pw1 = request.form.get('password')
    pw2 = request.form.get('password2')
    if not pw1 == pw2:
        return redirect(url_for('q'))
    if DB.get_user(email):
        return redirect(url_for('a'))
    salt = PH.get_salt()
    hashed = PH.get_hash(pw1 + salt.decode())
    DB.add_user(email, salt, hashed)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
