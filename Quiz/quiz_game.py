questions = ("how many elements are in the periodic table?: ",
             "which animal lays the largest eggs? ",
             "what is the most abundant gas in the atmosphere? : ",
             "how many bones in the human body?: ")

options = (("A.116", "B.117", "C.118", "D.119"),
           ("A.whale", "B.crocodile", "C.elephant", "D.ostrich"),
           ("A.N2", "B.O2", "C.NO2", "D.H2"),
           ("A.205", "B.206", "C.207", "D.208"))

answers = ("C", "D", "A", "B")

guesses = []
score = 0
question_number = 0

for question in questions:
    print("----------------")
    print(question)
    for option in options[question_number]:
     print(option)

    guess = input("Enter the answres: ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("Right answers")
    else:
       print("Incorrect!")
       print(f"{answers[question_number]} is the right answers")

    question_number += 1

print("----------")
print("Result")
print("---------")

print("answers: ", end=" ")
for ans in answers:
    print(ans, end=" ")
print()

print("guesses: ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score/len(questions) * 100)
print(f"your score is: {score}% ")