from db.run_sql import run_sql
from models.attendance import Attendance
from models.member import Member
from models.activity import Activity
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def save(attendance):
    sql = "INSERT INTO attendances ( member_id, activity_id ) VALUES ( %s, %s ) RETURNING id"
    values = [attendance.member_id, attendance.activity_id]
    results = run_sql( sql, values )
    attendance.id = results[0]['id']
    return attendance

def update(attendance):
    sql = "UPDATE attendances SET ( member_id, activity_id ) = ( %s, %s ) WHERE id = %s"
    values = [attendance.member_id, attendance.activity_id, attendance.id]
    run_sql(sql, values)

def select_all():
    attendances = []

    sql = '''SELECT m.id as member_id, act.id as activity_id, m.first_name, m.last_name,
            act.name as activity_name
            FROM attendances att 
            JOIN activities act ON (act.id = att.activity_id) 
            JOIN members m ON (m.id = att.member_id)'''
    results = run_sql(sql)

    for row in results:
        attendances.append(Booking(**row))
    return attendances