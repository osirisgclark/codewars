def sum_two_smallest_numbers(numbers):
    l= list()
    m= list()
    l.append(min(numbers))
    for x in numbers:
        if x not in l:
            m.append(x)
    l.append(min(m))
    q= sum(l)
    return q


print(sum_two_smallest_numbers([19,5,42,2,77]))
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)
print(sum_two_smallest_numbers([1, 8, 12, 18, 5]), 6)
print(sum_two_smallest_numbers([13, 12, 5, 61, 22]), 17)


# BEST:
# def sum_two_smallest_numbers(numbers):
#     return sum(sorted(numbers)[:2])

# def sum_two_smallest_numbers(num_list):
#     num_list.sort()
#     return num_list[0] + num_list[1]