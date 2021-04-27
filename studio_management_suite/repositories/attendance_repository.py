from db.run_sql import run_sql
from models.attendance import Attendance
from models.member import Member
from models.activity import Activity

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

def save(attendance):
    sql = "INSERT INTO attendances ( member_id, activity_id ) VALUES ( %s, %s ) RETURNING id"
    values = [attendance.member.id, attendance.activity.id]
    results = run_sql( sql, values )
    attendance.id = results[0]['id']
    return attendance