#6 kyu Multiples of 3 and 5

def solution(number):
    l = list()
    for n in range(1, number):
        if n % 5 == 0 or n % 3 == 0:
            l.append(n)
    return sum(l)


print(solution(10), 23)