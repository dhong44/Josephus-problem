def winner(n):
    if n == 2:
        return 1

    if n % 2:
        if winner((n+1)/2) == 1:
            return n
        else:
            return winner((n+1)/2) * 2 - 3

    else:
        return winner(n/2) * 2 - 1

while(True):
    n = input()
    print winner(n)
