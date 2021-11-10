def solution(roominess_backpack, backpack, quantity):
    if quantity == 0 or roominess_backpack == 0:
        return False
    if backpack[quantity - 1] > roominess_backpack:
        return solution(roominess_backpack, backpack, quantity - 1)
    else:
        return max(
            backpack[quantity - 1] + solution(roominess_backpack - backpack[quantity - 1], backpack, quantity - 1),
            solution(roominess_backpack, backpack, quantity - 1))


bag = []
try:
    roominess = int(input("Roominess: "))
    number = int(input("Number: "))

    for i in range(0, number):
        ingot = int(input("Ingot: "))
        bag.append(ingot)

    if solution(roominess, bag, number):
        print(solution(roominess, bag, number))
    else:
        print("Something went wrong")
except ValueError:
    print("You did not enter incorrect data!")
except IndexError:
    print("None")
