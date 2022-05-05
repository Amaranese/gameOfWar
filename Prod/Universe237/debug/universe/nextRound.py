# IMPORT UNIVERSAL UTILITIES
import sys
import time
import copy
import random
from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,techEraCost,PTcHistory,dialogue,printDialogue

import universe.gameFunctionFinance as financeFunction
import universe.gameFunctionWar     as warFunction
import universe.gameFunctionScience as scienceFunction
import universe.AIOrderFunctions    as AI 


"""
PLAN   
FIRST - WRITE LOGS TO DATABASE 
AFTER NEXT YEAR IS COMPLETE, DISPLAY IT ALL ON A PAGE
...CAN REFINE LATER 
"""

# ENTRANCE FUNCTION (TOP LEVEL FLOW)  
def processRound(db,averageRPOne,AverageRPTwo,AverageRPThree):
    # DEFINE PLAYER
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))


    # CONTAINS STATS FOR ALL NATIONS
    NATION_ASSETS = db.session.query(NATIONS).all()
    WAR_ASSETS    = db.session.query(warAssets).all()
    TECH_ASSETS   = db.session.query(techAssets).all()

    # FLUSH UPDATES FROM PREVIOUS ROUND 
    dialogue.query.delete()
    
    # REFERENCE DATABASES
    WAR_DATABASE   = db.session.query(warDataBase).all()
    TECH_COST_DB   = db.session.query(techEraCost).all()
    TECH_BONUS_DB  = db.session.query(techEraCost).all()
    PRICE_TRACKER  = db.session.query(PTc).first()
    FRIENDSHIP     = db.session.query(friendship).all()
    GAME_TRACKER   = db.session.query(gameTracker).first()
    year           = GAME_TRACKER.year
    month          = GAME_TRACKER.month

    # Nesting vars into a parm array to make it easier to pass between functions
    PARM_ARRAY = [NATION_ASSETS,WAR_ASSETS,TECH_ASSETS,WAR_DATABASE,TECH_COST_DB,TECH_BONUS_DB,PRICE_TRACKER,FRIENDSHIP,GAME_TRACKER,year]

    # UPDATE PRICE HISTORY
    historicalRow  = PTcHistory(goldPrice=PRICE_TRACKER.goldPrice, gold=PRICE_TRACKER.gold, goldPriceChange=PRICE_TRACKER.goldPriceChange, goldHistory=PRICE_TRACKER.goldHistory, goldAverage=PRICE_TRACKER.goldAverage,rareMetalsPrice= PRICE_TRACKER.rareMetalsPrice, rareMetals= PRICE_TRACKER.rareMetals, rareMetalsPriceChange= PRICE_TRACKER.rareMetalsPriceChange, rareMetalsHistory=PRICE_TRACKER.rareMetalsHistory,rareMetalsAverage=PRICE_TRACKER.rareMetalsAverage,gemsPrice= PRICE_TRACKER.gemsPrice, gems= PRICE_TRACKER.gems, gemsPriceChange= PRICE_TRACKER.gemsPriceChange, gemsHistory=PRICE_TRACKER.gemsHistory,gemsAverage=PRICE_TRACKER.gemsAverage, oilPrice= PRICE_TRACKER.oilPrice, oil= PRICE_TRACKER.oil, oilPriceChange= PRICE_TRACKER.oilPriceChange, oilHistory=PRICE_TRACKER.oilHistory,oilAverage=PRICE_TRACKER.oilAverage)
    db.session.add(historicalRow)
    db.session.commit()

    # Last row
    previousPrices = PTcHistory.query.order_by(-PTcHistory.id).first()

    # ITERATE FOR EACH COUNTRY ** THIS IS THE MAIN LOOP FOR UPDATING ** 
    for currentNation in NATION_ASSETS:
        index = currentNation.id
        if currentNation.country != myNation.country:
            flag = 'AI'
        else:
            flag = 'player'

        #AI TEAM DECISION
        if currentNation.country != myNation.country:
            AImessage = AI.setAIMoves(PARM_ARRAY,db,currentNation,averageRPOne,AverageRPTwo,AverageRPThree,index,flag)
            printRow = printDialogue(flag,str('________________________'),db)
            printRow = printDialogue(flag,str('\n \n \n'),db)

        # ACTION CARRIED OUT FOR ALL USERS
        actionMessage = action(PARM_ARRAY,db,currentNation,index,flag)

        # BRANCH PROMOTIONS
        currentNation  = financeFunction.promotion(currentNation,flag,db)
        #currentNation  = warFunction.promotion(currentNation,p,index,playerNationIndex)
        #currentNation = financeFunction.promotion(currentNation,p,index,playerNationIndex)
        #currentNation = financeFunction.promotion(currentNation,p,index,playerNationIndex)


    # Only talling scores at the end....masy need to change
    print('-------Tallying scores------')
    message = tallyScores(NATION_ASSETS,db)
    
    nextStepsMessage = defaultNextStep(NATION_ASSETS,db)

    
    # UPDATE PRICE 
    updateMessage = updatePrice(PRICE_TRACKER,previousPrices,db)
    # UPDATE WAR 
    # UPDATE TECH 

    #myNation = menu(myNation,PRICE_TRACKER,previousPrices,p,year)
 
    # INCREMENT THE YEARS
    month = int(month) + 1
    if month > 12:
        month = 1
        year = int(year) + 1
    GAME_TRACKER.month = month
    GAME_TRACKER.year = year
    db.session.commit()


    return('Year processed')




    

    

