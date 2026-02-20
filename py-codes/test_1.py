answer = input("Is it raining?\n").lower()
print(answer)

if answer == "yes":
    answer2 = input("Is it windy?\n")
    
    if answer2 == "yes":
        print("It is too windy for an umbrella\n")
    else:
        print("Then take an umbrella")
    
elif answer == "no":
    print("Enjoy your day")
    
