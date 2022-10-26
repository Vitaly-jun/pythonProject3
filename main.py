num_tickets = 0
age_tickets = []
while num_tickets <= 0:
    try:
        num_tickets = int(input("Количество билетов которые вы хотите приобрести?: "))
        if num_tickets < 0:
            raise ValueError()
    except ValueError:
        print("Введено некорректное значение!")
try:
    age_tickets = [int(input(f"Введите возраст посетителя для билета {i + 1}: ")) for i in range(int(num_tickets))]
except ValueError:
    print("Введено некорректное значение!")
count = 0
for j in age_tickets:
    if 0 < j < 18:
        count += 0
    elif 18 <= j <= 25:
        count += 990
    elif j > 25:
        count += 1390
    elif j < 0:
        print("Введено некорректное значение!")
        break
print(f"Итого к оплате: {count}")
sale = count
if num_tickets >= 3:
    print(f"Итого к оплате со скидкой: {int(sale * 0.9)}")
