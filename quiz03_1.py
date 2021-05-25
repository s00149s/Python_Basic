def q3_1():
    while True:
        num = input("수를 입력하세요")

        try:
            int(num)    # 캐스팅
        except:
            print("정수가 아닙니다, 다시 입력하세요")
        else:   #try 블록에 예외 없을때
            break

    total = 0
    to = int(num)

    # for i in range(1, to + 1):  # 1 ~ to
    #     if i % 3 == 0:
    #         total += i

    lst = [i for i in range(1, to + 1) if i % 3 == 0]   # 3의 배수 리스트 만들기
    total = sum(lst)

    print("1부터 {}까지의 3의 배수의 합 = {}".format(to, total))


def q3_2(): # isinstance 연습
    lst = [1, 3.14, 'python', 7, 89.1, 3]
    # lst_cleaned = []
    # for item in lst:
    #     if isinstance(item, (int, float)):
    #         lst_cleaned.append(item)
    lst_cleaned = [item for item in lst if isinstance(item, (int, float))]
    print("cleaned : ", lst_cleaned)

def summary(*args): # 가변인수 연습문제
    total = sum(args)
    return total, max(args), min(args), total / len(args)

def q3_3():
    total, maxval, minval, avg = summary(80, 75, 90, 85, 85)
    print(total, maxval, minval, avg)

def q3_4():
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""

    # wjdwp
    s = s.replace(",", "").replace(".", "").replace("\n", "").upper()
    splits = s.split()
    print("splits : ", splits)

    summary = {}    # 결과 dict
    for word in splits:
        if word in summary.keys():  # 이미 키에 있으면
            summary[word] += 1
        else:   # 키가 없으면
            summary[word] = 1

    for key, value in summary.items():  # (key, value) 쌍튜플 반환
        print("{}:{}".format(key, value))


if __name__ == "__main__":
    # q3_1()
    # q3_2()
    q3_3()
    # q3_4()