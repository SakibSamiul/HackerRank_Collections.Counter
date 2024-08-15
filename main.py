# from collections import Counter

# X = (input())
# X_sizes = list(map(int, input().split()))

# N_customers = int(input())
# totalprice = 0

# for i in range(N_customers):
#     size, price = map(int, input().split())

#     if size in X_sizes:
#         totalprice += price

#         X_sizes.remove(size)
# price(totalprice)


from collections import Counter
def counter(sizes, n):

    total_amount = 0
    for _ in range(n):
        size, price = list(map(int, input().split()))

        if sizes[size]:
            sizes[size] -= 1
            total_amount += price

    print(total_amount)

if __name__ == '__main__':
    x = int(input())
    sizes = Counter(map(int, input().split()))
    n = int(input())
    counter(sizes, n)