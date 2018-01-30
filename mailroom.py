from collections import OrderedDict

donors = {"Charlie": [100], "Charly": [100], "Santa": [200]}

def main():
	while True:
		response = prompt()
		if response == '4':
			break
		elif response == '1':
			name = input('Full Name ')
			donation = sum(donors[name])
			print('Thank you {0} for your donation of {1}'.format(name, donation))
	
		elif response == '3':
			donor_list()
			n = input('Name')
			if n not in donors:
				d = input('Donation Amount ')
				donors[n] = [int(d)]
			else:
				newDonation = input('Donation Amount ')
				donors[n].append(int(newDonation))
		elif response == '2':
			orderD = OrderedDict(sorted(donors.items()))
			for key, val in orderD.items():
				numDonations = len(val)
				total = sum(val)
				avg = total / numDonations
				print('Donor {0}: \tTotal Donation: {1},\tNum Donations {2},\tAverage donation {3}'.format(key, total, numDonations, avg))
			


def donor_list():
	dict_string = ' '.join('{}: {}\n'.format(key, val) for key, val in donors.items())
	print(dict_string) #will print dictionary list of donors


def prompt():
	response = input('1:\tSend a Thank You\n2:\tCreate a Report\n3:\tlist\n4:\tquit\n').lower()
	return response


main()
