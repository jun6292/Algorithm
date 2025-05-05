str = input()
for alpha in str:
    if 'a' <= alpha <= 'z':
        alpha = alpha.upper()
    else:
        alpha = alpha.lower()

    print(alpha, end='')
