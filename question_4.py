# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

name_list=[]

name_list.append("aakash")
print(id(name_list))
name_list.append("ram")
print(id(name_list))
name_list.append("hari")
print(id(name_list))
# No, the id of the last has not changed
print("No, the id of the last has not changed ")

sorted_name_list=sorted(name_list)
print("the first item on the list is ",sorted_name_list[0],"and second item is",sorted_name_list[len(sorted_name_list)-1])