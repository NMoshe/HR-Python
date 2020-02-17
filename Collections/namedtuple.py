from collections import namedtuple

if __name__ == '__main__':
    num = int(input())
    colum = input()
    marks = 0
    Student = namedtuple('Student', colum)
    for x in range(num):
        student = Student(*input().split())
        marks += int(student.MARKS)
    print(marks / num)
