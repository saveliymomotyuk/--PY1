money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
moneygrow = 1.05
moneyspend = salary - spend
while money_capital + moneyspend >= spend:
    money_capital += moneyspend
    spend = spend * moneygrow
    month += 1

print(month)
