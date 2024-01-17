def get_data():
    students = int(input("How many Students: "))
    students_data = dict()
    for i in range(students):
        name = input(f'Enter name of student {i+1} : ')
        marks = int(input(f'Enter marks of student {i+1} : '))
        students_data[name]=marks

    return students_data


def ranksstudents(students_data):
    marks_lst = []
    name_lst = []
    top_three = []
    top_three_marks = []

    for i in students_data:
        marks_lst.append(students_data[i])
        name_lst.append(i)
    for j in range(3):
        name_index = marks_lst.index(max(marks_lst))
        top_three.append(name_lst[name_index])
        top_three_marks.append(marks_lst[name_index])
        name_lst.pop(name_index)
        marks_lst.pop(name_index)
        print(f"{j+1} position goes to {top_three[j]} with marks: {top_three_marks[j]}")
    return top_three,top_three_marks


def appreciationmessage(top_three,top_three_marks):
    for i in range(len(top_three)):
        print(f"Appreciation msg for {top_three[i]} with marks {top_three_marks[i]} for securing {i+1} position")


students_data = get_data()
top_three, top_three_marks = ranksstudents(students_data)
appreciationmessage(top_three,top_three_marks)
