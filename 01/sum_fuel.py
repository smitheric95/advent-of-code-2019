import math

def fuel_requirement(mass):
    req = mass // 3 - 2

    if req <= 0:
        return 0

    return fuel_requirement(req) + req

if __name__ == "__main__":
    fuel_sum = 0

    with open("input.txt") as f:
        for mass in f:
            fuel_sum += fuel_requirement(int(mass))

    print(fuel_sum)