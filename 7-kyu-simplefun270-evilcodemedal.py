#7 kyu Simple Fun #270: Evil Code Medal


def evil_code_medal(user_time, gold, silver, bronze):
	(l, l1, l2, l3) = (user_time.split(':'), gold.split(':'), silver.split(':'), bronze.split(':'))
	(ut, g, s, b) = ((int(l[0])*3600) + (int(l[1])*60) + int(l[2]), (int(l1[0])*3600) + (int(l1[1])*60) + int(l1[2]), (int(l2[0])*3600) + (int(l2[1])*60) + int(l2[2]), (int(l3[0])*3600) + (int(l3[1])*60) + int(l3[2]))
	return 'Gold' if ut<g else 'Silver' if ut<s else 'Bronze' if ut<b else 'None'
	
print(evil_code_medal("01:15:00","00:15:00","00:45:00","01:15:00"),"None")
print(evil_code_medal("00:30:00","00:15:00","00:45:00","01:15:00"),"Silver")
print(evil_code_medal("00:00:01","00:00:10","00:01:40","01:00:00"),"Gold")
print(evil_code_medal("00:10:01","00:00:10","00:01:40","01:00:00"),"Bronze")
print(evil_code_medal("00:00:01","00:00:02","00:00:03","00:00:04"),"Gold")
# print(userTime("00:14:59"), 'gold')
# print(userTime("00:15:00"), 'gold')
# print(userTime("00:15:01"), 'silver')
# print(userTime("00:44:59"), 'silver')
# print(userTime("00:45:00"), 'silver')
# print(userTime("00:45:01"), 'bronze')
# print(userTime("01:14:59"), 'bronze')
# print(userTime("01:15:00"), 'bronze')
# print(userTime("01:15:01"), 'None')
# print(userTime("11:15:00"), 'None')

# import datetime
# # n = "00:14:99"
# # n = "00:15:00"
# n = "00:44:99"
# # n = "01:15:00" 
# l = n.split(':')
# ts = (int(l[0])*3600) + (int(l[1])*60) + int(l[2])
# print (ts)


#  gold = "00:15:00",
# silver = "00:45:00" 
#  bronze = "01:15:00"