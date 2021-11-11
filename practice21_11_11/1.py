import os
import timeit

# with open('asd.txt', 'w') as open_file:
#     while os.path.getsize('asd.txt') / 1000000 < 50:
#         open_file.write(
#             '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890\n')



s="""
with open("asd.txt") as file:
    sum = 0
    lines = file.readlines()
    for symbol in lines:
        if symbol.strip().isdigit():
            sum += int(symbol.strip().isdigit())"""

print(timeit.timeit(s, number=1))

s = """
with open("asd.txt") as file:
    sum = 0
    for line in file:
        if line.strip().isdigit():
            sum += int(line.strip().isdigit())
"""
print(timeit.timeit(s, number=1))

s ="""
with open("asd.txt") as file:
    s = 0
    k = (int(symbol.strip()) for symbol in file if symbol.strip().isdigit())
    s = sum(k)
"""


print(timeit.timeit(s, number=1))