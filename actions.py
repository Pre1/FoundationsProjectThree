# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Abdullah"
my_age = 11011
my_bio = "coding all the way down!!1"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

# def display_clubs():
	# """
	# utility function that display existing clubs
	# and return dict contating -> {club name of type str: club object} 
	# """
	# clb_names = {}
	# for c in clubs:
	# 	print("""
	# 	Name: {}
	# 	Description: {}
	# 	Members: {}
	# 	""".format(c.name, c.description, len(c.members)))

	# 	clb_names[c.name] = c # {club name: clb object}

	# print("---------------------------------------------------")
	# return clb_names



	
def options():
    # your code goes here!
	print("-------------------------")
	print("""
	Would you like to:
	1) Create a new club.
	or:
	2) Browse and join clubs.
	or:
	3) View existing clubs.
	or: 
	4) Display members of a club.
	or:
	-1) Close application.
	""")

	choice = int(input("> "))
	return choice


def create_club():
    # your code goes here!
    name = input("pick a name for your club: ")
    desc = input("What is your club about? ")

    club = Club(name, desc)

    print("""
    Enter the number of the people you'd like to recruit
    to your new club (-1 to stop):
    ---------------------------------------------------
    """)

    for i, v in enumerate(population):
    	print("[{}] {}".format(i+1, v.name))

    inn = None
    while inn != -1:
    	inn = int(input("> "))
    	club.members.append(population[inn-1])

    club.assign_president(myself)
    club.recruit_member(myself)
    clubs.append(club)
    
    print("""
    Here's your club:
    {}
    {}
	""".format(club.name, club.description))


def view_clubs():
	"""
	utility function that display existing clubs
	and return dict contating -> {club name of type str: club object} 
	"""
    # your code goes here!
	clb_names = {}

	for c in clubs:
		print("""
		Name: {}
		Description: {}
		Members: {}
		""".format(c.name, c.description, len(c.members)))

		clb_names[c.name.lower()] = c # {club name: clb object}
	
	print("---------------------------------------------------")
	return clb_names


def view_club_members():
    # your code goes here!
	clbs = view_clubs()

	clb_choice = input("Enter the name of the club whose members you'd like to see: ")

	clb = clbs.get(clb_choice.lower())
	if clb:
		clb.print_member_list()
	else:
		print("No such club sir!")


def join_clubs():
	clbs = view_clubs()
	club_choice = input("choose a club by typing its name: ")
	clb = clbs.get(club_choice.lower())

	if clb: 
		clb.recruit_member(myself)
		print("{} just joined {}!".format(my_name, club_choice))

	else:
		print("No such club sir!")
	print("---------------------------------------------------")

def application():
	introduction()

    # op = None
	while True:
		op = options()
		if op == 1:
			create_club()
		elif op == 2:
			join_clubs()
		elif op == 3:
			view_clubs()
		elif op == 4:
			view_club_members()
		else:
			break
    # your code goes here!


### testing ###
# print(clubs[0].print_member_list())