def action(PARM_ARRAY,db,currentNation,index,flag):
    NATION_ASSETS = PARM_ARRAY[0]
    WAR_ASSETS    = PARM_ARRAY[1]
    TECH_ASSETS   = PARM_ARRAY[2]
    WAR_DATABASE  = PARM_ARRAY[3]
    TECH_COST_DB  = PARM_ARRAY[4]
    TECH_BONUS_DB = PARM_ARRAY[5]
    PRICE_TRACKER = PARM_ARRAY[6]
    FRIENDSHIP    = PARM_ARRAY[7]
    GAME_TRACKER  = PARM_ARRAY[8]
    year          = PARM_ARRAY[9]


    currentNation = currentNation
    CURRENT_TECH_ASSETS = db.session.query(techAssets).filter_by(country=currentNation.country,era=currentNation.era).first()
    myWar    = db.session.query(warAssets).filter_by(country=currentNation.country,era=currentNation.era).first()


    # PROCESS PASS
    nextMoveIndex = 0

    printRow = printDialogue('AI',str('The current country is ' + str(currentNation.country)),db)

    nextMoves = currentNation.Nextmoves.split(":")
    for nextMove in nextMoves:
        if len(nextMove) == 0:
            continue
        # print(currentNation.Nextmoves)
        # REMEMBER TO UPDATE NATION ARRAY (NOT CURRENT NATION)
        # if 'pass' in nextMove:
        #     preferencePrint(str(str(currentNation[1]) + ' chose to pass'),p,index,playerNationIndex)
        if 'sabotaged' in nextMove:
            printRow = printDialogue(flag,str(str(currentNation.country) + ' sabotaged, skipping round.'),db)
            currentNation.Nextmoves = " "
            db.session.commit()
            return(0,'complete')

        if 'gamble' in nextMove:
            gambleResult = financeFunction.gambleAction(nextMove,currentNation,flag,db)

        if 'buy' in nextMove:
            financeMessage = financeFunction.buyAction(nextMove,currentNation,PRICE_TRACKER,flag,db)

        if 'sell' in nextMove:
            sellResult = financeFunction.sellAction(nextMove,currentNation,PRICE_TRACKER,flag,db)

        if 'investResource' in nextMove:
            investResult = financeFunction.investResource(nextMove,currentNation,PRICE_TRACKER,flag,nextMoveIndex,db)

        if 'investCountry' in nextMove:
            #print('current nation' + str(currentNation[1]))
            investResult = financeFunction.investCountry(nextMove,currentNation,PRICE_TRACKER,flag,nextMoveIndex,db)
    
        if 'drill' in nextMove:
            drillResult = warFunction.drill(nextMove,currentNation,myWar,nextMoveIndex,flag,db)

        # Even if prices change, you get it for the order you placed
        if 'WeaponsBuild' in nextMove:
            buildResult = warFunction.build(nextMove,currentNation,myWar,nextMoveIndex,flag,db)

        if 'WeaponsScrap' in nextMove:
            scrapMessage = warFunction.scrap(nextMove,currentNation,myWar,nextMoveIndex,flag,db)

        if 'espionage' in nextMove:
            espionageMessage = warFunction.espionage(nextMove,currentNation,myWar,nextMoveIndex,flag,db)

        if 'research' in nextMove:
            researchMessage = scienceFunction.processResearch(nextMove,currentNation,CURRENT_TECH_ASSETS,nextMoveIndex,flag,db)

        if 'gainResearch' in nextMove:
            grantMessage = scienceFunction.gainResearch(nextMove,currentNation,nextMoveIndex,flag,db)

        if 'advanceEra' in nextMove:
            advanceMessage = scienceFunction.advanceEra(nextMove,currentNation,myWar,nextMoveIndex,flag,db)        

        if 'pass'  in nextMove:
            printRow = printDialogue(flag,str(str(currentNation.country) + ' chose to pass.'),db)

        nextMoveIndex = nextMoveIndex + 1

    return(0,'complete')
        
 




# # TALLY UP SCORES FOR ALL TEAMS 
def tallyScores(NATION_ASSETS,db):
    for currentNation in NATION_ASSETS:    
        #SUM UP SUBSCORES *** Need to sort out names **
        financeScore   = int(currentNation.wealth)
        techScore      = int(currentNation.KP)
        warScore       = int(currentNation.might)
        politicsScore  = int(currentNation.influence)
        totalSubScores = round(financeScore + techScore + warScore + politicsScore)
        currentNation.score = totalSubScores
        db.session.commit()
    return(0,'complte')






