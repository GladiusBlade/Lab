prev = int(input())
cur = int(input())

used = cur - prev

if used < 0:
    used += 10000

if used <= 300:
    cost = 21000
elif used <= 600:
    cost = 21000 + (used - 300) * 60
elif used <= 800:
    cost = 39000 + (used - 600) * 40
else:
    cost = 47000 + (used - 800) * 25

pay = ((cost + 5) // 10) / 100

avg = pay / used


print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(prev, cur, used, f"{pay:.2f}", f"{avg:.2f}")
