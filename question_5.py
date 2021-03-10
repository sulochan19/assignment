# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

detail = ("sulochan", "thapa", 22)
people = []
people.append(detail)
detail1 = ("hari", "sharma", 23)
people.append(detail1)
detail2 = ("shyam", "prasad", 24)
people.append(detail2)
people.sort(key=lambda x: x[1], reverse=True)
print(people)
