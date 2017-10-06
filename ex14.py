#import argv from sys library
from sys import argv
#defines arguments for argv - in this text it is script name an
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, im the {script} script")
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
And you have a {computer} computer. Nice.
""")
