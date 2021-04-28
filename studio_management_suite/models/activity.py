class Activity:

    def __init__(self, name, instructor, time, studio, level, id = None):
        self.name = name
        self.instructor = instructor
        self.time = time
        self.studio = studio
        self.level = level
        self.id = id

    def __str__(self):
        return '{}'.format(self.name)