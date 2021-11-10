import sys

argument = sys.argv[1:]

arithmetic = {"add": "+",
              "sub": "-",
              "mul": "*",
              "div": "/"}
try:
    a = str(argument[0])
    print(eval(arithmetic[a].join(sys.argv[2:])))

except SyntaxError:
    print("None")
except NameError:
    print("None")
except KeyError:
    print("None")
except IndexError:
    print("None")
except ZeroDivisionError:
    print("None")
