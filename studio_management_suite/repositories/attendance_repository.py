from db.run_sql import run_sql
from models.attendance import Attendance
from models.member import Member
from models.activity import Activity

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

    sql = "SELECT * FROM attendances"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        activity = activity_repository.select(row['activity_id'])
        attendance = Attendance(member, activity, row['id'])
        attendances.append(attendance)
    return attendances