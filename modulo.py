n_list = []

for n in range(100, 1000):
    # print(n%7==0 or n%9==0)
    if n%7==0 or n%9==0:
        n_list.append(n)

n_25 = n_list[-25:]

print(n_25)  # think about another solution that need less iterations