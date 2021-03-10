# Create a list of tuples of first name, last name, and age for your friends
# and colleagues. If you don't know the age, put in None. Calculate the
# average age, skipping over any None values. Print out each name,
# followed by old or young if they are above or below the average age.

people = [("sulochan", "thapa", None), ("shyam", "prasad", 3), ("hari", "sharma", 2)]
length = len(people)
total = 0
for x in range(0, 3):
     people_age=people[x][2]
     if people_age != None:
        total +=people_age
     else:
         continue
average_age = total / length

for x in range(3):
    if people[x][2] is not None and people[x][2]> average_age:
        print(people[x][0])
        print("old")
    elif people[x][2] is not None and people[x][2]< average_age:
        print(people[x][0])
        print("young")


