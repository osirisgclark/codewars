#7 kyu Lost number in number sequence
def find_deleted_number(arr, mixed_arr):
    return sum(arr)-sum(mixed_arr)
 

print(find_deleted_number([1,2,3,4,5,6,7,8,9], [3,2,4,6,7,8,1,9]), 5)