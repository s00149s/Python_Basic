def score_input():
    score1 = int(input("점수1을 입력하세요"))
    score2 = int(input("점수2를 입력하세요"))
    if score1 >= 50 and score2 >= 50 and (score1 + score2)/2 >= 60:
        message = "합격"
    else:
        message = "불합격"
    print(message)



if __name__ == "__main__":
    score_input()