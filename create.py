file = open("create.txt","x")
file.write("file created using x mode")
file.close()

print("file created successfully")

file = open("append.txt","a")
file.write("This is my first line\n")
file.close()


file=open("append.txt","w")
file.write("this content will overwrite old data")
file.close()