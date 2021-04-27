from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member

def save(member):
    sql = "INSERT INTO members( first_name, last_name, email, phone ) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [member.first_name, member.last_name, member.email, member.phone]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, email, phone) = ( %s, %s, %s, %s ) WHERE id = %s"
    values = [member.first_name, member.last_name, member.email, member.phone, member.id]
    run_sql(sql, values)

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['email'], row['phone'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['email'], result['phone'], result['id'] )
    return member

