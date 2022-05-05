# All Finance Menu Function

from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities  import selectCountry as selectCountry
from gameConquest_utilities  import checkMoves as checkMoves
from gameConquest_utilities  import enterMoney as enterMoney


"""
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#                           FINANCEBEURO
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""


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


def financeBeuro(myNation,year,PRICE_TRACKER,NATION_ARRAY):
    financeSelection = ' '
    while financeSelection != 'XYZFFJJJJJJ':
        clearScreen()
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('     WELCOME TO THE FINANCE BEURO    😊💰        ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('     WELCOME TO THE FINANCE BEURO    ;-)         ')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')    
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('Wealth : ' + str(myNation[0]['Finance']['wealth']) )
        print('Level  : ' + str(myNation[0]['Finance']['level']))
        print('')
        print('[G] Gamble')
        print('[I] Invest')
        print('[T] Trade Exchange')
        print('[R] Return')
        print(' ')
        print(' ')
        print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
        print('**************************************************')
        print(' ')
        print(' ')
        financeSelection = str(input('Please chose an option \n')).upper()
        if financeSelection == 'G':
            myNation = gambleMenu(myNation,year)
        if financeSelection == 'I':
            myNation = investMenu(myNation,year,PRICE_TRACKER,NATION_ARRAY)
        if financeSelection == 'T':
            myNation = tradeMenu(myNation,year,PRICE_TRACKER)
        if financeSelection == 'R' or financeSelection == '':
            return(myNation)
    return(myNation)

            
"""
# SUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENU
# =====================================================================
#                           VIEW OPTION UTILS
# =====================================================================
# =====================================================================
"""

def showFriendship(myNation,friendshipFlag):
    if friendshipFlag == 'Y':
        print(str(myNation[1]) + ' INTERNATIONAL RELATIONS')
        print('---------------------------------------------')
        for nation in myNation[0]['Friendship'].keys():
            paddingLen = 15 - len(nation)
            padding = ''
            for x in range(0,paddingLen): padding = padding + ' '

            print(str(nation) + str(padding) + ': Friendship Level = ' + str(myNation[0]['Friendship'][nation]['level']))
        input('Enter to continue \n')
        clearScreen()
        friendshipFlag = 'N'
    return(friendshipFlag)

def showResources(myNation,year,PRICE_TRACKER,investFlag):
    if investFlag == 'Y':
        clearScreen()
        goldPrice   = PRICE_TRACKER['gold']['price']
        gemPrice    = PRICE_TRACKER['gems']['price']
        metalPrice  = PRICE_TRACKER['raremetals']['price']
        oilPrice    = PRICE_TRACKER['oil']['price']
        myWealth    = myNation[0]['Finance']['wealth']
        print('     ***EXCHANGE RATES***')
        print('')
        print('     Gold        : ' + '$' + str(goldPrice)  + ' ' + str(PRICE_TRACKER['gold']['priceChange'])) 
        print('     Gems        : ' + '$' + str(gemPrice)   + ' ' + str(PRICE_TRACKER['gems']['priceChange']))
        print('     Rare Metals : ' + '$' + str(metalPrice) + ' ' + str(PRICE_TRACKER['raremetals']['priceChange']))
        print('     Oil         : ' + '$' + str(oilPrice)   + ' ' + str(PRICE_TRACKER['oil']['priceChange']))
        print('')
        input('Enter to continue \n')
        clearScreen()
        investFlag = 'N'
    return(investFlag)



"""
# SUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENU
# =====================================================================
#                           SUB MENU
# =====================================================================
# =====================================================================
"""


def gambleMenu(myNation,year):
    clearScreen()
    print('My Team: ' + str(myNation[1]))
    print('Year: ' + str(year))
    print('Trade Credits: ' + str(myNation[0]['Finance']['wealth']))
    print(' ')
    print('')
    

    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'gamble')[1]
    if returnCode > 0: 
        input('Moves used up or already gambled this round. \n')
        return(myNation)

    returnCode,gambleAmount = enterMoney(myNation,'How much money do you wish to gamble?')
    if returnCode > 0: return(myNation)

    # Decrement wealth now.
    myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - gambleAmount
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['gamble',gambleAmount]]

    print('You will gamble ' + str(gambleAmount) + ' in the next round')
    buffer = input('Press enter to continue \n')
    skipflag = 'y'
    return(myNation)
    

"""
# SUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENU
# =====================================================================
#                           SUB MENU
# =====================================================================
# =====================================================================
"""



def buy(credits, price,myNation, name):
    maxpurchase = int(credits // price)
    print('You can buy up to ' + str(maxpurchase) + ' ' + str(name) + ' for a cost of $' + str(price) + ' each.')


    try:
        purchaseAmount = int(input('Enter amount \n'))
    except:
        print("Entered incorrectly, please try again")
        return(myNation)

    cost = purchaseAmount * price
    if cost > credits:
        input('Not enough credits, sorry \n')
        return(myNation)
    if purchaseAmount < 1:
        input('Enter a correct amount \n')
        return(myNation)

    # Deduct cost & Place Order 
    myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - cost
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['buy',name, purchaseAmount]]

    fast_print('Bought ' + str(name) + ' at a cost of ' + str(cost) + '\n')
    input('Press enter to continue \n')
    return(myNation)


def buyMenu(myNation,year,PRICE_TRACKER):
    financeSelection = ' '

    while financeSelection != 'XYZFFJJJJJJ':
        clearScreen()
        goldPrice   = PRICE_TRACKER['gold']['price']
        gemPrice    = PRICE_TRACKER['gems']['price']
        metalPrice  = PRICE_TRACKER['raremetals']['price']
        oilPrice    = PRICE_TRACKER['oil']['price']
        myWealth    = myNation[0]['Finance']['wealth']



        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('         💰💰💰  BUY BUY BUY      💰💰💰💰     ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('            £££  BUY BUY BUY     $$$             ')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('Wealth : ' + str(myWealth))
        print('Level  : ' + str(myNation[0]['Finance']['level']))
        print('Stash: Gld:' + str(myNation[0]['Finance']['gold']) + ' Gms: ' + str(myNation[0]['Finance']['gems']) + ' Rm: ' + str(myNation[0]['Finance']['raremetals'])  + ' Oil: ' + str(myNation[0]['Finance']['oil'])  ) 
        print('')
        print('')
        print('     ***EXCHANGE RATES***')
        print('')
        print('     Gold        : ' + '$' + str(goldPrice)   + ' ' + str(PRICE_TRACKER['gold']['priceChange']))  
        print('     Gems        : ' + '$' + str(gemPrice)    + ' ' + str(PRICE_TRACKER['gems']['priceChange']))   
        print('     Rare Metals : ' + '$' + str(metalPrice)  + ' ' + str(PRICE_TRACKER['raremetals']['priceChange'])) 
        print('     Oil         : ' + '$' + str(oilPrice)    + ' ' + str(PRICE_TRACKER['oil']['priceChange']))   
        print('')
        print('')
        print('')
        print('[G] Buy Gold')
        print('[P] Buy Precious Gems')
        print('[R] Buy Rare Metals')
        print('[O] Buy Oil')
        print('[A] Show median rates')
        print('[H] Show historical prices')
        print('[M] Show Marketplace stock')
        print('')
        print('')
        print('[R] Return')
        #print('[M] Main Menu')
        print(' ')
        print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
        print('***************************************************')
        print(' ')
        print(' ')

        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        moveLimit = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves']) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
        if moveLimit < 1: 
            input('you have used up all your moves for this round')
            return(myNation)


        financeSelection = str(input('Please chose an option \n')).upper()
        if financeSelection == 'G':
            clearScreen()
            myNation = buy(myWealth,goldPrice,myNation, 'gold')
        if financeSelection == 'P':
            clearScreen()
            myNation = buy(myWealth,gemPrice,myNation, 'gems')
        if financeSelection == 'R':
            clearScreen()
            myNation = buy(myWealth,metalPrice,myNation, 'raremetals')
        if financeSelection == 'O':
            clearScreen()
            myNation = buy(myWealth,oilPrice,myNation, 'oil')
        if financeSelection == 'A':
            clearScreen()
            for item in PRICE_TRACKER:
                print('Average ' + str(item) + ' price: ' +str(PRICE_TRACKER[item]['average']))
            input('Press enter to continue \n')
        if financeSelection == 'H':
            for item in PRICE_TRACKER:
                print('Historical ' + str(item) + ' prices: ' + str((PRICE_TRACKER[item]['history'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'M':
            for item in PRICE_TRACKER:
                print(str(item) + ' stock available to buy : ' + str((PRICE_TRACKER[item]['stock'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'R' or financeSelection == 'r' or financeSelection == '':
            return(myNation)




def sell(credits, price,myNation, name):
    myStock = myNation[0]['Finance'][name]
    print('You can sell up to ' + str(myStock) + ' ' + str(name) + ' for $' + str(price) + ' each')


    try:
        sellAmount = int(input('Enter amount \n'))
    except:
        print("Entered incorrectly, please try again")
        return(myNation)
    clearScreen()
    value = sellAmount * price
    if sellAmount > myStock:
        input('Not enough to sell \n')
        return(myNation)
    if sellAmount < 1:
        input('Enter a correct amount \n')
        return(myNation)

    # reduce stock and place order
    myNation[0]['Finance'][name] = myNation[0]['Finance'][name] - sellAmount
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['sell',name, sellAmount, value]]

    fast_print('Sold ' + str(name) + ' at a value of ' + str(value) + '\n')
    input('You will get paid next round \n')
    return(myNation)



def sellMenu(myNation,year,PRICE_TRACKER):
    financeSelection = ' '

    while financeSelection != 'XYZFFJJJJJJ':
        clearScreen()
        goldPrice   = PRICE_TRACKER['gold']['price']
        gemPrice    = PRICE_TRACKER['gems']['price']
        metalPrice  = PRICE_TRACKER['raremetals']['price']
        oilPrice    = PRICE_TRACKER['oil']['price']
        myWealth    = myNation[0]['Finance']['wealth']



        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('         💰💰💰  SELL SELL SELL   💰💰💰💰     ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('            £££  SELL SELL SELL     $$$          ')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('Wealth : ' + str(myWealth))
        print('Level  : ' + str(myNation[0]['Finance']['level']))
        print('Stash: Gld:' + str(myNation[0]['Finance']['gold']) + ' Gms: ' + str(myNation[0]['Finance']['gems']) + ' Rm: ' + str(myNation[0]['Finance']['raremetals'])  + ' Oil: ' + str(myNation[0]['Finance']['oil'])  ) 
        print('')
        print('')
        print('     ***EXCHANGE RATES***')
        print('')
        print('     Gold        : ' + '$' + str(goldPrice)  + ' ' + str(PRICE_TRACKER['gold']['priceChange'])) 
        print('     Gems        : ' + '$' + str(gemPrice)   + ' ' + str(PRICE_TRACKER['gems']['priceChange']))
        print('     Rare Metals : ' + '$' + str(metalPrice) + ' ' + str(PRICE_TRACKER['raremetals']['priceChange']))
        print('     Oil         : ' + '$' + str(oilPrice)   + ' ' + str(PRICE_TRACKER['oil']['priceChange']))
        print('')
        print('')
        print('')
        print('[G] Sell Gold')
        print('[P] Sell Precious Gems')
        print('[R] Sell Rare Metals')
        print('[O] Sell Oil')
        print('[A] Show median rates')
        print('[H] Show historical prices')
        print('[M] Show Marketplace stock')
        print('')
        print('')
        print('[R] Return')
        #print('[M] Main Menu')
        print(' ')
        print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
        print('***************************************************')
        print(' ')
        print(' ')

        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        moveLimit = int(myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves']) + str(sum(myNation[0]['Nextmoves'], [])).count('pending') )
        if moveLimit < 1: 
            input('you have used up all your moves for this round')
            return(myNation)


        financeSelection = str(input('Please chose an option \n')).upper()
        if financeSelection == 'G':
            myNation = sell(myWealth,goldPrice,myNation, 'gold')
        if financeSelection == 'P':
            myNation = sell(myWealth,gemPrice,myNation, 'gems')
        if financeSelection == 'R':
            myNation = sell(myWealth,metalPrice,myNation, 'raremetals')
        if financeSelection == 'O':
            myNation = sell(myWealth,oilPrice,myNation, 'oil')
        if financeSelection == 'A':
            for item in PRICE_TRACKER:
                print('Average ' + str(item) + ' price: ' +str(PRICE_TRACKER[item]['average']))
            input('Press enter to continue \n')
        if financeSelection == 'H':
            for item in PRICE_TRACKER:
                print('Historical ' + str(item) + ' prices: ' + str((PRICE_TRACKER[item]['history'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'M':
            for item in PRICE_TRACKER:
                print(str(item) + ' stock available to buy : ' + str((PRICE_TRACKER[item]['stock'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'R' or financeSelection == 'r' or financeSelection == '':
            return(myNation)
        if financeSelection == 'M' or financeSelection == 'm':
            print('exiting...') 
            return(myNation)



"""
# SUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENUSUBMENU
# =====================================================================
#                           SUB MENU
# =====================================================================
# =====================================================================
"""


def tradeMenu(myNation,year,PRICE_TRACKER):
    financeSelection = ' '
    while financeSelection != 'XYZFFJJJJJJ':
        clearScreen()
        goldPrice   = PRICE_TRACKER['gold']['price']
        gemPrice    = PRICE_TRACKER['gems']['price']
        metalPrice  = PRICE_TRACKER['raremetals']['price']
        oilPrice    = PRICE_TRACKER['oil']['price']
        myWealth    = myNation[0]['Finance']['wealth']
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('         💰💰💰  TRADE EXCHANGE   💰💰💰💰     ')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        # print('           $$$$  TRADE EXCHANGE   ££££           ')
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
        print('Level  : ' + str(myNation[0]['Finance']['level']))
        print('')
        print('     ***EXCHANGE RATES***')
        print('')
        print('     Gold        : ' + '$' + str(goldPrice)  + ' ' + str(PRICE_TRACKER['gold']['priceChange'])) 
        print('     Gems        : ' + '$' + str(gemPrice)   + ' ' + str(PRICE_TRACKER['gems']['priceChange']))
        print('     Rare Metals : ' + '$' + str(metalPrice) + ' ' + str(PRICE_TRACKER['raremetals']['priceChange']))
        print('     Oil         : ' + '$' + str(oilPrice)   + ' ' + str(PRICE_TRACKER['oil']['priceChange']))
        print('')
        print('')
        print('Gold        : ' + str(myNation[0]['Finance']['gold']))
        print('Gems        : ' + str(myNation[0]['Finance']['gems']))
        print('Rare Metals : ' + str(myNation[0]['Finance']['raremetals']))
        print('Oil         : ' + str(myNation[0]['Finance']['oil']))
        print('')
        print('[B] Buy')
        print('[S] Sell')
        print('')
        print('')
        print('[A] Show median rates')
        print('[H] Show historical prices')
        print('[M] Show Marketplace stock')
        print('[R] Return')
        print(' ')
        print(' ')
        print('Moves: ' + str( myNation[0]['Special']['moveLimit'] - len(myNation[0]['Nextmoves'])  + str(sum(myNation[0]['Nextmoves'], [])).count('pending')))
        print('***************************************************')
        print(' ')
        print(' ')
        financeSelection = str(input('Please chose an option \n')).upper()
        if financeSelection == 'B':
            myNation = buyMenu(myNation,year,PRICE_TRACKER)
        if financeSelection == 'S':
            myNation = sellMenu(myNation,year,PRICE_TRACKER)
        if financeSelection == 'A':
            for item in PRICE_TRACKER:
                print('Average ' + str(item) + ' price: ' +str(PRICE_TRACKER[item]['average']))
            input('Press enter to continue \n')
        if financeSelection == 'H':
            for item in PRICE_TRACKER:
                print('Historical ' + str(item) + ' prices: ' + str((PRICE_TRACKER[item]['history'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'M':
            for item in PRICE_TRACKER:
                print(str(item) + ' stock available to buy : ' + str((PRICE_TRACKER[item]['stock'])) )
                print('')
            input('Press enter to continue \n')
        if financeSelection == 'R' or financeSelection == '':
            print('exiting...')
            return(myNation)







def investMenu(myNation,year,PRICE_TRACKER,NATION_ARRAY):
    investFlag = ''
    friendshipFlag = 'n'
    investSelection = ' '
    while investSelection != 'XYZFFJJJJJJ':
        clearScreen()
        myWealth    = myNation[0]['Finance']['wealth']
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('         $$$      INVESTMENT HUB      $$$          ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team: ' + str(myNation[1]))
        print('Year: ' + str(year))
        print('Wealth : ' + str(myNation[0]['Finance']['wealth']))
        print('Level  : ' + str(myNation[0]['Finance']['level']))
        print(' ')
        investFlag     = showResources(myNation,year,PRICE_TRACKER,investFlag)
        friendshipFlag = showFriendship(myNation,friendshipFlag)
        print('')
        print('[C] Invest in Countries')
        print('[G] Speculate on Gold')
        print('[O] Speculate on Oil')
        print('[D] Speculate on Diamonds and Gems')
        print('[M] Speculate on Rare Metals')
        print(' ')
        print(' ')
        print(' ')
        print('[R] Show My Resources')
        print('[S] Show Marketplace stock')
        print('[H] Show historical prices')
        print('[F] Show Friendships')
        print('[X] Exit')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)
        investSelection = str(input('Please chose an option \n')).upper()
        if investSelection == 'C':
            myNation = investCountry(myNation,NATION_ARRAY)
        if investSelection == 'G':
            myNation = investResource(myNation,NATION_ARRAY,PRICE_TRACKER,'gold')
        if investSelection == 'O':
            myNation = investResource(myNation,NATION_ARRAY,PRICE_TRACKER,'oil')
        if investSelection == 'D':
            myNation = investResource(myNation,NATION_ARRAY,PRICE_TRACKER,'gems')
        if investSelection == 'M':
            myNation = investResource(myNation,NATION_ARRAY,PRICE_TRACKER,'raremetals')
        if investSelection == 'S':
            for item in PRICE_TRACKER:
                print(str(item) + ' stock available to buy : ' + str((PRICE_TRACKER[item]['stock'])) )
                print('')
            input('Press enter to continue \n')
        if investSelection == 'H':
            for item in PRICE_TRACKER:
                print('Historical ' + str(item) + ' prices: ' + str((PRICE_TRACKER[item]['history'])) )
                print('')
            input('Press enter to continue \n')
        if investSelection == 'F':
            friendshipFlag = 'Y'
        if investSelection == 'R':
            investFlag = 'Y'
        if investSelection == 'X' or investSelection == '':
            return(myNation)
    return(myNation)



def investResource(myNation,NATION_ARRAY,PRICE_TRACKER,resource):
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'investResource')[1]
    if returnCode > 0: 
        input('Already invested or moves used up')
        return(myNation)

    returnCode,spendAmount = enterMoney(myNation,'How much money do you wish to invest?')
    if returnCode > 0: return(myNation)
    print('Investment amount is: ' + str(spendAmount))

    # PLACE ORDER
    # Decrement wealth now
    myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - spendAmount
    investedPrice = PRICE_TRACKER[resource]['price']
    wait = 4
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['Submitted','investResource',resource,spendAmount,investedPrice,wait]]

    print('You have chosen to invest $' + str(spendAmount) + ' in ' + str(resource))
    print('Your profits will be paid into your account after' + str(wait) + ' moves.')
    print(myNation[0]['Nextmoves'] )
    buffer = input('Press enter to continue \n')

    return(myNation)
    

def investCountry(myNation,NATION_ARRAY):
    print('Investing in the growth of a country, helps boost friendship and earns money.')
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'investCountry')[1]
    if returnCode > 0: 
        print('Already invested or moves used up.')
        return(myNation)
    # SELECT COUNTRY
    returnCode,NationChoice = selectCountry(NATION_ARRAY,myNation,'****CHOOSE A NATION TO INVEST IN****')
    if returnCode > 0: return(myNation)

    returnCode,spendAmount = enterMoney(myNation,'How much money do you wish to invest in ' + str(NATION_ARRAY[NationChoice][1]))
    if returnCode > 0: return(myNation)
    print('Investment amount is: ' + str(spendAmount))

    # PLACE ORDER
    # Decrement wealth now
    myNation[0]['Finance']['wealth'] = myNation[0]['Finance']['wealth'] - spendAmount
    nationsOriginalWealth = NATION_ARRAY[NationChoice][0]['Finance']['wealth']
    wait = 4
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [['Submitted','investCountry',NationChoice,spendAmount,nationsOriginalWealth,wait]]

    print('You have chosen to invest $' + str(spendAmount) + ' in ' + str(NATION_ARRAY[NationChoice][1]))
    print('Your profits will be paid into your account after ' + str(wait) + ' moves.')
    buffer = input('Press enter to continue \n')



    return(myNation)
    

