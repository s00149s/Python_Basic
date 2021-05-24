def gugu():
    for i in range(2, 10):
        print(i, "단")
        for x in range(2,10):
            print(i, "*", x, "=", i * x)

if __name__ == "__main__":
    gugu()