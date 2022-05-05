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



def gambleAction(nextMove,NATION_ARRAY,currentNation,p,index,playerNationIndex):
    preferencePrint('',p,index,playerNationIndex)
    preferencePrint(str(str(currentNation[1]) + ' chose to gamble'),p,index,playerNationIndex)
    preferencePrint('---------------------',p,index,playerNationIndex)
    amount = nextMove[1] # the amount chosen to gamble
    originalFinanceScore = currentNation[0]['Finance']['wealth'] + amount
    winnings = random.randint((round(0.3*amount)), round(2*amount)) 

    NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + winnings

    difference = NATION_ARRAY[index][0]['Finance']['wealth'] - originalFinanceScore  

    if difference > 0:
        preferencePrint(str(str(currentNation[1]) + ' gained  +' + str(difference)),p,index,playerNationIndex)
    elif difference < 0:
        preferencePrint(str(str(currentNation[1]) + ' lost  ' + str(difference)),p,index,playerNationIndex)
    else:
        preferencePrint(str(str(currentNation[1]) + ' broke even  ' + str(difference)),p,index,playerNationIndex)

    preferencePrint(str('Gambled         : ' + str(amount)),p,index,playerNationIndex)
    preferencePrint(str('Winnings        : ' + str(winnings)),p,index,playerNationIndex)
    preferencePrint(str('Finance credits : ' + str(NATION_ARRAY[index][0]['Finance']['wealth'] )),p,index,playerNationIndex)
    return(NATION_ARRAY)


def buyAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex):
    commodity = nextMove[1]
    amount    = nextMove[2]
    cost      = amount * PRICE_TRACKER[commodity]['price']

    preferencePrint(str(str(currentNation[1]) + ' chose to buy '),p,index,playerNationIndex)
    preferencePrint('------------------',p,index,playerNationIndex)
    preferencePrint(str('Credits    : ' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
    preferencePrint(str(str(commodity) + ' purchased : ' + str(amount)),p,index,playerNationIndex)
    preferencePrint(str('Total Cost :' + str(cost)),p,index,playerNationIndex)

    # UPDATE Reduce stock and deliver goods to user
    PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] - amount
    NATION_ARRAY[index][0]['Finance'][commodity] = NATION_ARRAY[index][0]['Finance'][commodity] + amount
    preferencePrint(str('New total : ' + str(NATION_ARRAY[index][0]['Finance'][commodity])),p,index,playerNationIndex)
    return(NATION_ARRAY,PRICE_TRACKER)

def sellAction(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex):
    commodity = nextMove[1]
    amount    = nextMove[2]
    value     = nextMove[3]
    preferencePrint(str(str(currentNation[1]) + ' chose to sell'),p,index,playerNationIndex)
    preferencePrint('------------------',p,index,playerNationIndex)
    preferencePrint(str('Credits    : ' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
    preferencePrint(str(str(commodity) + ' owned : ' + str(currentNation[0]['Finance'][commodity])),p,index,playerNationIndex)
    preferencePrint(str(str(commodity) + ' sold  : ' +  str(amount)),p,index,playerNationIndex)
    

    # UPDATE Increase stock and credit user
    PRICE_TRACKER[commodity]['stock'] = PRICE_TRACKER[commodity]['stock'] + amount
    NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + value
    preferencePrint(str(str(currentNation[1]) + ' was paid ' + str(value)),p,index,playerNationIndex)
    preferencePrint(str('New Credits Total   : ' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
    return(NATION_ARRAY,PRICE_TRACKER)


def investResource(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex,nextMoveIndex):
    pending          = nextMove[0]
    job              = nextMove[1]
    resource         = nextMove[2]
    spendAmount      = nextMove[3]
    investedPrice    = nextMove[4]
    wait             = nextMove[5] 
    moveIndex = nextMoveIndex # Get position in country array
    #[['Submitted','investResource',resource,spendAmount,investedPrice,wait]]

    # IF NOT YET READY
    if wait > 0:
        wait = wait -1
        preferencePrint(str(str(currentNation[1]) + ' chose to Invest in ' + str(resource)),p,index,playerNationIndex)
        preferencePrint('------------------',p,index,playerNationIndex)
        preferencePrint(str('Time Remaining : ' + str(wait)),p,index,playerNationIndex)

        nextMove = ['pending',job,resource,spendAmount,investedPrice,wait]
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = nextMove

    if wait < 1:
        currentPrice = PRICE_TRACKER[resource]['price']
        priceDiff = currentPrice - investedPrice
        original = currentNation[0]['Finance']['wealth']

        if priceDiff > 0:
            bonus = round(priceDiff * spendAmount * (random.randint(1,300)/100))
            NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + bonus
            preferencePrint(str(str(currentNation[1]) + ' made a profit of $' + str(bonus)),p,index,playerNationIndex)
            
        if priceDiff < 0:
            priceDiff = -priceDiff
            token = round((priceDiff/investedPrice) * investedPrice)
            loss = round(spendAmount - token)
            NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + loss
            preferencePrint(str(str(currentNation[1]) + ' made a loss, but recouped $' + str(loss)),p,index,playerNationIndex)

        if priceDiff == 0:
            token = round(investedPrice + (investedPrice * (random.randint(1,18)/100)))
            NATION_ARRAY[index][0]['Finance']['wealth'] = NATION_ARRAY[index][0]['Finance']['wealth'] + token + spendAmount
            preferencePrint(str(str(currentNation[1]) + ' made no profit, but gained token interest of $' + str(token)),p,index,playerNationIndex)

        preferencePrint(str('Credits changed from $' + str(original) + ' to $' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = []


    return(NATION_ARRAY)


def investCountry(nextMove,NATION_ARRAY,currentNation,PRICE_TRACKER,p,index,playerNationIndex,nextMoveIndex):
    pending                  = nextMove[0]
    job                      = nextMove[1]
    NationChoice             = nextMove[2]
    spendAmount              = nextMove[3]
    nationsOriginalWealth    = nextMove[4]
    wait                     = nextMove[5] 
    moveIndex                = nextMoveIndex # Get position in country array
    myNation                 = currentNation[1]
    thereNation              = NATION_ARRAY[NationChoice][1]
    original                 = currentNation[0]['Finance']['wealth']
    originalFriendshipAB     = NATION_ARRAY[index][0]['Friendship'][thereNation]['level']
    originalFrienshipBA      = NATION_ARRAY[NationChoice][0]['Friendship'][myNation]['level']


    # IF NOT YET READY
    if wait > 0:
        wait = wait -1
        preferencePrint(str(str(currentNation[1]) + ' chose to Invest in ' + str(NATION_ARRAY[NationChoice][1])),p,index,playerNationIndex)
        preferencePrint('------------------',p,index,playerNationIndex)
        preferencePrint(str('Time Remaining : ' + str(wait)),p,index,playerNationIndex)

        nextMove = ['pending',job,NationChoice,spendAmount,nationsOriginalWealth,wait]
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = nextMove

    if wait < 1:
        currentWealth          = NATION_ARRAY[NationChoice][0]['Finance']['wealth']
        wealthDiff             = currentWealth - nationsOriginalWealth
        myOriginalCredits      = currentNation[0]['Finance']['wealth']
        
        if wealthDiff > 0:
            bonus = round(wealthDiff * 0.2) + round(wealthDiff * 0.05 * spendAmount/100) + (spendAmount * 1.5)
            bonus = round(bonus)
            #print('982348937982348937982348937982348937982348937982348937 WEALTH DIFF' + str(wealthDiff))
            NATION_ARRAY[index][0]['Finance']['wealth'] = round(NATION_ARRAY[index][0]['Finance']['wealth'] + bonus)
            preferencePrint(str(str(currentNation[1]) + ' made a profit of $' + str(bonus)),p,index,playerNationIndex)
   
        if wealthDiff < 0:
            loss = 0.8 * spendAmount
            NATION_ARRAY[index][0]['Finance']['wealth'] = round(NATION_ARRAY[index][0]['Finance']['wealth'] + loss)
            preferencePrint(str(str(currentNation[1]) + ' made a loss, but recouped $' + str(loss)),p,index,playerNationIndex)

        if wealthDiff == 0:
            token = round(nationsOriginalWealth + (nationsOriginalWealth * (random.randint(1,10)/100)))
            token = round(token)
            NATION_ARRAY[index][0]['Finance']['wealth'] = round(NATION_ARRAY[index][0]['Finance']['wealth'] + token + spendAmount)
            preferencePrint(str(str(currentNation[1]) + ' made no profit, but gained token interest of $' + str(token)),p,index,playerNationIndex)


        # BOOST FRIENDSHIP
        NATION_ARRAY[index][0]['Friendship'][thereNation]['level'] = NATION_ARRAY[index][0]['Friendship'][thereNation]['level'] + random.randint(1,18)
        NATION_ARRAY[NationChoice][0]['Friendship'][myNation]['level']     = NATION_ARRAY[NationChoice][0]['Friendship'][myNation]['level'] + random.randint(1,18)
        
        preferencePrint(str(str(thereNation) + ' greatly appreciates the investment from ' + str(myNation)),p,index,playerNationIndex)
        preferencePrint(str('New friendship between ' + str(thereNation) + ' and ' + str(myNation) + ' has increased from ' + str(originalFriendshipAB) + ' to ' + str(NATION_ARRAY[index][0]['Friendship'][thereNation]['level'])),p,index,playerNationIndex)
        preferencePrint(str('New friendship between ' + str(myNation) + ' and ' + str(thereNation) + ' has increased from ' + str(originalFrienshipBA) + ' to ' + str(NATION_ARRAY[NationChoice][0]['Friendship'][myNation]['level'])),p,index,playerNationIndex)
        preferencePrint(str('Credits changed from $' + str(original) + ' to $' + str(currentNation[0]['Finance']['wealth'])),p,index,playerNationIndex)
        NATION_ARRAY[index][0]['Nextmoves'][moveIndex] = []


    return(NATION_ARRAY)






def promotion(currentNation,p,index,playerNationIndex):
    financeRank = ['PickPocket', 'Penny Pusher', 'Assistant', 'gambler', 'accountant', 'huslter', 'business magnate']
    wealth = currentNation[0]['Finance']['wealth']
    rank   = currentNation[0]['Finance']['level']
    if wealth > 5100 and rank == financeRank[0]:
        currentNation[0]['Finance']['level'] = financeRank[1]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)

    if wealth > 10000 and rank == financeRank[1]:
        currentNation[0]['Finance']['level'] = financeRank[2]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)

    if wealth > 15000 and rank == financeRank[2]:
        currentNation[0]['Finance']['level'] = financeRank[3]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)

    if wealth > 20000 and rank == financeRank[3]:
        currentNation[0]['Finance']['level'] = financeRank[4]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)

    if wealth > 30000 and rank == financeRank[4]:
        currentNation[0]['Finance']['level'] = financeRank[5]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint(str(currentNation[1] ) + ' levelled up! New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)

    if wealth > 40000 and rank == financeRank[5]:
        currentNation[0]['Finance']['level'] = financeRank[6]
        rank   = currentNation[0]['Finance']['level']
        currentNation[0]['Special']['notes'].append('financeLevel') 
        preferencePrint('****' +  str(currentNation[1] ) + ' levelled up!***** New Finance rank is ' + str(currentNation[0]['Finance']['level']),p,index,playerNationIndex)
    return(currentNation)
