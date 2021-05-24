# 함수 정의 연습
def dummy():    # 함수 구현부가 없을 때
    pass

def my_function():
    print("Hello Python")   # 끝날 때까지 함수 종료시킬 필요 없을 때, return 생략 가능

def times(a, b):    # 입력은 인수로 전달
    return a * b    # 반환할 값이 있을 때는 return으로 반환

def none():
    return  # 반환 없이 return문만 사용 -> None 반환(함수의 중단)

dummy()
print(dummy())  # None -> return 없음
print(times(10, 20))
print(none())


# 함수도 객체다
# 함수도 다른 객체와 동등하게 변수에 할당될 수 있고
# 다른 함수의 인수로 전달될 수 있다
fun = times # time 함수의 참조 주소를 fun에 할당
print(fun(10, 20), type(fun))
# 실행 가능 객체(function)인지 확인 -> collable
print("fun is callable? ", callable(fun))   # 전달 받은 객체가 함수인지 확인

# 응용
if callable(fun):
    print(fun(10, 20))  # 실행 가능한 객체인지를 확인한 후 호출

# 기본적으로 return은 한 개의 객체 반환
def max_value(a, b):
    if a > b:
        return a
    else:
        return b

print(max_value(10, 20))

# return 문으로 여러 개의 객체(결과) 반환 가능 -> 튜플로 패킹되어서 반환됨

def swap(a, b):
    return b, a # tuple로 패킹되어 반환

print(swap(10, 20), type(swap(10, 20)))

c, d = swap(10, 20) # unpacking으로 여러 값을 전달 받을 수 있다
print(c, d)