from title import *
from fetchxnum import *
from keywords import *
from functools import cache

print("Welcome! Please select a function: ")
print("   1. Select number of articles to display")
print("   2. Search by keyword")
print("   3. Search by title")

stop = 0
while(stop != 1):
    choice1 = input("Number: ")

    match choice1:
        case "1":
            number = input("How many articles would you like to see? (1-10): ")
            choice2 = input("Would you like to choose a category? Y/N: ")
            if choice2 == "Y":
                print("What category would you like?")
                print("   1. General")
                print("   2. World")
                print("   3. Nation")
                print("   4. Business")
                print("   5. Technology")
                print("   6. Entertainment")
                print("   7. Sports")
                print("   8. Science")
                print("   9. Health")
                cat = input("Category: ")
            else:
                cat = "general"
            xnum(number, cat)
            stop = 1;
        case "2":
            key = input("What keyword would you like to search? ")
            keyword(key)
            stop = 1;
        case "3":
            print("What is the title of the article? (Check your spelling!)")
            t = input("If that title does not exist, the next closest will be returned. ")
            title(t)
            stop = 1;
        case _ :
            print("Invalid input. Try again!")