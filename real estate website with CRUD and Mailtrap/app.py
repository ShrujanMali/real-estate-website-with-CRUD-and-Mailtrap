from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from send_mail import send_mail
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact-us.db'

app.config['MAIL_SERVER'] = ''
db = SQLAlchemy(app)


class PropertyFY(db.Model):
    """ Data base structure for posts """
    id = db.Column(db.Integer, primary_key=True)    # primary key is unique for user
    title = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    emails = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner = db.Column(db.String(20), nullable=False, default='N/A')
    want = db.Column(db.String(20), nullable=False)
    property = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'PropertyFY' + str(self.id)

# db for contact us
class Contact_US(db.Model):
    """ Data base structure of contact us form """
    id = db.Column(db.Integer, primary_key=True)    # primary key is unique for user
    name = db.Column(db.String(20), nullable=False)
    email_add = db.Column(db.String(25), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'enq' + str(self.id)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')
    
# to cerate post
@app.route('/posts', methods=['GET','POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_address = request.form['address']
        post_want = request.form['want']
        post_property = request.form['property']
        post_emails = request.form['emails']
        post_description = request.form['description']
        post_owner = request.form['owner']

        if post_title == '' or post_emails == '' or post_property == '' or post_address == '' or post_owner == '' or post_description == '':
            return render_template('new_post.html', message="Please, fill required fields")
        else:
            new_post = PropertyFY(title=post_title, address=post_address, want=post_want, property=post_property, 
                                  emails=post_emails, description=post_description, owner=post_owner)
            db.session.add(new_post)
            db.session.commit()
            return render_template('new_post.html', message="Thank you")
    else:
        all_posts = PropertyFY.query.order_by(PropertyFY.date_posted).all()         # new post comes under previous post
        return render_template('posts.html', posts= all_posts)                      # posts is variable

# Delete post
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = PropertyFY.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


# Edit post
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = PropertyFY.query.get_or_404(id) 
    if request.method == 'POST':
        
        post.title = request.form['title']
        post.address = request.form['address']
        post.want = request.form['want']
        post.property = request.form['property']  
        post.emails = request.form['emails']
        post.description = request.form['description']
        post.owner = request.form['owner']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)


# Crate new post page
@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_address = request.form['address']
        post_want = request.form['want']
        post_property = request.form['property']   
        post_emails = request.form['emails']
        post_description = request.form['descrption']
        post_owner = request.form['owner']
        
        if post_title == '' or post_emails == '' or post_property == '' or post_address == '' or post_owner == '' or post_description == '':
            return render_template('new_post.html', message="Please, fill required fields")
        else:
            new_post = PropertyFY(title=post_title, address=post_address, want=post_want, property=post_property, 
                                  emails=post_emails, description=post_description, owner=post_owner)
            db.session.add(new_post)
            db.session.commit()
            return render_template('new_post.html', message="Thank you")
    else:
        all_posts = PropertyFY.query.order_by(PropertyFY.date_posted).all()
        return render_template('new_post.html', posts= all_posts)  


@app.route('/contactus', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        name = request.form['name']
        email_add = request.form['email_add']
        description = request.form['description']
        
        if name == '' or email_add == '' or description == '':
            return render_template('contactus.html', message="Please, fill required fields")
        else:
            enq = Contact_US(name=name, email_add=email_add, description=description)
            db.session.add(enq)
            db.session.commit()
            send_mail(name, email_add, description)
            return render_template('contactus.html', message="Thank you")
    else:
        return render_template('contactus.html')

if __name__ == '__main__':
    app.run(debug=True)
