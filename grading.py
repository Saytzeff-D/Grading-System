def grade(): 
    score_1 = input("What's your CA score: ")
    score_2 = input("Enter your Exam score: ")
    result = int(score_1) + int(score_2)
    if result > 100:
        print(f"Your score is {result} but it is impossible to define your Grade!")
    elif result == 100:
        print(f"Bravo! You had a perferct score.")
    elif result >= 70:
        print(f"Your score is {result} and your Grade is A")
    elif result >=60:
        print(f"Your score is {result} and your Grade is B")
    elif result >= 50:
        print(f"Your score is {result} and your Grade is C")
    elif result >=45:
        print(f"Your score is {result} and your Grade is D")
    elif result >=40:
        print(f"Your score is {result} and your Grade is E")
    else: 
        print(f"Your score is {result} and your Grade is F")

grade()