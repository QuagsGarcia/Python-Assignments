# Prints the version of the application
vzn = "v1.0"
print("Hello and welcome to appointment manager " + vzn + ".")
# function for setting the appointment
def apptSet():
	# appointment command prompt
	appointment = input('To set an appointment, please type "appointment": ')

	# Used lower() to make the comparison case-insensitive
	while appointment.lower() != "appointment":
		# error message
	    print("This app only has one command.")
	    appointment = input('To set an appointment, please type "appointment": ')
	#title input with a while loop since the input is required
	title = input('Please type the title of your appointment: ')

	while title == "":
		# error message
	    print("A title is required.")
	    title = input('Please type the title of your appointment: ')
	#description input with no while loop since its optional
	desc = input('Please type the description of your appointment (optional): ')
	#date input with a while loop since the input is required
	date = input('Please type the date of your appointment: ')
	
	while date == "":
		#error message
	    print("A date is required.")
	    date = input('Please type the date of your appointment: ')
	#time input with a while loop since the input is required
	time = input('Please type the time of your appointment: ')

	while time == "":
	    print("A time is required.")
	    time = input('Please type the time of your appointment: ')
	# prints the final stored variables in multiple lines with \n
	print("Your appointment is now set for " + date + " at " + time + ". \nDetails:\nTitle: " + title + "\nDescription: " + desc)
	# the prompt is used to prevent the application closing so you can see the final results
	apptPrompt()
# appointment prompt function to select whether you want the application closed or set another appointment
def apptPrompt():
	prompt = input('Would you like to close this program? (type "y"): ')
	if prompt.lower() != "y":
		prompt = input('Sounds good! To set another appointment, type "y": ')
		if prompt.lower() != "y":
			apptPrompt()
		else:
			apptSet()
# called function
apptSet()