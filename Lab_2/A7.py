x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
W1 = (x1 + y1) % 2 == 0
W2 = (x2 + y2) % 2 == 0
if W1 == W2:
    print("YES")
    if W1:
        print("White")
    else:
        print("Black")
else:
    print("NO")
