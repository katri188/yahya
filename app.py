from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# معلومات المستخدمين (قاعدة بيانات بسيطة)
users = []

# كلمة السر الخاصة بالإدمن
ADMIN_PASSWORD = '96762011'
USER_PASSWORD = '9900'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    role = request.form['role']
    password = request.form['password']

    if role == 'user' and password == USER_PASSWORD:
        return render_template('user_login.html')
    elif role == 'admin' and password == ADMIN_PASSWORD:
        return redirect(url_for('admin_dashboard'))
    else:
        return 'كلمة السر خاطئة!'


@app.route('/user_login', methods=['POST'])
def user_login():
    username = request.form['username']
    password = request.form['user_password']

    # تخزين المعلومات في جدول
    users.append({
        'username': username,
        'password': password,
        'timestamp': datetime.now(),
        'device': request.user_agent.platform,  # الجهاز المستخدم
        'random_number': random.randint(1000000, 99999999)
    })

    return render_template('user_result.html', random_number=users[-1]['random_number'])


@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html', users=users)


@app.route('/delete_user/<int:index>')
def delete_user(index):
    if index < len(users):
        del users[index]
    return redirect(url_for('admin_dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
