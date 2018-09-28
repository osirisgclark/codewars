#7 kyu Sort the climbing grades
# Sort una lista pr otra

def sort_grades(lst):
	k = ['VB', 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5','V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17']
	return [x for x in k if x in lst]#+[x for x in n if x not in k]
return sorted(lst, key=lambda x: k.index(x))

#If there a elements that are not in k you can use this return
#return [x for x in k if x in lst]+[x for x in n if x not in k]
print(sort_grades(['V4', 'V10', 'V5', 'V2']), ['V2', 'V4', 'V5', 'V10'])
print(sort_grades([]), [])
print(sort_grades(['V1']), ['V1'])    
print(sort_grades(['V7', 'V12', 'V1']), ['V1', 'V7', 'V12'])
print(sort_grades(['V13', 'V14', 'VB', 'V0']), ['VB', 'V0', 'V13', 'V14'])    
print(sort_grades(['V0+', 'V0', 'V16', 'V2', 'VB', 'V6']), ['VB', 'V0', 'V0+', 'V2', 'V6', 'V16'])  