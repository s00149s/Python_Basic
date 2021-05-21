def quiz01_2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    slice = lst[3:7]
    print(slice)
    print(sorted(slice, reverse=True))

    lst[3:7] = sorted(slice, reverse=True)
    print(lst)



if __name__ == "__main__":
    quiz01_2()