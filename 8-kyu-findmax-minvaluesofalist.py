
# 8 kyu Find Maximum and Minimum Values of a List
my_min = min
my_max = max
def min(arr):
    global my_min 
    return my_min(arr)
    
def max(arr):
    global my_max 
    return my_max(arr)


print(remove_char(max([4,6,2,1,9,63,-134,566])), 566)
print(remove_char(min([-52, 56, 30, 29, -54, 0, -110])), -110)
print(remove_char(max([5])), 5)
print(remove_char(min([42, 54, 65, 87, 0])), 0)
