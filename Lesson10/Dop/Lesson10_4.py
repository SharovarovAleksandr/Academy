import sys
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print (" Недопустима операція ділення на 0 ",file=sys.stderr)
        return 0


print(div(10,0))