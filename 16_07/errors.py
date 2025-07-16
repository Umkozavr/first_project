def calc(x,y):
    try:
        return int(x) / int(y)
    except(ZeroDivisionError, ValueError) as err:
        print(x, y)
        raise err
        # print(err)
        # print("Error")

    # except ZeroDivisionError:
    #     print("Can't divide by zero")
    # except ValueError:
    #     print("Input the numbers, please")


print(calc(input("Number: "), input("Number: ")))
print("hello")

