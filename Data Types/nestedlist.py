if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    newStudents = sorted(students, key=lambda x: (x[1], x[0]))

    names = [i[0] for i in newStudents]
    marks = [i[1] for i in newStudents]
    minMark = min(marks)

    while marks[0] == minMark:
        marks.remove(marks[0])
        names.remove(names[0])

    for x in range(0, len(marks)):
        if marks[x] == min(marks):
            print(names[x])
