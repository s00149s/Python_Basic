def quiz01_3():
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
    students[0]['average'] = round(sum(list(students[0].values())[1:4])/len(list(students[0].values())[1:4]), 2)


    students[1]['total'] = sum(list(students[1].values())[1:4])
    students[1]['average'] = round(sum(list(students[1].values())[1:4]) / len(list(students[1].values())[1:4]), 2)

    print(students)




if __name__ == "__main__":
    quiz01_3()