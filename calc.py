score_1 = float(input("Enter a number: "))
score_2 = float(input("Enter another number: "))

def calc():     
    print(f"Your addition is {score_1 + score_2}")       
    print(f"Your subtraction is {score_1 - score_2}")
    print(f"Your multiplication is {score_1 * score_2}")
    print(f"Your exponential is {score_1 ** score_2}")
    print(f"Your division is {score_1 / score_2}")
    print(f"Your floor division is {score_1 // score_2}")

calc()