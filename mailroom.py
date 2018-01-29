'''You want to write a small command-line script that can handle some of the tasks associated with this job for you. Here’s a list of the things you want to be able to do:

The script should have a data structure that holds a list of your donors and a history of the amounts they have donated. '''

donors = {"Charlie": 100, "Charly": 100, "Santa": 200}

def donor_list():
	dict_string = ' '.join('{}: {}\n'.format(key, val) for key, val in donors.items())
	print(dict_string) #will print dictionary list of donors

'''
When run, the script should prompt the user to choose from a menu of 2 actions: ‘Send a Thank You’ or ‘Create a Report’.
'''
def prompt():
	response = input('Send a Thank You or Create a Report ').lower()
	return response

response = prompt()

'''
If the user selects ‘Send a Thank You’, prompt for a Full Name.
'''
if response == 'send a thank you':
	name = input('Full Name')
	donation = donors[name]
	print('Thank you {0} for your donation of {1}'.format(name, donation))

'''
If the user types ‘list’, show them a list of the donor names and re-prompt
'''
if response == 'list':
	donor_list()
	goto start
	

def add_donor(Ayden):
	amount = input('Donation amount?')
	donors[name] = amount
	print(donors)



'''
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn’t.
Once an amount has been given, add that amount to the donation history of the selected user.
'''
#if name_input not in donors dictionary:
#	add name to donors dictionary
#else	
#	input('what is donation amount')
#		use if to check if valid input:
#			add amount to donor if valid


	
'''
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
'''
"Thank you {0} for your donation of {1}"

'''
You need not persist the new donors when the script quits running.
'''

'''If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
'''

#if input is create a report:
#	sort dictionary by values and print list of donor and values and avg donation 
#	print "Donor {0}: Total Donation: {1}, Num Donations {2}, Average donation {3}  

'''

At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly.
Tasks
Begin by thinking of each individual step as a stand-alone operation. What kind of function would you need to write to accomplish a single step from the above list of steps?

Write a series of pseudocode functions to accomplish the tasks identified by the list of steps above.

Continue by planning the flow of your script. What should happen first, second? How will you move from one step to the next?

You may find that creating a flow chart that shows how you expect your script to work can help you to visualize this process.

You can use a program to create a flow chart, or a free web service like draw.io. Or you can simply sketch something by hand.
'''



#raw_input(