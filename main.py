from flask import Flask, render_template, send_file, request
from forms import ContactForm
from flask_mail import Mail, Message
import os


app = Flask(__name__)

app.config.update(
DEBUG=True,
#EMAIL SETTINGS
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT=465,
MAIL_USE_SSL=True,
MAIL_USERNAME = os.getenv('GMAIL_USER'),
MAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
)

mail = Mail(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    msg = Message(subject,
                    sender=email,
                    recipients=["alexcornea@gmail.com"])
    msg.body = f'Name: {name} \n Email: {email} \n Message: \n "{message}"'
    mail.send(msg)
    confirm_msg = 'Your message has been sent.'
    return render_template("index.html", confirm_msg=confirm_msg)

@app.route('/download', methods=['GET', 'POST'])
def download_file():
    file = 'cv.pdf'
    return send_file(file, as_attachment=True)

@app.route('/post1')
def post1():
    return render_template("post1.html")

@app.route('/post2')
def post2():
    return render_template("post2.html")

@app.route('/post3')
def post3():
    return render_template("post3.html")


if __name__ == '__main__':
    app.run(debug=True)


