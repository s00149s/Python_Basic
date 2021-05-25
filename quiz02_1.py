def q2_1():
    score1 = int(input("점수1을 입력하세요"))
    score2 = int(input("점수2를 입력하세요"))
    if score1 >= 50 and score2 >= 50 and (score1 + score2)/2 >= 60:
        message = "합격"
    else:
        message = "불합격"
    print(message)

    """
    score1 = int(input("점수1: "))
    score2 = int(input("점수2: "))
    average = (score1 + score2) / 2
    
    if score 1>= 50 and score2 >= 50 and\
        average >= 60:
        message = "합격"
        
    else:
        message = "불합격"
    
    print(message)
    """

def q2_2():
    for i in range(2, 10):  # 2 ~ 9 단
        print(i, "단")
        for x in range(2,10):
            print(i, "*", x, "=", i * x)


def q2_3(): # 무한 루프 : while 문 (continue, break 연습)
    balance = 0 # 잔액변수 : while문 밖에 넣어야 누적됨
    while True:
        method = input("method: ")
        method = method.lower()
        if method == "q":
            break   # 루프 종료
        if method != "d" and method != "w":
            print("?")
            continue

        # d, w만 남음
        # 금액 입력
        amount = int(input("Amount:"))

        if method == "d" :  # 입금
            balance += amount
        else:   # 출금
            balance -= amount

        # balance += amount if method == "d" else -amount

        print("Balance: ", balance)


    print("프로그램 종료")



if __name__ == "__main__":
    # q2_1()
    # q2_2
    q2_3()