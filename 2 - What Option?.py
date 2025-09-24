option = int(input("Input a number. What option would you like to choose?: "))
print("1 - Chicken")
print("2 - Beef")
print("3 - Turkey")
print("4 - Fish")
print()
match option:

    case 1:
        print("Good choice, chicken is a to-go to for a lean meat")
    case 2:
        print("Beef is not bad, but it can be fatty.")
    case 3:
        print("Turkey is like beef but with less of the fat, so would it be better?")
    case 4:
        print("Maybe the weakest link among the others, but it's still a solid protein.")
    case _:
        print("If you're reading this, you didn't put a number 1-4, shame on you.")

if option == 1 or option == 2 or option == 3 or option == 4:
    print("Bur thanks for sharing, bye!")