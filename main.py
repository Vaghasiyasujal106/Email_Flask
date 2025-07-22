from flask_restful import Api, Resource
from flask import Flask, render_template
from flask_mail import Mail, Message
from pyexpat.errors import messages

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['SECRET_KEY'] = "sujall2101030400425"
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "turabit.qa@gmail.com"  # Your email
app.config['MAIL_PASSWORD'] = "aamazjpktbrwwenp"  # Your email password

mail = Mail(app)

# Initialize Flask-RESTful API
api = Api(app)

class MailFlask(Resource):
    def get(self):  #get method page ko reload krne k liye use hoti hai and bina page ko reload karaye me koi work nhi kr sakti iska means ye hai muje pehle page reload krna padega and after me aur koi function ko use kr sakti hun like post etc....
        subject = "test mail"
        recipient = "sujalvaghasiya053@gmail.com"
        message_body = "this is test mail"

        msg = Message(subject=subject, sender='turabit.qa@gmail.com', recipients=[recipient])
        msg.body = message_body

        try:
            mail.send(msg)
            return "mail send successfully"
        except Exception as e:
            return "error:"+ str(e)

api.add_resource(MailFlask, '/send_mail')  #endpoit me kuchh bhi de sakti hun aisa nahi hai jo mera class hoga vahi endpoint hoga

if __name__ == '__main__':
    app.run(debug = True)

