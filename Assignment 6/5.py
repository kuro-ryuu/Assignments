import random
x = []
def int_list(num: list[int]):
    even_only = [i for i in num if i % 2 == 0]
    return even_only

numlist = [random.randint(1, 10) for _ in range(5)]
uneven_numbers = int_list(numlist)
print(f'Original: {numlist}')
print(f'Filtered: {uneven_numbers}')

