score = 0
print('Welcome to the computer quiz game!')
print('----------------------------------')
name = input('What\'s your name? ')
ask = input(f"Hi {name} do you wanna play the quiz game? ")
if ask != "yes" and ask != "Yes":
    print("as you wish!")
    quit()

print("Ok let's play :)")

quest_1 = input("What does CPU stands for? ")
if quest_1 == "Central processing unit" or quest_1 =="central processing unit":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_2 = input("What does PSU stand for? ")
if quest_2 == "power supply" or quest_2 == "Power supply":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_3 = input('What does GPU stand for? ')
if quest_3 == 'graphics processing unit' or quest_3 == 'Graphics processing unit':
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_4 = input("What does RAM stand for? ")
if quest_4 == "random access memory" or quest_4 == "Random access memory":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_5 = input('What does ROM stand for? ')
if quest_5 == 'read-only memory' or quest_5 == 'Read-only memory' or quest_5 == 'Read only memory' or quest_5 == 'read only memory':
    print('correct!')
    score += 1
else:
    print('That\'s wrong!')


print(f'Your score is {score}/5')
if score == 5:
    print('You rock!')




