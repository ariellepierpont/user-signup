from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


def is_username():
    for chars in request.form['username']:
        if chars <= 20 or chars >= 3:
            return True
        else: 
            return username_error

def is_password():
    for chars in request.form['password']:
        if chars <= 20 or chars >= 3 or chars != '':
            return True
        else:
            return password_error

def is_verify():
    for chars in request.form['verify']:
        if chars == chars in request.form['password']:
            return True
        else: 
            return verify_error

def is_email():
    for chars in request.form['email']:
        if chars == '@' or chars == '.' or chars == '':
            return True
        else:
            return email_error

@app.route("/", methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if not is_username():
        username_error = 'Please create a username between 3-20 characters'
        username = ''
        #else:
        #username = #validate that it is text using html escape

    if not is_password():
        password_error = 'Please make sure your password is between 3-20 characters and does not contain any spaces.'
        password = request.form['password']
    else:
        password = ''

    if not is_verify():
        verify_error = 'Please make sure your passwords match.'
        verify = request.form['verify']
    else: 
        verify = ''
    
    if not is_email():
        email_error = 'Please enter a valid e-mail including the @ symbol and a period.'
    else: 
        email = ''

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        template = jinja_env.get_template('home.html')
        return template.render(username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.args.get('username')
    #or return '<h1>Welcome, ' + cgi.escape(username) + '</h1>' if not using templates
    #template = jinja_env.get_template('welcome.html')
    #return template.render(username=username)
    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    return render_template('home.html')

    
app.run()

#update as of 10/10 @ 3:39PM:
    #keeps UN and E-mail and deletes PW!
    #goes to new page, but shows "None" as the UN
    #submits with errors 

#error if any feilds are empty

#error if UN or PW are not valid (no spaces, must be within 3-20 characters)

#error if PW and PW conf do not match 

#error if user provides email but it is invalid - can be left empty, but if not empty, must be validated
#email must have a single @, a single ., and is 3-20 chars

#feedback message must be next to feild it goes with 

#welcome page when all input is valid

