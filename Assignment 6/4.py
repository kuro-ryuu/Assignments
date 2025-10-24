import random

def int_list(num: list[int]):
    return (sum(num))

numlist = [random.randint(1, 10) for _ in range(5)]
print(f"The sum of {numlist} is: {int_list(numlist)}")
