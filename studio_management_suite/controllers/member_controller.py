from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

#GET
#NEW
@members_blueprint.route("/members/new", methods = ['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", all_members = members)

#CREATE
#POST
@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    # member = member_repository.select(member_id)
    member = Member(first_name, last_name, email, phone)
    member_repository.save(member)
    return redirect('/members')

# SHOW
# GET '/members/<id>'
@members_blueprint.route("/members/<id>", methods = ['GET'])
def show_member(id):
    member = member_repository.select(id)
    return render_template('members/show.html', member = member)