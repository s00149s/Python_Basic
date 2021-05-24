def infinite_loop():


    while True:
        v = str(input("please [q to quit]: "))
        total = 0
        if v == "q":
            break
        if v == "d":
            price = int(input("price"))
            total += price
            print("method: ", v)
            print("Amount: ", price)
            print("Balance: ", total + price)

        elif v == "w":
            price = int(input("price"))
            print("method: ", v)
            print("Amount: ", price)
            total -= price
            print("Balance: ", total)
        else:
            print("?")

















if __name__ == "__main__":
        infinite_loop()