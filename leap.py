# x=int(input('enter year'))
# def is_year_leap(year):
# 	if (year % 400 == 0) and (year % 100 == 0):
# 		return True

# 	# not divided by 100 means not a century year
# 	# year divided by 4 is a leap year
# 	elif (year % 4 ==0) and (year % 100 != 0):
# 		return True

# 	# if not divided by both 400 (century year) and 4 (not century year)
# 	# year is not leap year
# 	else:
# 		return False
# print(is_year_leap(x))




# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
# 	yr = test_data[i]
# 	print(yr,"->",end="")
# 	result = is_year_leap(yr)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Failed")
    
# def is_year_leap(year):
	if (year % 400 == 0) and (year % 100 == 0):
		return True

	# not divided by 100 means not a century year
	# year divided by 4 is a leap year
	elif (year % 4 ==0) and (year % 100 != 0):
		return True

	# if not divided by both 400 (century year) and 4 (not century year)
	# year is not leap year
	else:
		return False

def days_in_month(year, month):
    if month==9 or month==4 or month==6 or month==11:
        return 30
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        if is_year_leap(year)==True:
            return 29
        else:
            return 28

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
