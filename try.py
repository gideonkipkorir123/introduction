from pkg_resources import invalid_marker


try:
    x=int(input ("enter a text"))
    print(x)
except ZeroDivisionError:
    print("division by zero")
except  ValueError:
    print("wrong value")

  