def preserveNextMove(currentNation):
    adjustedNextMove = ""
    nextMoves = currentNation.Nextmoves.split(":")
    for nextMove in nextMoves:
        if 'sabotaged' in nextMove:
            adjustedNextMove = 'sabotaged'
            return(adjustedNextMove)


        if 'pending' in nextMove:
            adjustedNextMove = adjustedNextMove  + nextMove + ':' 
        else:
            adjustedNextMove = adjustedNextMove + ""
    return(adjustedNextMove)    



# DEFAULTS ALL TEAM ACTIONS TO 'PASS' unless exceptions 
def defaultNextStep(NATION_ASSETS,db):
    for currentNation in NATION_ASSETS:
        adjustedNextMove = preserveNextMove(currentNation)
        currentNation.Nextmoves = adjustedNextMove
        db.session.commit()
    return(0,'complete')



# Update Price, Price change, Historical and average
def updatePrice(PRICE_TRACKER,previousPrices,db):

    previousPrices = PTcHistory.query.order_by(-PTcHistory.id).first()
    commodityList = ['gold','gems','rareMetals','oil']
    for commodity in commodityList:
        pcKey         = commodity + "PriceChange"
        previousStock = getattr(previousPrices,commodity)
        newStock      = getattr(PRICE_TRACKER,commodity)
        price         = getattr(PRICE_TRACKER, str(str(commodity) + "Price"))
        historicalP   = getattr(PRICE_TRACKER, str(str(commodity) + "History"))
        difference    = -((newStock-previousStock)/previousStock) # -ve if stock increases
        volitility    = 80
        inflation     = difference + (difference * (random.randint(10,volitility))) # inflation
        inflated      = round(inflation,2)  # inverst as stock decreases...
        if str(inflated)[0] != '-': inflated = str('+' + str(inflated)) 

        # Update price (if stock increases, price decreases)
        setattr(PRICE_TRACKER,pcKey,inflated)
        newPrice = round(int(price) + (int(price) * inflation),2)
        setattr(PRICE_TRACKER, str(str(commodity) + "Price"),newPrice)
        # Update history
        history = str(str(historicalP) + ',' + str(price))
        setattr(PRICE_TRACKER, str(str(commodity) + "History"), history)
        # Get Average Values
        summed = 0
        for item in history.split(','): summed += int(float(item))
        average = round(summed/len(history.split(',')),2)

        setattr(PRICE_TRACKER, str(str(commodity) + "Average"), average)
        db.session.commit()

    return(0,'success')



# def menu(myNation,PRICE_TRACKER,previousPrices,p,year):

#     # MENU
#     hintSwitch = 'off'
#     if myNation[0]['hints'] == 'on':
#         hintSwitch = 'off'
#     else: hintSwitch = 'on'

#     choice = 'x'
#     while choice != 'xnsdfaoiga':
#         print('')
#         print('----Processing Complete----')
#         print('[1] View prices')
#         print('[2] View Previous Prices')
#         print('[3] Print Json (for developers)')
#         print('[4] Switch hints ' + str(hintSwitch))
#         print('[5] Change Next Year Updates')
#         print('[x] Skip')
#         choice = str(input('Press enter to skip \n'))
#         if choice == '1':
#             clearScreen()
#             for item in PRICE_TRACKER:
#                 print('*****' + str(item) + '*******')
#                 print('Price          : ' + str(PRICE_TRACKER[item]['price']))
#                 print('Market Stock   : ' + str(PRICE_TRACKER[item]['stock']))
#                 print('Price Change   : ' + str(PRICE_TRACKER[item]['priceChange']))
#                 print('Average        : ' + str(PRICE_TRACKER[item]['average']))
#             print(" ")
#             input('Press enter to continue \n')
#         if choice == '2':
#             clearScreen()
#             for item in previousPrices:
#                 print('*****' + str(item) + '*******')
#                 print('Price          : ' + str(previousPrices[item]['price']))
#                 print('Market Stock   : ' + str(previousPrices[item]['stock']))
#                 print('Price Change   : ' + str(previousPrices[item]['priceChange']))
#                 print('Average        : ' + str(previousPrices[item]['priceChange']))
#             print(" ")
#             input('Press enter to continue \n')
#         if choice == '3':
#             clearScreen()
#             print(previousPrices)
#             print(PRICE_TRACKER)
#             input('Press enter to continue \n')
#         if choice == '4':
#             myNation[0]['hints'] = hintSwitch
#             if hintSwitch == 'off':
#                 hintSwitch = 'on'
#             else: hintSwitch = 'off'
#         if choice == '5':
#             p = options(p)
#         if choice == 'x' or choice =='':
#             break


#     # lazy coding...
#     if hintSwitch == 'off':
#         hints = ['****Hint**** \n You can change what you see in next round updates from the options menu', '****Hint**** \n Pressing enter exits or skips most menu`s or takes you back' ,'****Hint**** \n Resources like gold have a market stock, prices reflect the availability in the market.']
#         print(str(random.choice(hints)))
#     print('')
#     print('')
#     buffer = input('Press enter to continue \n')
    
#     return(myNation)



