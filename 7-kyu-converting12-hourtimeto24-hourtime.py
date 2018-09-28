
from datetime import datetime
def to24hourtime(hour, minute, period):
	l = list()
	l.append(str(hour))
	l.append(str(minute))
	l.append(str(period))
	k = ':'.join(l)
	in_time = datetime.strptime(k, "%I:%M:%p")
	out_time = datetime.strftime(in_time, "%H%M")
	return out_time



print(to24hourtime(8, 30, "am" ))
print(to24hourtime(8, 30, "pm" ))