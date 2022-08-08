#Computer quiz game
score = 0
print('Welcome to the computer quiz game!')
print('----------------------------------')
name = input('What\'s your name? ')
ask = input(f"Hi {name} do you wanna play the quiz game? ")
if ask.lower() != "yes":
    print("as you wish!")
    quit()

print("Ok let's play :)")

quest_1 = input("What does CPU stands for? ")
if quest_1.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_2 = input("What does PSU stand for? ")
if quest_2.lower() == "power supply":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_3 = input('What does GPU stand for? ')
if quest_3.lower() == 'graphics processing unit':
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_4 = input("What does RAM stand for? ")
if quest_4.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("That's wrong!")
quest_5 = input('What does ROM stand for? ')
if quest_5.lower == 'read-only memory' or quest_5 == 'read only memory':
    print('correct!')
    score += 1
else:
    print('That\'s wrong!')


print(f'Your score is {score}/5')
if score == 5:
    print('You rock!')




