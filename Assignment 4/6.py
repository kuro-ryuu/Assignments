import random
points = int(input("How many random points do you want to generate?: "))
in_circle = 0
for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        in_circle += 1
pi = 4*in_circle/points
print(f"The approximation of pi is {pi}")
