x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 > 0 and y1 > 0:
    q1 = "I"
elif x1 < 0 and y1 > 0:
    q1 = "II"
elif x1 < 0 and y1 < 0:
    q1 = "III"
else:
    q1 = "IV"

if x2 > 0 and y2 > 0:
    q2 = "I"
elif x2 < 0 and y2 > 0:
    q2 = "II"
elif x2 < 0 and y2 < 0:
    q2 = "III"
else:
    q2 = "IV"

if q1 == q2:
    print("Yes, " + q1)
else:
    print("No")
