from datetime import datetime, timedelta

today = datetime.now()
print(today)

birthday = input("enter your date of birth: ")

test = datetime.strptime(birthday, "%m/%d/%Y")
#2006-07-23 00:00:00 = ISO8601 date format
test = test + timedelta(days=15)
test_str = test.strftime("%A, %B %d %Y")
print(test_str)
