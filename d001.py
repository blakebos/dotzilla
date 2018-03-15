n = input('Specify a number:')

print("\n".join((i*"*").center(n*2) for i in range(1, n*2, 2)))