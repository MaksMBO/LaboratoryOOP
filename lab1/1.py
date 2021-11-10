import sys

argument = sys.argv[1:]

try:
    print(eval(" ".join(argument)))
except SyntaxError:
    print("None")
except NameError:
    print("None")
except ZeroDivisionError:
    print("None")
