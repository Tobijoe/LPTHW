
#from sys import argv argument
from sys import argv
#add arguments to argv, in this case script name (ex15.py)and the text sample (ex15sample.txt)
script, filename = argv
#set var txt to open filename given in argument
txt = open(filename)
#print formatted string, with filename
print(f"Here is your file {filename}")
#print contents of filename
print(txt.read())
#prompt for user input
print("Type the filename again:")
#set var file_again to ask for user input of filename
file_again = input("->")
#set text_again var to open given filename
txt_again = open(file_again)
#print contents of given filename in text_again
print(txt_again.read())
