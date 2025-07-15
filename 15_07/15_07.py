from abc import abstractmethod

#Classes

class Group:
    pupils = True
    school_name = 42
    director = "Marivanna"

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader


    def study(self):
        print("sit down and read")

    @abstractmethod
    def move(self):
        pass

class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = "left"

    def __init__(self, title, pupils_count, group_leader, classroom):
        super().__init__(title, pupils_count, group_leader)
        self.classroom = classroom

    def move(self):
        print("run")


class HighGroup(Group):
    max_age = 18
    min_age = 14
    def move(self):
        print("walk")

class MediumGroup(Group):
    max_age = 14
    min_age = 11

first_a = PrimaryGroup("1a", 18, "MF", 10)
first_b = PrimaryGroup("1b", 20, "TD", 11)

eleven_a = HighGroup("11a", 15, "AR")
six_a = MediumGroup("6a", 24, "LK")

print(first_a.classroom)
print(first_b.classroom)
print(eleven_a.title)

# first_a.study()
# eleven_a.study()
# six_a.study()
#
# first_a.move()
# eleven_a.move()
# six_a.move()
