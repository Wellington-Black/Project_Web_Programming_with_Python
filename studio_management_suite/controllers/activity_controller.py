from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", activities = activities)

#GET
#NEW
@activities_blueprint.route("/activities/new", methods = ['GET'])
def new_activity():
    activities = activity_repository.select_all()
    return render_template("activities/new.html", all_activities = activities)

#CREATE
#POST
@activities_blueprint.route("/activities", methods = ['POST'])
def create_activity():
    name = request.form['name']
    instructor = request.form['instructor']
    time = request.form['time']
    studio = request.form['studio']
    level = request.form['level']
    # member = member_repository.select(member_id)
    activity = Activity(name, instructor, time, studio, level)
    activity_repository.save(activity)
    return redirect('/activities')