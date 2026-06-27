# The General Knowledge Quiz
score = 0
answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")
    
answer = input("2. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

answer = input("3. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

print("\nQuiz Completed!")
print("Your final score is:", score, "/3")