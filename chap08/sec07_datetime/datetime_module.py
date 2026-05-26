from datetime import datetime

now = datetime.now()
print(now)

str_now = now.strftime("%Y.%m.%d")
print(str_now)

print("year:", now.year)
print("month:", now.month)
print("date:", now.day)
print("hour:", now.hour)
print("minute:", now.minute)
print("second:", now.second)