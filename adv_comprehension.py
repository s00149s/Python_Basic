def list_comprehension():
    """
    리스트 내포
    Syntax: [ 표현식 for 변수 in 순차형 if 조건식]
    """
    # 1 ~ 10 까지의 리스트가 있을 때, 내부 항목을 제곱한 새로운 리스트 생성
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []

    # 1. for문
    for num in nums:
        result = num * num
        results.append(result)
    print("FOR 결과: ", results)

    # 2. list 내포
    results = [ num * num for num in nums]
    print("내포 결과 : ", results)

    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    # strings의 요소 중에서 문자열의 길이가 3이하인 문자열 리스트 생성
    # for문 ver.
    results = []
    for item in strings:
        if len(item) <= 3:
            results.append(item)
    print("FOR 결과: ", results)

    # list 내포 ver.
    results = [item for item in strings if len(item) <= 3]
    print("내포 결과 : ", results)

    # 1 ~ 100까지의 수 중에서 짝수의 리스트 생성
    evens = [i for i in range(1, 101) if i % 2 == 0]
    print("짝수 리스트: ", evens)

def set_comprehension():
    # Syntax : { 표현식 for 변수 in 순차형 if 조건식 }
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    # strings의 요소 중에서 문자열의 길이가 3이하인 문자열 SET 생성
    results = { item for item in strings if len(item) <= 3}
    print("SET 결과 : ", results)

    # strings의 요소의 문자열 길이를 set으로 저장
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    results = { len(item) for item in strings}
    print(results)

def dict_comprehension():
    # Syntax: { 키표현식 : 값표현식 for 변수 in 순차형 if 조건식}
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    # strings의 값 -> 키, 값의 길이 -> 값 으로 받는 새로운 사전 생성
    dct = { item : len(item) for item in strings}
    print(dct)







if __name__ == "__main__":
    # list_comprehension()
    # set_comprehension(
    dict_comprehension()