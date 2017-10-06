#create cheese and crackers function
def cheese_and_crackers(cheese_count, boxes_of_crckers):
    #print cheese count from function
    print(f"You have {cheese_count} cheeses")
    #print boxes of crackers from funtion
    print(f"you have {boxes_of_crckers} boxes of crackers!")
    #print comment output for function
    print("Man, thats enough for a party!")
    #print another with a newline
    print("Get a blanket.\n")
#
print("We can just give the function numbers directly")
#pass values directly into the function
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
#pass integer variables from the script, this changes previous values
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
