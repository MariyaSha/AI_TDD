import re
import string

from flask import Flask, render_template, request

app = Flask(__name__)


def valid_password(value):
    return (len(value) >= 6
            and re.search(r'[A-Z]', value) is not None
            and re.search(r'[a-z]', value) is not None
            and re.search(r'[0-9]', value) is not None
            and any(char in string.punctuation for char in value))


@app.route('/', methods=['GET', 'POST'])
def register():
    error = None
    success = False
    if request.method == 'POST':
        if not re.fullmatch(r'[A-Za-z0-9]+', request.form.get('username', '')):
            error = 'Username must contain only ASCII letters and digits.'
        elif not valid_password(request.form.get('password', '')):
            error = 'Password must meet all requirements.'
        else:
            success = True
    return render_template('register.html', error=error, success=success), 400 if error else 200
