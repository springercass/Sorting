def foo(a=[]):
    a.append(5)

    return a


#

# contant time
# O(1) -> 'Order 1' Big-O Notation


def process1(l):
    first_val = l[0]

    return first_val


def process2(l):
    t = 0

    for v in l:
        t += v

    return t


def process3(n):
    for _ in range(n):
        pass


def process4(n):
    for _ in range(n**2):
        pass


print(process4(8000))


def process5(l):
    t = 0           # O(1)

    t += l[0]       # O(1)
    t += l[1]       # O(1)

    return t        # O(1)

# O(1 + 1 + 1 + 1) == O(4) == O(4 * 1)


def process6(l):
    t = 0               # O(1)

    t += l[0]           # O(1)

    for i in l:         # O(n) -> loops get O(number_of_loops)
        t += 1

    t += l[1]           # O(1)

    return t            # O(1)

# O(1 + 1) + O(n * 1) + O(1 + 1)
# O(1) + O(n)
# O(n + 1)
