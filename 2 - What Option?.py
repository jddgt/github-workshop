while True:
    print(("Input a number. What option would you like to choose?: "
           "\n1 - Chicken"
           "\n2 - Beef"
           "\n3 - Turkey"
           "\n4 - Fish"))
    option = int(input())
    print()
    while True:
        match option:
            case 1:
                print("Good choice, chicken is a to-go to for a lean meat")
                break
            case 2:
                print("Beef is not bad, but it can be fatty.")
                break
            case 3:
                print("Turkey is like beef but with less of the fat, so would it be better?")
                break
            case 4:
                print("Maybe the weakest link among the others, but it's still a solid protein.")
            case _:
                print("If you're reading this, you didn't put a number 1-4, shame on you.")
    print()
    again = input("Want to select something else? ")
    if again in ("Yes", "yes", "YES" "Y", "y"):
        print()
        continue
    else:
        print("Bur thanks for sharing. Buh-bye")