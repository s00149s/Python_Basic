def quiz01_1():
    str = "Life is too short, You need Python"
    lst = list(str.lower().replace(",", "").replace(" ", ""))
    chars = set(lst)
    print(chars)
    lst = list(chars)
    print(sorted(lst))
    print(len(lst))


if __name__ == "__main__":
    quiz01_1()