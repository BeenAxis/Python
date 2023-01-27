from calendar import monthrange
print("Год: ")
year = int(input())
result = 0
for i in range(1, 13):
    days = monthrange(year, i)[1]
    print(f"В месяце {i} = {days} дней")
    for y in range(1, days+1):
        str = f"{y}"
        if len(str) == 1:
            result += int(str)
        else:
            one = str[0]
            two = str[1]
            result += int(one) + int(two) 
print(f"Сумма: {result}")