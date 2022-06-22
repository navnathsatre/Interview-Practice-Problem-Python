try:
    with open("city.txt", 'r') as fo:
        print(fo.read())
    res = 2 + 3
    print(res)
    r = 10 / 0
    print(r)
except FileNotFoundError as e:
    print("Got an error while reading a file : ", e)
except TypeError as e:
    print("An issue occurred: ", e)
except ZeroDivisionError as e:
    print("Can't divide by 0 , ", e)
except Exception as e:
    print("Caught by the general exception: ", e)
else:
    print("There is no exception hence else has run!")
finally:
    print("I run always , I am finally ")
