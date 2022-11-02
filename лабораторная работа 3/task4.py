salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need = 0  # количество денег, чтобы прожить 10 месяцев

moneygrow = increase + 1
for money in range(1, months +1):
    money = spend - salary
    spend = spend * moneygrow
    need += money

print(round(need))
