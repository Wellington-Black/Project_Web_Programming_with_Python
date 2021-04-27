import pdb
from models.activity import Activity
from models.member import Member
from models.attendance import Attendance

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.attendance_repository as attendance_repository

member1 = Member("Luis","Garcia", "LGarcia@email.com", "07723498234")
member2 = Member("Stuart", "Donovan", "SDonovan@email.com", "07612346521")
member3 = Member("Kakarot", "Gonzalez", "DBKing@email.com", "07346523491")
member4 = Member("Gon", "Freecss", "Janken@email.com", "07823487611")
member5 = Member("Midoriya", "Izuku", "OneforAll@email.com", "07712348576")

member_repository.save(member1)
member_repository.save(member2)
member_repository.save(member3)
member_repository.save(member4)
member_repository.save(member5)

activity1 = Activity("Salsa", "Vegeta", "18:00", "Paladium", "Beginner")
activity2 = Activity("Bachata", "Hinata", "19:00", "Island", "Intermediate")
activity3 = Activity("Salsa", "Naruto", "20:00", "Tumbao", "Advance")
activity4 = Activity("Bachata", "Misa", "21:00", "Paladium", "Improver")

activity_repository.save(activity1)
activity_repository.save(activity2)
activity_repository.save(activity3)
activity_repository.save(activity4)

attendance1 = Attendance(member1, activity1)
attendance2 = Attendance(member1, activity3)
attendance3 = Attendance(member2, activity4)
attendance4 = Attendance(member3, activity3)

attendance_repository.save(attendance1)
attendance_repository.save(attendance2)
attendance_repository.save(attendance3)
attendance_repository.save(attendance4)


member_repository.update(member1)


pdb.set_trace()