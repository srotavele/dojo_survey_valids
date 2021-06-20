from flask import Flask, render_template, request, redirect, session
from flask_app import app
from ..models.dojos import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all()
    
    return render_template("index.html", all_dojos = dojos)

@app.route('/create/', methods = ['POST'])
def creates_survey():
    if not Dojo.validate_survey(request.form):
        return redirect('/')

    dojos = Dojo.create(request.form)

    return redirect('/survey/results')


@app.route('/survey/results')
def survey__results():
    survey = Dojo.get_results()
    return render_template('results.html', survey = survey[0])


@app.route('/reset')
def reset():
    return redirect ('/')