from pkg_resources import invalid_marker


try:
    answer=10/0
    x=int(input ("enter a text"))
    print(x)
except ZeroDivisionError as fatal:
    print("fatal")
except  ValueError:
    print("wrong value")

  