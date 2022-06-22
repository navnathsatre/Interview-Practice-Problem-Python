try:
    r = 10/0
    print(r)
except ZeroDivisionError as e:
    print("Sorry", e)
except Exception as e:
    print("error", e)
else:
    print("There is no exception")
finally:
    print("I run always")
