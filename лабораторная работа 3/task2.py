list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_ = 0
for number in range(len(list_numbers)):
    numbermax = list_numbers[max_]
    anynumber = list_numbers[number]
    if anynumber > numbermax:
        max_ = number



list_numbers[max_], list_numbers[-1], = list_numbers[-1], list_numbers[max_]
print(list_numbers)

