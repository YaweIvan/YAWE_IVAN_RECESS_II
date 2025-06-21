##
with open ("geoff.txt", "r")as file:
    content = file.read()
    print(content)
    


#Writing to a file 
with open("geoff.txt", "w")as file:
    file.write("Hello python\n")
    #wirting another file