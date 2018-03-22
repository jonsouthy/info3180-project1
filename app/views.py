"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, random, datetime, uuid
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify, make_response
from werkzeug.utils import secure_filename
from form import signForm
from models import UserProfile


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile',methods=["GET","POST"])
def profile():

    # Instantiate your form class
    form = signForm()
    # Validate file upload on submit
    if request.method == 'POST':
        ff = app.config['UPLOAD_FOLDER']
        # Get form data
        if form.validate_on_submit():
            fname = form.fname.data
            lname = form.lname.data
            gender = form.gender.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            photo = form.upload.data
            
            created_on = datetime.date.today()
            userid = random_id()
            
            newuser = UserProfile(userid=userid, fname = fname, lname =lname, gender=gender, email=email,
                        location=location, biography=biography,created_on=created_on,photo=photo)
            
            db.session.add(newuser)
            db.session.commit()
            
            flash('Created Successfully', 'success')
            return redirect(url_for('profile'))

    return render_template('signup.html', form=form)
    

    
@app.route('/profiles',methods=["GET","POST"])
def profiles():
    
    users = UserProfile.query.all()
    if request.method == "GET":
        ff = app.config['UPLOAD_FOLDER']
        return render_template("userlist.html",users=users)


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


    
@app.route('/profile/userid')
def prof():
    user = UserProfile.query.filter_by(userid=userid).first()
    
    if request.method == "GET":
        ff = app.config['UPLOAD_FOLDER']
        return render_template("userprof.html", user=user)
    
def random_id():
    rid = uuid.uuid4()
    return rid
    
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
