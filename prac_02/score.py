import random

def main():
    """The main function to ask score and print result"""
    score = float(input("Score: "))
    result = evaluate_score(score)
    print(result)

def evaluate_score(score):
    """evaluate the parameter of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return"Passable"
    else:
        return"Bad"
main()