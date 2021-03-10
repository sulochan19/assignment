# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it

name_list=["john","shyam","hari","gopal","john"]

count=0;
for name in name_list:
    if name=="john":
        count+=1;
        break
if count==0:
    print("name not found")
else:
    print("name found")