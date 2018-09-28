#7 kyu Simple Fun #22: Is Smooth?
def is_smooth(n):
    return True if len(n)%2 ==0 and n[len(n)//2]+n[len(n)//2-1]==n[0]==n[-1] or n[len(n)//2]==n[-1]==n[0] else False