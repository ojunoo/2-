class Student:
    def __init__(self, student_id, name, english, c_prog, python):
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_prog = c_prog
        self.python = python
        self.total = self.calculate_total()
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total(self):
        return self.english + self.c_prog + self.python

    def calculate_average(self):
        return self.total / 3

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B+"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"{self.student_id}\t{self.name}\t{self.english}\t{self.c_prog}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"


def assign_ranks(students):
    sorted_students = sorted(students, key=lambda x: x.total, reverse=True)
    for idx, student in enumerate(sorted_students):
        student.rank = idx + 1


def main():
    students = []
    for _ in range(5):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어 점수: "))
        c_prog = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))
        students.append(Student(student_id, name, english, c_prog, python))
    
    assign_ranks(students)
    
    print("\n성적관리 프로그램")
    print("=" * 70)
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 70)
    for student in students:
        print(student)

if __name__ == "__main__":
    main()