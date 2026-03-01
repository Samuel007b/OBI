H = int(input())
M = int(input())
S = int(input())
T = int(input())
S += T
if S >= 60:
    M += S/60
    S %= 60
    if M >= 60:
        H += M/60
        M %= 60
        if H >= 24:
            H %= 24
print(f'{int(H)}\n{int(M)}\n{int(S)}')