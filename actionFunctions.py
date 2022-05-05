# IMPORT UNIVERSAL UTILITIES
from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
from gameConquest_utilities import options as options
from gameConquest_utilities import music as music

import sys
import time
import copy
import random

import gameFunctionFinance as financeFunction
import gameFunctionWar     as warFunction
import gameFunctionScience as scienceFunction
import AIOrderFunctions    as AI 




# ENTRANCE FUNCTION (TOP LEVEL FLOW)  
def nextYear(year,myNation,ARRAY_DICT,playerNationIndex,p):
    NATION_ARRAY   = ARRAY_DICT['NATION_ARRAY']
    PRICE_TRACKER  = ARRAY_DICT['PRICE_TRACKER']
    WAR_BRIEFING   = ARRAY_DICT['WAR_BRIEFING']
    TECH_MAP       = ARRAY_DICT['TECH_MAP']


    clearScreen()
    fast_print('Processing next year....')
    print('')


    previousPrices = copy.deepcopy (PRICE_TRACKER)

    # ITERATE FOR EACH TEAM 
    for x in range(0, len(NATION_ARRAY)):
        currentNation = NATION_ARRAY[x]
        index = x

        # AI TEAM DECISION
        if currentNation != myNation: 
            currentNation = AI.setAIMoves(index,currentNation,ARRAY_DICT)

        # ACTION CARRIED OUT FOR ALL USERS
        NATION_ARRAY,PRICE_TRACKER = action(index, ARRAY_DICT,currentNation,p,playerNationIndex)

        # BRANCH PROMOTIONS
        currentNation  = financeFunction.promotion(currentNation,p,index,playerNationIndex)
        currentNation  = warFunction.promotion(currentNation,p,index,playerNationIndex)
        #currentNation = financeFunction.promotion(currentNation,p,index,playerNationIndex)
        #currentNation = financeFunction.promotion(currentNation,p,index,playerNationIndex)


    # Only talling scores at the end....may need to change
    print('Tallying scores')
    NATION_ARRAY = tallyScores(NATION_ARRAY)
    NATION_ARRAY = defaultNextStep(NATION_ARRAY)

    # UPDATE PRICE 
    PRICE_TRACKER = updatePrice(PRICE_TRACKER,previousPrices)

    # UPDATE WAR 

    # UPDATE TECH 


    myNation = menu(myNation,PRICE_TRACKER,previousPrices,p,year)
    # INCREMENT THE YEARS
    year = year + 1

    return(year, NATION_ARRAY,PRICE_TRACKER,WAR_BRIEFING,p)








def action(index, ARRAY_DICT,currentNation,p,playerNationIndex):
    NATION_ARRAY   = ARRAY_DICT['NATION_ARRAY']
    PRICE_TRACKER  = ARRAY_DICT['PRICE_TRACKER']
    WAR_BRIEFING   = ARRAY_DICT['WAR_BRIEFING']
    TECH_MAP       = ARRAY_DICT['TECH_MAP']

    if 'sabotaged' in currentNation[0]['Nextmoves']:
        preferencePrint((str(currentNation[1]) + ' sabotaged, skipping round.'),p,index,playerNationIndex)
        currentNation[0]['Nextmoves'] = []
        return(NATION_ARRAY,PRICE_TRACKER)
    
    # PROCESS PASS
    nextMoveIndex = 0
    for nextMove in currentNation[0]['Nextmoves']:
        preferencePrint(str(''),p,index,playerNationIndex)

        # REMEMBER TO UPDATE NATION ARRAY (NOT CURRENT NATION)
        if 'pass' in nextMove:
            preferencePrint(str(str(currentNation[1]) + ' chose to pass'),p,index,playerNationIndex)
            
        if 'gamble' in nextMove:
            NATION_ARRAY = financeFunction.gambleAction(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex)

        if 'buy' in nextMove:
            NATION_ARRAY,PRICE_TRACKER = financeFunction.buyAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex)

        if 'sell' in nextMove:
            NATION_ARRAY,PRICE_TRACKER = financeFunction.sellAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex)

        if 'investResource' in nextMove:
            NATION_ARRAY = financeFunction.investResource(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex,nextMoveIndex)

        if 'investCountry' in nextMove:
            #print('current nation' + str(currentNation[1]))
            NATION_ARRAY = financeFunction.investCountry(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex,nextMoveIndex)
    
        if 'drill' in nextMove:
            NATION_ARRAY = warFunction.drill(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex)

        # Even if prices change, you get it for the order you placed
        if 'WeaponsBuild' in nextMove:
            NATION_ARRAY = warFunction.build(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex,nextMoveIndex)

        if 'WeaponsScrap' in nextMove:
            NATION_ARRAY = warFunction.scrap(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex)

        if 'espionage' in nextMove:
            NATION_ARRAY = warFunction.espionage(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex)

        if 'research' in nextMove:
            NATION_ARRAY = scienceFunction.processResearch(nextMove,NATION_ARRAY,TECH_MAP,currentNation,p,index,playerNationIndex,nextMoveIndex)

        if 'gainResearch' in nextMove:
            NATION_ARRAY = scienceFunction.gainResearch(nextMove,NATION_ARRAY,TECH_MAP,currentNation,p,index,playerNationIndex,nextMoveIndex)

        if 'advanceEra' in nextMove:
            NATION_ARRAY = scienceFunction.advanceEra(nextMove,NATION_ARRAY,TECH_MAP,WAR_BRIEFING,currentNation,p,index,playerNationIndex,nextMoveIndex)        

        nextMoveIndex = nextMoveIndex + 1


    return(NATION_ARRAY,PRICE_TRACKER)
        
 




