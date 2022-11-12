from random import sample
start = -10
stop = 10
count = 15
def get_unique_list_numbers() -> list[int]:
    list_numbers = [i for i in range(start,stop +1)]
    uniqie = sample(list_numbers, count)
    return uniqie








list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
