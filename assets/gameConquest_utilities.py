
# UTILITIES 
import sys
import time

p = 'All'

def slow_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.2)


def med_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.10)

def fast_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)

def superfast_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)

def clearScreen():
	for x in range(0,70):
		print('')

def preferencePrint(s,p,i,myNationIndex):
	if p == 'All':
		print(s)
	elif p == 'Me':
		if str(i) == str(myNationIndex):
			print(s)
	elif p == 'None':
		pass
	else:
		print(s)



def printupdates(p):
	print('Welcome...')
	print(' ')
	print('You can change what you want to see at the end of the round')
	print('[A]. All stats and country activities')
	print('[O]. Only my stuff')
	print('[D]. Dont show me anything' )
	p = str(input('Please select an option. \n')).upper()
	if p == 'A':
		p = 'All'
	elif p == 'O':
		p = 'Me'
	elif p == 'D':
		p = 'None'
	else:
		p = 'All'
	return(p)

def options(p,NATION_ARRAY):
	clearScreen()
	print('***************************************************')
	print('*                  OPTIONS                        *')
	print('***************************************************')
	print('')
	print('1. Select Music')
	print('2. Change End of Round Updates')
	print('3. Developer Insights')

	selection = str(input('Please select an option \n'))
	if selection == '1':
		music()
	if selection == '2':
		p = printupdates(p)
		return(p)
	if selection == '1':
		developer(NATION_ARRAY)







def music():
	import webbrowser
	clearScreen()
	
	print('***************************************************')
	print('                🎸🎸 MUSIC  🎺🎺                  ')
	print('***************************************************')
	# print('***************************************************')
	# print('             [+][+]   MUSIC  [+][+]                ')
	# print('***************************************************')
	print('1. Game Music')
	print('2. SciFi Chill')
	print('3. LO FI')
	print('4. Trappin')
	print('5. Relaxed Gaming Music')
	print('6. 70s Japanese')
	print('7. Asian Pop')
	print('8. Exit')
	print('')
	print('')
	fast_print('This will open music in your webbrowser. \n' )
	print('')

	decision = str(input('Please select an option. \n'))

	if decision == '1':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/H8w_Q57RQJc')
	if decision == '2':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/B0PGvSA5f7k')
	if decision == '3':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/_fVjJmX2GYs')
	if decision == '4':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/rehF0Df2DIc')
	if decision == '5':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/tghXpPpHHJ4')
	if decision == '6':
		fast_print('Opening browser window, remember to come back!')
		webbrowser.open('https://youtu.be/E4s-hxY80pA')
	if decision == '7':
		fast_print('Opening browser window, remember to come back!')	
		webbrowser.open('https://www.youtube.com/watch?v=w0dMz8RBG7g&list=PL0B70C9C2654CEED6&index=2Asian Classic')
	if decision == '8':
		fast_print('Exiting')
		clearScreen()


def developer(NATION_ARRAY):
	clearScreen()
	print('***************************************************')
	print('*              DEV CONSOLE                        *')
	print('***************************************************')
	print('')
	print('1. Select Country')
	print('2. Change End of Round Updates')
	print('3. Developer Insights')

	selection = str(input('Please select an option \n'))
	if selection == '1':
		countryChoice = input('Enter Country name to view stats \n')
		for item in NATION_ARRAY:
		    if item[1] == countryChoice:
		        print(item[0])

	if selection == '2':
		p = printupdates(p)
		return(p)
	if selection == '1':
		developer(NATION_ARRAY)
