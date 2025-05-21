print("welcome plese")
print("we gonna create a list of 5 names")

# crete a list of 5 names
names = []
for i in range(5):
    name = input(f"Enter name{i+1}:")
    names.append(name)
    
#out put 2nd item
print(f"\n the 2nd name is in the list {names[1]}")

#change 1st item
new_first = input("enter a new name to replace the first name:")
names[0]= new_first
print("updated list:", names)

# add a 6th item
sixth_name = input(" enter a 6th name to add to list:")
names.append(sixth_name)
print("list after adding 6th name:", names)

# add Bathel as 3rd item 
custom_insert =input("put Bathel in 3rd position:")
names.insert(2,custom_insert)
print("list after inserting into 3rd position", names)

#remove from 4th item
print(f"removing the 4th item:{names[3]}")
del names[3]
print("list after deleting 4th item",names)

#print the last item using negative indexing
print(f"the last item(using-1)is:{names[-1]}")

# create a new list of 7 i tems
print("\n lets create a new list of 7 fav things")
new_list=[]
for i in range(7):
    item=input(f"Enter item{i+1}:")
    new_list.append(item)
    
print("your 3rd to 5th favorite things are:",new_list[2:5])