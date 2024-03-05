print("Welcome to my software abbreviations quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does IDE stand for? ")
if answer.lower() == "integrated development environment":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application programming interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does SQL stand for? ")
if answer.lower() == "structured query language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got", score, "questions correct!")
percentage = (score / 4) * 100
print("You got", percentage, "%.")
