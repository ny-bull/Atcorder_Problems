C = []

for n in range(3):
    C.append(list(map(int,input().split())))

ans = False

if (C[0][0] - C[0][1]) == (C[1][0] - C[1][1]) == (C[2][0] - C[2][1]):
    if (C[0][1] - C[0][2]) == (C[1][1] - C[1][2]) == (C[2][1] - C[2][2]):
        if (C[0][0] - C[1][0]) == (C[0][1] - C[1][1]) == (C[0][2] - C[1][2]):
            if (C[1][0] - C[2][0]) == (C[1][1] - C[2][1]) == (C[1][2] - C[2][2]):
                ans = True
