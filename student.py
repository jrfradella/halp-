from random import uniform

GRADES = [("A", 0.9), ("B", 0.8), ("C", 0.7), ("D", 0.6), ("F", 0)]
NAMES = ["Tanner", "Erin", "Joey", "Jo-el"]
NUM_SCORES = 20
STUDENTS = []


class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.scores = []
        self.grades = []

    def grade(self, score: str | float):
        score = float(score)
        for grade_score in GRADES:
            grade = grade_score[0]
            min_score = grade_score[1]
            if score >= min_score:
                self.scores.append(score)
                self.grades.append(grade)
                break


if __name__ == "__main__":
    for student_name in NAMES:
        student = Student(student_name)
        for i in range(NUM_SCORES):
            score = round(uniform(0.01, 1.00), 2)
            student.grade(score)
        STUDENTS.append(student)

    student_name = input("Enter your name: ")
    score = input("Enter your score: ")
    student_scored = False
    for student in STUDENTS:
        if student_name == student.name:
            student.grade(score)
            student_scored = True
    if not student_scored:
        student = Student(student_name)
        student.grade(score)
        STUDENTS.append(student)

    for student in STUDENTS:
        print("-" * 50)
        average_score = round(sum(student.scores) / len(student.scores), 2)
        print(student.name)
        print(f"Average Score: {average_score}")
        for grade in GRADES:
            grade = grade[0]
            print(f"Qty {grade}: {student.grades.count(grade)}")
