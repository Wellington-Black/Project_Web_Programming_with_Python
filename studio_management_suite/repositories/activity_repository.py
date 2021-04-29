from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member
from models.booking import Booking


def save(activity):
    sql = "INSERT INTO activities(name, instructor, time, studio, level) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [activity.name, activity.instructor, activity.time, activity.studio, activity.level]
    results = run_sql( sql, values )
    activity.id = results[0]['id']
    return activity

def update(activity):
    sql = "UPDATE activities SET (name, instructor, time, studio, level) = ( %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [activity.name, activity.instructor, activity.time, activity.studio, activity.level, activity.id]
    run_sql(sql, values)

def select_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)
    for row in results:
        activity = Activity(row['name'], row['instructor'], row['time'], row['studio'], row['level'], row['id'])
        activities.append(activity)
    return activities

def upcoming():
    activities = []

    sql = "SELECT * FROM activities WHERE time > NOW()"
    results = run_sql(sql)
    for row in results:
        activity = Activity(row['name'], row['instructor'], row['time'], row['studio'], row['level'], row['id'])
        activities.append(activity)
    return activities

def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(result['name'], result['instructor'], result['time'], result['studio'], result['level'], result['id'] )
    return activity


def select_activity_id(id):
    attendances = []

    sql = '''SELECT 
                m.id as member_id, 
                act.id as activity_id, 
                m.first_name, 
                m.last_name,
                act.name as activity_name
            FROM attendances att 
            JOIN activities act ON (act.id = att.activity_id) 
            JOIN members m ON (m.id = att.member_id) 
            WHERE act.id = %s '''
    results = run_sql(sql, id)

    # results = [{"member_id":3, "activity_id":4, "firs..."},
    #            {"member_id":3, "activity_id":4, "firs..."} ]

    for row in results:
        # row = {"member_id":3, "activity_id":4, "firs..."} 

        # A: Booking( {"member_id":3, "activity_id":4, "firs..."} ) == Booking(row)

        # B: Booking(member_id =3, activity_id=4, first_name=... ) == Booking(**row)


        attendances.append(Booking(**row))
    return attendances