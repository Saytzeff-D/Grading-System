score_1 = input("What's your CA score: ")
score_2 = input("Enter your Exam score: ")
score_3 = 79

def grade(): 
    result = int(score_1) + int(score_2)
    if result >= 70:
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