import datetime

def input_data():
	"""Helper function to take input from the user"""
	print("Enter your date strings dataset")
	print("Please press the key 'X' after entering your dataset \n")
	dataset = []
	while True:
		x = input()
		#On pressing X the input ends
		if x == "X":
			break
		else:
			dataset.append(x)
	return dataset

def time_in_range(start, end, x):
    """Helper function to return true if x is in the range [start, end]"""
    if start <= end:
        return "Open" if start <= x <= end else "Closed"
    else:
        return "Open" if start <= x or x <= end else "Closed"


data = input_data()
if len(data) == 0:
	exit("Please enter the data!!!!!")

#Mapping days to nums
days_dict = {"Mo":1, "Tu":2, "We":3, "Th":4, "Fr":5, "Sa":6, "Su":0}

for single_input_datetime in data:
	explode = single_input_datetime.split(",")
	input_date_range, validate_date = explode[0], explode[1]

	date_time_obj = datetime.datetime.strptime(validate_date, '%Y-%m-%dT%H:%M:%SZ')
	day = date_time_obj.strftime("%w")

	split_input_date_range = input_date_range.split(" ")
	input_date_range_days = ''
	if len(split_input_date_range) == 1:
		input_date_range_times = split_input_date_range[0]
	else:
		input_date_range_days, input_date_range_times = split_input_date_range[0], split_input_date_range[1]

	if input_date_range_days != '':
		#handling of day of the week
		explode = input_date_range_days.split("-")
		input_date_range_days_start, input_date_range_days_end = days_dict[explode[0]], days_dict[explode[1]]
		
		if int(day) not in list(range(input_date_range_days_start, input_date_range_days_end+1)):
			print("Closed")
			continue

	explode = input_date_range_times.split("-")
	start_time, end_time = explode[0], explode[1]

	start = datetime.time(int(start_time.split(":")[0]), int(start_time.split(":")[1]), 0)
	end = datetime.time(int(end_time.split(":")[0]), int(end_time.split(":")[1]), 0)
	validate = datetime.time(int(date_time_obj.strftime("%H")), int(date_time_obj.strftime("%M")), int(date_time_obj.strftime("%S")))
	result = time_in_range(start, end, validate)
	
	#final output for each string passed as input
	print(result)