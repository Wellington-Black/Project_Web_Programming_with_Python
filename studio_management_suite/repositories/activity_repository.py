from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

def save(activity):
    sql = "INSERT INTO activities(name, instructor, time, studio, level) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [activity.name, activity.instructor, activity.time, activity.studio, activity.level]
    results = run_sql( sql, values )
    activity.id = results[0]['id']
    return activity