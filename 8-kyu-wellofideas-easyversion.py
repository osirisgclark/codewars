#8 kyu Well of Ideas - Easy Version

def well(x):
    l= list()
    for n in x:
        if n=='good':
            l.append(n)
    if len(l)>=3:
        return 'I smell a series!'
    elif len(l)==2 or len(l)==1:
        return 'Publish!'
    else:
        return 'Fail!'



#Optimo
def well(x):
    l= list()
    for n in x:
        if n=='good':
            l.append(n)
    return 'I smell a series!' if len(l) > 2 else 'Publish!' if len(l) else 'Fail!'


print(well(['bad', 'bad', 'bad']), 'Fail!')
print(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')



#return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'