__author__ = 'rezenter'


def simple(num):
    a = 2
    while a <= pow(num, 1/2):
        if num % a == 0:
            return False
        a += 1
    return True


number = int(input())


def divs(n):
    i = 1
    result = []
    while i <= pow(n, 1/2):
        if simple(i):
            if n % i == 0:
                if simple(n/i):
                    result.append([i, int(n/i)])
        i += 1
    return result
r = []
counter = 1
while counter <= number:
    if len(divs(counter)) >= 1:
        r.append(counter)
    counter += 1
print(r)
