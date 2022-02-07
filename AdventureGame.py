print('''
           .-""""-.       .-""""-.
           /        \     /        /
          /_        _\   /_        _/
         // \      / \\ // \      / \\
         |\__\    /__/| |\__\    /__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        /
  /_        _\|  /_        _\|  /_        _ /
 // \      / \\ // \      / \\ // \      / \\
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
 jgs  |  |           |  |           |  |
      |  |           |  |           |  |


''')
print("Welcome to a Rick and Morty Adventure!\n\n\n\n") 

name = input("What is your name? ")
print(" \n\nYou've just finished an episode of Rick and Morty. You fall asleep.\n")

print(f"Rick portals into your bedroom.\n'Lets go {name}. In and out twewnty minute adventure.'\n")

decision = input("A. Its a dream! Go back to sleep. \nB. Go with Rick. \nDecision = ")
decision = decision.lower()

if decision == "b":
    print(" \nYou are on Ricks space ship watching the earth get smaller and smaller.\nRick puts the spaceship into autopilot, he burps then falls aleep. You look back and notice a big red shiny egg in the back seat.\n")
    decision2 = input("A. Touch the egg! \nB. Don't touch the egg! \nDecision = ")
    decision2 = decision2.lower() 
    if decision2 == "b":
        print(f" \nAliens begin shooting at you! Rick wakes up. \n'{name}, grab the box in the back!' Aliens keep shooting. \nRick starts to shoot back and dodges their attacks. \n'{name} cut the wire, when the count down begins throw the bomb.' \nYou ask 'Which wire?' but Rick is too occupied. He shouts 'Hurry up!'\n\n")
        decision3 = input("Do you cut the Red, Green or Blue wire? \nA. Red \nB. Green \nC. Blue \nDecision = ")
        decision3 = decision3.lower()
        if decision3 == "a":
            print(f" \nThe timer begins! Rick says 'Throw the bomb {name}!' \nYou throw the bomb and destroy the aliens chasing you. \nRick gives you gloves to pick up the egg. \n\nYou return the egg to its home, you are awarded with 3000 flerbos and spend the rest of the day at Blips and Chitz with Rick! \n\nWINNER!")
        elif decision3 == "b":
            print(" \nThe bomb explodes. \nYou and Rick are dead. \n\nGAME OVER!")
        else:
            print(" \nThe timer begins! You throw the bomb. \nIt doesn't explode. \nYou and Rick are blown up. \n\nGAMEOVER!")
    else: 
        print(" \nThe egg hatches. It's the cutest thing you've seen in your life. It looks at you. Then eats you! \n\nGAME OVER! ")  
else:
    print(" \nDude! You tottally just missed an adeventure with Rick! Back to your boring day job it is!")



 