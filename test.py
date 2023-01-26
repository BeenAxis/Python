
#Сумма всех
print('Введите знак: ')
znak = input()
result = 0
format = ""
while True:
    print('Введите число: ')
    num = int(input())
    if result == 0:
        result = num
        format = f"{num}"
    elif num == 0:
        break
    else:
        if znak == "+":
            result += num
        elif znak == "-":
            result -= num
        elif znak == "/":
            result /= num
        elif znak == "*":
            result *= num
        format += f" {znak} {num}"
print(f'Результат {format} = {result}')
