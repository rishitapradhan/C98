

f = open("text.txt")


f = open("text.txt")
fileLines = f.readlines()

for line in fileLines:
    print(line)

introString = "My name is Rishita Pradhan. I like to read, sing, dance and run."
words = introString.split(",")
print(words)




def greet(Name):
    print("Hello , " + Name + " How are you ?")

greet("RiShiTa")