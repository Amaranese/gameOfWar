# All Finance Menu Function

from conquest_utilities import slow_print as slow_print
from conquest_utilities import med_print as med_print
from conquest_utilities import fast_print as fast_print
from conquest_utilities import superfast_print as superfast_print
from conquest_utilities import clearScreen as clearScreen
from conquest_utilities	 import preferencePrint as preferencePrint

"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           FINANCE  MENU
#     1. Gamble
#     2. Trade
#     2.1 buy
#     2.2 sell
#     5. Exit
# =====================================================================
# =====================================================================
# =====================================================================
"""

def financeBeuro(myNation,year):
	financeSelection = ' '
	while financeSelection != '':
		clearScreen()
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('        WELCOME TO THE FINANCE BEURO $£          ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']) )
		print('Year: ' + str(year))
		print('')
		print('[1] Gamble')
		print('[2] Trade Exchange')
		print('[3] Exit')
		print(' ')
		print(' ')
		print('****************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':
			myNation = gambleMenu(myNation,year)
		if financeSelection == '2':
			myNation = tradeMenu(myNation,year)
		if financeSelection == '3':
			print('exiting...')
			break
	return(myNation)

			

def gambleMenu(myNation,year):
	clearScreen()
	print('My Team: ' + str(myNation[1]))
	print('Year: ' + str(year))
	print('Trade Credits: ' + str(myNation[0]['Finance']['wealth']))
	print(' ')
	print('')
	
	
	flag = 0
	creditsAvailable = int(myNation[0]['Finance']['wealth'])
	gambleAmount = 0

	if creditsAvailable < 1:
		print('you do not have enough credits, sorry')
		flag = 1

	if flag == 1:
		print('you do not have enough credits, exiting, sorry')
		return(myNation)

	fast_print('How much do you wish to gamble? \n')
	while gambleAmount < 1:
		try:
			gambleAmount = int(input('Input amount between 1 and ' + str(creditsAvailable) + '\n'))
		except:
			print("Entered incorrectly, please try again")
	
	if gambleAmount > creditsAvailable:
		fast_print('Entered too much')
		return(myNation)

	# Decrement wealth now.
	myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - gambleAmount
	myNation[0]['Nextmove'] = 'gamble',gambleAmount
	print('You will gamble ' + str(myNation[0]['Nextmove'][1]) + ' in the next round')
	buffer = input('press any key to continue')
	skipflag = 'y'
	return(myNation)
	



def buyMenu(myNation,year):
	clearScreen()
	financeSelection = ' '
	while financeSelection != '':
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('         $$$  BUY BUY BUY      $$$               ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
		print('Stash: ' + str(myNation[0]['Finance']['gold']) + ' : ' + str(myNation[0]['Finance']['gems']) + ' : ' + str(myNation[0]['Finance']['raremetals'])  + ' : ' + str(myNation[0]['Finance']['oil'])  ) 
		print('')
		print('Gold        : ' + '$200')
		print('Gems        : ' + '$300')
		print('Rare Metals : ' + '$20')
		print('Oil         : ' + '$10')
		print('')
		print('[1] Buy Gold')
		print('[2] Buy Gems')
		print('[3] Buy Metals')
		print('[4] Buy Oil')
		print('')
		print('')
		print('[R] Return')
		#print('[M] Main Menu')
		print(' ')
		print(' ')
		print('***************************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':

			# buy funcion 
			# (item, price, credits)
			# max = round(credits/price) down
			# input('How many do you want to buy? ' )
			fast_print('Bought Gold')
			print('')
		if financeSelection == '2':
			fast_print('Bought Gems')
			print('')
		if financeSelection == '3':
			print('exiting...')
			return(myNation)
		if financeSelection == 'R' or financeSelection == 'r':
			return(myNation)
		if financeSelection == 'M' or financeSelection == 'm':
			print('exiting...') 
			return(myNation)





def tradeMenu(myNation,year):
	clearScreen()
	financeSelection = ' '
	while financeSelection != '':
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('         $$$$  TRADE EXCHANGE   $$$$$            ')
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print('')
		print('My Team: ' + str(myNation[1]))
		print('Year: ' + str(year))
		print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
		print('')
		print('Gold        : ' + str(myNation[0]['Finance']['gold']))
		print('Gems        : ' + str(myNation[0]['Finance']['gems']))
		print('Rare Metals : ' + str(myNation[0]['Finance']['raremetals']))
		print('Oil         : ' + str(myNation[0]['Finance']['oil']))
		print('')
		print('[1] Buy')
		print('[2] Sell')
		print('[3] Exit')
		print(' ')
		print(' ')
		print('***************************************************')
		print(' ')
		print(' ')
		financeSelection = str(input('Please chose an option \n'))
		print(financeSelection)
		if financeSelection == '1':
			myNation = buyMenu(myNation,year)
		if financeSelection == '2':
			fast_print('Chose to sell')
		if financeSelection == '3':
			print('exiting...')
			return(myNation)





