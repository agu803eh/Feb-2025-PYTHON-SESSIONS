#basics of file handling
#opening files
file = open("example.txt", "r") #open file in read mode# 
content = file.read() #read the content of the file
print(content) #print the content of the file
file.close() #close the file
#OR

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#with statement automatically closes the file after the block is executed

#writing to files
with open("example.txt", "w") as file: #open file in write mode
    file.write("Hello, Baby!") #write to the file
#append to files

try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.") 

try: #open a file that may not exist
    file = open("sample.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("operation completed")