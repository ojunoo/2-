def avg(total_score):
    average = []
    for score in total_score:
       average.append(score/3)
    return average
    
def calculate_grade(avg):
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
    
def print_result(student_ids, names, total_scores, averages, grades):
    """학생 정보를 표 형식으로 출력하는 함수"""
    print("\n성적관리 프로그램")
    print("=" * 70)
    print("학번\t이름\t총점\t평균\t학점")
    print("=" * 70)

    for i in range(len(student_ids)):
        print(f"{student_ids[i]}\t{names[i]}\t{total_scores[i]}\t{averages[i]:.2f}\t {grades[i]}")  # 평균을 소수점 2자리까지 출력

    print("=" * 70)

def main():
    total_score = []       #총점
    student_ids = []        #학번
    names = []              #이름    
    for _ in range(5):
        student_id = input("학번: ")
        name = input("이름: ")  
        english = int(input("영어 점수: "))
        c_prog = int(input("C-언어 점수: "))
        python = int(input("파이썬 점수: "))

        total = (english + c_prog + python)
        student_ids.append(student_id)
        names.append(name)
        total_score.append(total)

    average = avg(total_score)
    grade = [calculate_grade(a) for a in average]
    
    print_result(student_ids, names, total_score, average, grade)

main()
    

        
    