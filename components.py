# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age

class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.members = []
        self.president = None

    def assign_president(self, person):
        # your code goes here!
        self.president = person


    def recruit_member(self, person):
        # your code goes here!
        self.members.append(person)


    def print_member_list(self):
        # your code goes here!
        tot_age = 0
        for m in self.members:
            # print("""
            # - {} ({} years old) - {}
            # """).format(m.name, m.age, m.bio)
            print("==DEBUG==")
            print("m.presn", self.president.name)
            print("==DEBUG==")

            presn = ", President" if self.president.name == m.name else ""
            print(" - %s (%s years old%s) - %s" % (m.name, m.age, presn, m.bio))
            tot_age += m.age

        print("Avg age in this club: %s yr" %(tot_age/len(self.members)))
        print("---------------------------------------------------")

