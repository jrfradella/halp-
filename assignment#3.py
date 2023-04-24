score = input("enter score between 0.0 and 1.0: ")

grades = {"A": 0.9, "B": 0.8, "C": 0.7, "D": 0.6, "F": 0}


def check_score(score):
    for grade_letter, minimum_grade in grades.items():
        if score >= minimum_grade:
            return grade_letter


try:
    score = float(score)
    print(f"Score: {score*100}% | Grade: {check_score(score)}")
except Exception as e:
    print(f"Got this error: {e}")
