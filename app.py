from flask import Flask, render_template, redirect, url_for, flash
from forms import Contact
from flask_mail import Mail, Message

app = Flask(__name__)
app.config["SECRET_KEY"] = "4bd5619c1e0b8ec14ac983703b2000c5"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "ansumanmaharana74@gmail.com"
app.config["MAIL_PASSWORD"] = "xhloavsaroxisgsz"
app.config["MAIL_DEFAULT_SENDER"] = "ansumanmaharana74@gmail.com"

mail = Mail(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = Contact()
    if form.validate_on_submit():
        username = form.username.data
        phonenumber = form.phonenumber.data
        email = form.email.data

        msg = Message(
            subject="New Contact Form Submission",
            recipients=["mahranaansuman@gmail.com"],
            body=f"Contact {username}, with {phonenumber} and {email}."
        )
        mail.send(msg)

        flash(f"Thank you {username}! I will contact you at {email}.")
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact", form=form)

if __name__ == "__main__":
    app.run(debug=True)