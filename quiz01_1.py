def q1_1(): # replace로 콤마, 공백 제거해서 알파벳을 리스트, 셋에 담기
    s = "Life is too short, You need Python"
    lst = list(s.lower().replace(",", "").replace(" ", ""))
    chars = set(lst)
    print(chars)
    lst = list(chars)
    print(sorted(lst))
    print(len(lst))


def q1_2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice = lst[3:7]
    print(slice)
    print(sorted(slice, reverse=True))

    lst[3:7] = sorted(slice, reverse=True)
    print(lst)

    """
    slice = lst[3:7]
    slice.reverse()
    lst[3:7] = slice
    
    print(list)
    print(lst == [1, 2, 3, 7, 6, 5, 4, 8, 9, 10])
    """


def q1_3(): # 루프 돌리기

    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]
    print(students, type(students))
    print("================================================================")

    students[0]['total'] = sum(list(students[0].values())[1:4])
    students[0]['average'] = round(sum(list(students[0].values())[1:4]) / len(list(students[0].values())[1:4]), 2)

    students[1]['total'] = sum(list(students[1].values())[1:4])
    students[1]['average'] = round(sum(list(students[1].values())[1:4]) / len(list(students[1].values())[1:4]), 2)

    print(students)


    """
    for student in studnets:
        total = student.get("kor") + student.get("eng) + student.get("math")
        average = total / 3
        student['total'] = total
        student['average'] = average
    
    print(students) 
    """


if __name__ == "__main__":
    # q1_1()
    # q1_2()
    q1_3()