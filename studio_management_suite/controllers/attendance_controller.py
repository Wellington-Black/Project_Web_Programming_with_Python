from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attendance import Attendance
import repositories.attendance_repository as attendance_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

attendances_blueprint = Blueprint("attendances", __name__)

@attendances_blueprint.route("/attendances")
def attendances():
    attendances = attendance_repository.select_all()
    return render_template("attendances/index.html", attendances = attendances)

#GET
#NEW
@attendances_blueprint.route("/attendances/new", methods = ['GET'])
def new_attendance():
    members = member_repository.select_all()
    activities = activity_repository.select_all()

    return render_template("attendances/new.html", members = members, activities= activities)


#CREATE
#POST
@attendances_blueprint.route("/attendances", methods = ['POST'])
def create_attendance():
    member_id = request.form['member_id']
    activity_id = request.form['activity_id']
    attendance = Attendance(member_id, activity_id)
    attendance_repository.save(attendance)
    return redirect('/attendances/index.html')