# TALLY UP SCORES FOR ALL TEAMS 
def tallyScores(NATION_ARRAY):
    for x in range(0, len(NATION_ARRAY)):    
        #SUM UP SUBSCORES
        financeScore   = NATION_ARRAY[x][0]['Finance']['wealth']
        techScore      = NATION_ARRAY[x][0]['Tech']['knowledge']
        warScore       = NATION_ARRAY[x][0]['War']['might']
        politicsScore  = NATION_ARRAY[x][0]['Politics']['influence']
        totalSubScores = round(financeScore + techScore + warScore + politicsScore)
        NATION_ARRAY[x][0]['Score'] = totalSubScores
    return(NATION_ARRAY)






def preserveNextMove(country):
    adjustedNextMove = []
    for nextMove in country['Nextmoves']:
        if 'sabotaged' in nextMove:
            adjustedNextMove = ['sabotaged']
            return(adjustedNextMove)


        if 'pending' in nextMove:
            adjustedNextMove = adjustedNextMove + [nextMove]
        else:
            adjustedNextMove = adjustedNextMove + []
    return(adjustedNextMove)    



# DEFAULTS ALL TEAM ACTIONS TO 'PASS' unless exceptions 
def defaultNextStep(NATION_ARRAY):
    for x in range(0, len(NATION_ARRAY)):
        country = NATION_ARRAY[x][0]
        adjustedNextMove = preserveNextMove(country)
        NATION_ARRAY[x][0]['Nextmoves'] = adjustedNextMove
    return(NATION_ARRAY)


# Two things - updates prices based upon stock change 
# Adds an average value to price tracker
def updatePrice(PRICE_TRACKER,previousPrices):

    for item, key in PRICE_TRACKER.items():
        original   = previousPrices[item]['stock']
        new        = key['stock']
        difference =  (new-original)/original
        volitility =  80
        difference = difference + (difference * (random.randint(10,volitility))) # inflation
        PRICE_TRACKER[item]['priceChange'] = -(round(PRICE_TRACKER[item]['price'] * difference))
        if PRICE_TRACKER[item]['priceChange'] > -1:
            PRICE_TRACKER[item]['priceChange'] = '+' + str(PRICE_TRACKER[item]['priceChange'])
        else:
            PRICE_TRACKER[item]['priceChange'] = str(PRICE_TRACKER[item]['priceChange'])


        if new > original:
            PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  - (PRICE_TRACKER[item]['price'] * difference)) 
        if new < original:
            difference = - difference
            PRICE_TRACKER[item]['price'] = round(PRICE_TRACKER[item]['price']  + (PRICE_TRACKER[item]['price'] * difference))


    # UPDATE HISTORY AND AVERAGE
    for item in PRICE_TRACKER:
        PRICE_TRACKER[item]['history'].append(PRICE_TRACKER[item]['price'])
        average = round(sum(PRICE_TRACKER[item]['history']) / len(PRICE_TRACKER[item]['history']))
        if PRICE_TRACKER[item]['average'] ==0: PRICE_TRACKER[item]['average'] = 1
        PRICE_TRACKER[item]['average'] = average

    return(PRICE_TRACKER)



def menu(myNation,PRICE_TRACKER,previousPrices,p,year):

    # MENU
    hintSwitch = 'off'
    if myNation[0]['hints'] == 'on':
        hintSwitch = 'off'
    else: hintSwitch = 'on'

    choice = 'x'
    while choice != 'xnsdfaoiga':
        print('')
        print('----Processing Complete----')
        print('[1] View prices')
        print('[2] View Previous Prices')
        print('[3] Print Json (for developers)')
        print('[4] Switch hints ' + str(hintSwitch))
        print('[5] Change Next Year Updates')
        print('[x] Skip')
        choice = str(input('Press enter to skip \n'))
        if choice == '1':
            clearScreen()
            for item in PRICE_TRACKER:
                print('*****' + str(item) + '*******')
                print('Price          : ' + str(PRICE_TRACKER[item]['price']))
                print('Market Stock   : ' + str(PRICE_TRACKER[item]['stock']))
                print('Price Change   : ' + str(PRICE_TRACKER[item]['priceChange']))
                print('Average        : ' + str(PRICE_TRACKER[item]['average']))
            print(" ")
            input('Press enter to continue \n')
        if choice == '2':
            clearScreen()
            for item in previousPrices:
                print('*****' + str(item) + '*******')
                print('Price          : ' + str(previousPrices[item]['price']))
                print('Market Stock   : ' + str(previousPrices[item]['stock']))
                print('Price Change   : ' + str(previousPrices[item]['priceChange']))
                print('Average        : ' + str(previousPrices[item]['priceChange']))
            print(" ")
            input('Press enter to continue \n')
        if choice == '3':
            clearScreen()
            print(previousPrices)
            print(PRICE_TRACKER)
            input('Press enter to continue \n')
        if choice == '4':
            myNation[0]['hints'] = hintSwitch
            if hintSwitch == 'off':
                hintSwitch = 'on'
            else: hintSwitch = 'off'
        if choice == '5':
            p = options(p)
        if choice == 'x' or choice =='':
            break


    # lazy coding...
    if hintSwitch == 'off':
        hints = ['****Hint**** \n You can change what you see in next round updates from the options menu', '****Hint**** \n Pressing enter exits or skips most menu`s or takes you back' ,'****Hint**** \n Resources like gold have a market stock, prices reflect the availability in the market.']
        print(str(random.choice(hints)))
    print('')
    print('')
    buffer = input('Press enter to continue \n')
    
    return(myNation)



