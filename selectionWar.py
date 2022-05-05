# All WAR Menu Function

from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities  import preferencePrint as preferencePrint
from gameConquest_utilities  import checkMoves as checkMoves
from gameConquest_utilities  import selectCountry as selectCountry


"""
# =====================================================================
# =====================================================================
# =====================================================================
#                           WAR  MENU
#     1. drill
#     2. weapons
#     2.1 buy
#     2.2 scrap
#     5. Exit
# =====================================================================
# =====================================================================
# =====================================================================
"""
def showAssets(myNation,year,flag):
    if flag == 'yes':
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']
        print('Light Unit : ' + str(unitOne[1] + unitTwo[1]))
        print('--------------')
        print(str(unitOne[0]) +  ' : ' + str(unitOne[1]))
        print(str(unitTwo[0]) +   ' : ' + str(unitTwo[1]))
        print('')
        print('Core Division : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
        print('--------------')
        print(str(unitThree[0]) +   ' : ' + str(unitThree[1]))
        print(str(unitFour[0]) +   ' : ' + str(unitFour[1]))
        print(str(unitFive[0]) +   ' : ' + str(unitFive[1]))
        print('')   
        print('Heavy Forces: ' + str(unitSix[1] + unitSeven[1]))
        print('--------------')
        print(str(unitSix[0]) +   ' : ' + str(unitSix[1]))
        print(str(unitSeven[0]) +   ' : ' + str(unitSeven[1]))
        print('')
        print('Super Weapon' )
        print('--------------')
        print(str(unitEight[0]) +   ' : ' + str(unitEight[1]))
        print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        input('Enter to continue \n')
        clearScreen()
        flag = 'no'
    return(flag)

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
        





def warMinistry(myNation,NATION_ARRAY,year,WAR_BRIEFING):
    flag = ''
    warSelection = ' '
    while warSelection != 'XYZFFJJJJJJ':
        clearScreen()
        # NUMER
        unitOne      = myNation[0]['War']['weapons']['1'][1]
        unitTwo      = myNation[0]['War']['weapons']['2'][1]
        unitThree    = myNation[0]['War']['weapons']['3'][1]
        unitFour     = myNation[0]['War']['weapons']['4'][1]
        unitFive     = myNation[0]['War']['weapons']['5'][1]
        unitSix      = myNation[0]['War']['weapons']['6'][1]
        unitSeven    = myNation[0]['War']['weapons']['7'][1]
        unitEight    = myNation[0]['War']['weapons']['8'][1]
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('        WELCOME TO THE MINISTRY OF WAR   :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team   : ' + str(myNation[1]))
        print('Year      : ' + str(year))
        print('Might     : ' + str(myNation[0]['War']['might']) )
        print('Rank     : ' + str(myNation[0]['War']['level']))
        print('Firepower : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print('')
        print("""
(╯°□°)--︻╦╤─ - - - 
                """)
        flag = showAssets(myNation,year,flag)
        print('')
        print('[C] Combat Manevres')
        print('[W] Weapons')
        print('[O] Offensive Missions')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print('[A] Show Military Assets')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        warSelection = str(input('Please chose an option \n')).upper()
        if warSelection == 'C':
            myNation = manoeuvresMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'W':
            myNation = weaponsMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'O':
            myNation = missionsMenu(myNation,NATION_ARRAY,year,WAR_BRIEFING)
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'A':
            flag = 'yes'
        if warSelection == 'R' or warSelection == '':
            return(myNation)
    return(myNation)






"""
# =====================================================================
# =====================================================================
# =====================================================================
#      WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#     WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#     WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
#    WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS WEAPON WEAPONS 
# =====================================================================
# =====================================================================
# =====================================================================
"""





def weaponsMenu(myNation,year,WAR_BRIEFING):
    flag = ''
    warSelection = ' '
    while warSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('                 WEAPONS DEPOT           :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team        : ' + str(myNation[1]))
        print('Year           : ' + str(year))
        print('Might          : ' + str(myNation[0]['War']['might']) )
        print('Rank           : ' + str(myNation[0]['War']['level']))
        print('Light Unit     : ' + str(unitOne[1] + unitTwo[1]))
        print('Core Division  : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
        print('Heavy Forces   : ' + str(unitSix[1] + unitSeven[1]))
        print('SuperWeapons   : ' + str(unitEight[1]))
        print('Firepower      : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print('')
        print("""
(╯°□°)--︻╦╤─ - - - 
                """)
        flag = showAssets(myNation,year,flag)
        print('')
        print('[B] Build')
        print('[S] Scrap')
        print(' ')
        print(' ')
        print('[V] View my units')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)
        warSelection = str(input('Please chose an option \n')).upper()
        if warSelection == 'B':
            myNation = buildMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'S':
            myNation = scrapMenu(myNation,year,WAR_BRIEFING)
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'T':
            fast_print('not ready')
        if warSelection == 'V':
            flag = 'yes'
        if warSelection == 'R' or warSelection == '':
            return(myNation)
    return(myNation)





def buildMenu(myNation,year,WAR_BRIEFING):
    era = myNation[0]['Tech']['era']
    WARONE    = WAR_BRIEFING['weapons'][era]['1']
    WARTWO    = WAR_BRIEFING['weapons'][era]['2']
    WARTHREE  = WAR_BRIEFING['weapons'][era]['3']
    WARFOUR   = WAR_BRIEFING['weapons'][era]['4']
    WARFIVE   = WAR_BRIEFING['weapons'][era]['5']
    WARSIX    = WAR_BRIEFING['weapons'][era]['6']
    WARSEVEN  = WAR_BRIEFING['weapons'][era]['7']
    WAREIGHT  = WAR_BRIEFING['weapons'][era]['8']
    flag = ''
    buildSelection = ' '
    show = 'off'
    price = 'off'
    while buildSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']
        firstTech    = myNation[0]['Tech']['researched']['one']
        secondTech   = myNation[0]['Tech']['researched']['two']
        thirdTech    = myNation[0]['Tech']['researched']['three']
        fourthTech   = myNation[0]['Tech']['researched']['four']
        fifthTech    = myNation[0]['Tech']['researched']['five']
        techLevel    = myNation[0]['Tech']['level']
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('               WEAPONS PROCUREMENT       :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team   : ' + str(myNation[1]))
        print('Year      : ' + str(year))
        print('Might     : ' + str(myNation[0]['War']['might']) )
        print('Wealth    : ' + str(myNation[0]['Finance']['wealth']) )
        print('Tech Lv   : ' + str(techLevel) )
        print('')
        print('')
        print('SuperWeapons: ' + str(unitEight[1]))
        print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print('')
        print("""
(╯°□°)--︻╦╤─ - - - 
                """)
        print('')
        print('Build')
        print('[A] ' + str(unitOne[0]))
        print('[B] ' + str(unitTwo[0]))
        print('[C] ' + str(unitThree[0]))
        print('[D] ' + str(unitFour[0]))
        print('[E] ' + str(unitFive[0]))
        print('[F] ' + str(unitSix[0]))
        print('[G] ' + str(unitSeven[0]))
        print('[H] ' + str(unitEight[0]))
        print('')
        print('')
        if price == 'on':
            print('======================')
            print('       Pricings       ')
            print('======================')
            print('______________________')
            print('Light Unit            :')
            print('----------------------')
            print(str(WARONE[0]) + ' = $' + str(WARONE[2]))
            print('buildTime    = ' + str(WARONE[3]))
            print('MightPoints  = +' + str(WARONE[4]) + '%')
            print('')
            print(str(WARTWO[0]) + ' = $' + str(WARTWO[2]))
            print('buildTime    = ' + str(WARTWO[3]))
            print('MightPoints  = +' + str(WARTWO[4]) + '%')
            print('')
            print('______________')
            print('Core Division         : ')
            print('--------------')
            print(str(WARTHREE[0]) + ' = $' + str(WARTHREE[2]))
            print('buildTime    = ' + str(WARTHREE[3]))
            print('MightPoints  = +' + str(WARTHREE[4]) + '%')
            print('')
            print(str(WARFOUR[0]) + ' = $' + str(WARFOUR[2]))
            print('buildTime    = ' + str(WARFOUR[3]))
            print('MightPoints  = +' + str(WARFOUR[4]) + '%')
            print('')
            print(str(WARFIVE[0]) + ' = $' + str(WARFIVE[2]))
            print('buildTime    = ' + str(WARFIVE[3]))
            print('MightPoints  = +' + str(WARFIVE[4]) + '%')
            print('')
            print('______________')
            print('Heavy Forces     : ')
            print('--------------')
            print(str(WARSIX[0]) + ' = $' + str(WARSIX[2]))
            print('buildTime    = ' + str(WARSIX[3]))
            print('MightPoints  = +' + str(WARSIX[4]) + '%')
            print('')
            print(str(WARSEVEN[0]) + ' = $' + str(WARSEVEN[2]))
            print('buildTime    = ' + str(WARSEVEN[3]))
            print('MightPoints  = +' + str(WARSEVEN[4]) + '%')
            print('')
            print('')
            print(str(WAREIGHT[0]) + ' = $' + str(WAREIGHT[2]))
            print('buildTime    = ' + str(WAREIGHT[3]))
            print('MightPoints  = +' + str(WAREIGHT[4]) + '%')
            print('')
            fast_print('Press Enter to clear ')
            price = 'off'
            print('')
        if show == 'on':
            print('Light Unit : ' + str(unitOne[1] + unitTwo[1]))
            print('--------------')
            print(str(unitOne[0]) +  ' : ' + str(unitOne[1]))
            print(str(unitTwo[0]) +   ' : ' + str(unitTwo[1]))
            print('')
            print('Core Division : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
            print('--------------')
            print(str(unitThree[0]) +   ' : ' + str(unitThree[1]))
            print(str(unitFour[0]) +   ' : ' + str(unitFour[1]))
            print(str(unitFive[0]) +   ' : ' + str(unitFive[1]))
            print('')   
            print('Heavy Forces: ' + str(unitSix[1] + unitSeven[1]))
            print('--------------')
            print(str(unitSix[0]) +   ' : ' + str(unitSix[1]))
            print(str(unitSeven[0]) +   ' : ' + str(unitSeven[1]))
            print('')
            print('Super Weapon' )
            print('--------------')
            print(str(unitEight[0]) +   ' : ' + str(unitEight[1]))
            fast_print('press Enter to clear')
            print(' ')
            show = 'off'
        print('Options')
        print('[V] View your units')
        print('[P] Get Unit pricings')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)

        buildSelection = str(input('Please chose an option \n')).upper()

        # LIGHT UNIT
        if buildSelection == 'A':
            clearScreen()
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='1')
        if buildSelection == 'B':
            clearScreen()
            if firstTech[2] < 100:
                print('You need to complete ' + str(firstTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='2')

        # CORE DIVISION
        if buildSelection == 'C':
            clearScreen()
            if secondTech[2] < 100:
                print('You need to complete ' + str(secondTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue 
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='3')
        if buildSelection == 'D':
            clearScreen()
            if thirdTech[2] < 100:
                print('You need to complete ' + str(thirdTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='4')
        if buildSelection == 'E':
            clearScreen()
            if thirdTech[2] < 100:
                print('You need to complete ' + str(thirdTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='5')
        
        # HEAVY FORCES
        if buildSelection == 'F':
            clearScreen()
            if fourthTech[2] < 100:
                print('You need to complete ' + str(fourthTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='6')
        if buildSelection == 'G':
            clearScreen()
            if fourthTech[2] < 100:
                print('You need to complete ' + str(fourthTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='7')
        
        # SUPER WEAPON
        if buildSelection == 'H':
            clearScreen()
            if fifthTech[2] < 100:
                print('You need to complete ' + str(fifthTech[1]) + ' development to unlock.')
                fast_print('Your Tech level is not high enough')
                continue
            myNation = buildUnits(myNation,year,WAR_BRIEFING,unit='8')
        if buildSelection == 'V':
            clearScreen()
            show = 'on'
        if buildSelection == 'P':
            clearScreen()
            price = 'on'
        if buildSelection == 'R' or buildSelection == '':
            return(myNation)
    return(myNation)





def buildUnits(myNation,year,WAR_BRIEFING,unit):

    era = myNation[0]['Tech']['era']

    name       = WAR_BRIEFING['weapons'][era][unit][0]
    price      = WAR_BRIEFING['weapons'][era][unit][2]
    wait       = WAR_BRIEFING['weapons'][era][unit][3]
    bonusMight = WAR_BRIEFING['weapons'][era][unit][4]
    credits    = myNation[0]['Finance']['wealth']

    maxpurchase = int(credits // price)
    print('Note* This unit as a wait time of  ' + str(wait) + ' round[s]')
    print('You can buy up to ' + str(maxpurchase) + ' ' + str(name) + ' at a cost of $' + str(price) + ' each.' )

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
    myNation[0]['Finance']['wealth'] -=  cost
    # Intentional glitch(if user puts in order same time as advance era, they get the next level for the same price)
    myNation[0]['Nextmoves'] += [['submitted','WeaponsBuild',unit, purchaseAmount,wait,bonusMight]]
    print(myNation[0]['Nextmoves'] )
    superfast_print('Purchase order for ' + str(name) + ' placed at a cost of ' + str(cost) + '\n')
    input('Press enter to continue \n')
    return(myNation)








def scrapMenu(myNation,year,WAR_BRIEFING):
    era = myNation[0]['Tech']['era']
    WARONE    = WAR_BRIEFING['weapons'][era]['1']
    WARTWO    = WAR_BRIEFING['weapons'][era]['2']
    WARTHREE  = WAR_BRIEFING['weapons'][era]['3']
    WARFOUR   = WAR_BRIEFING['weapons'][era]['4']
    WARFIVE   = WAR_BRIEFING['weapons'][era]['5']
    WARSIX    = WAR_BRIEFING['weapons'][era]['6']
    WARSEVEN  = WAR_BRIEFING['weapons'][era]['7']
    WAREIGHT  = WAR_BRIEFING['weapons'][era]['8']
    flag = ''
    buildSelection = ' '
    show = 'off'
    price = 'off'
    while buildSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']
        techLevel    = myNation[0]['Tech']['level']
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('                    SCRAP YARD           :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team   : ' + str(myNation[1]))
        print('Year      : ' + str(year))
        print('Might     : ' + str(myNation[0]['War']['might']) )
        print('Wealth    : ' + str(myNation[0]['Finance']['wealth']) )
        print('Tech Lv   : ' + str(techLevel) )
        print('')
        print('')
        print('SuperWeapons: ' + str(unitEight[1]))
        print('Total Firepower : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print('')
        print("""
(╯°□°)--︻╦╤─ - - - 
                """)
        print('')
        print('Scrap')
        print('[A] ' + str(unitOne[0]))
        print('[B] ' + str(unitTwo[0]))
        print('[C] ' + str(unitThree[0]))
        print('[D] ' + str(unitFour[0]))
        print('[E] ' + str(unitFive[0]))
        print('[F] ' + str(unitSix[0]))
        print('[G] ' + str(unitSeven[0]))
        print('[H] ' + str(unitEight[0]))
        print('')
        print('')
        if price == 'on':
            print('======================')
            print('       VALUATIONS     ')
            print('======================')
            print('______________________')
            print('Light Unit            :')
            print('----------------------')
            print(str(WARONE[0]) + ' = $' + str(WARONE[2]))
            print('buildTime    = ' + str(WARONE[3]))
            print('MightPoints  = +' + str(WARONE[4]) + '%')
            print('')
            print(str(WARTWO[0]) + ' = $' + str(WARTWO[2]))
            print('buildTime    = ' + str(WARTWO[3]))
            print('MightPoints  = +' + str(WARTWO[4]) + '%')
            print('')
            print('______________')
            print('Core Division         : ')
            print('--------------')
            print(str(WARTHREE[0]) + ' = $' + str(WARTHREE[2]))
            print('buildTime    = ' + str(WARTHREE[3]))
            print('MightPoints  = +' + str(WARTHREE[4]) + '%')
            print('')
            print(str(WARFOUR[0]) + ' = $' + str(WARFOUR[2]))
            print('buildTime    = ' + str(WARFOUR[3]))
            print('MightPoints  = +' + str(WARFOUR[4]) + '%')
            print('')
            print(str(WARFIVE[0]) + ' = $' + str(WARFIVE[2]))
            print('buildTime    = ' + str(WARFIVE[3]))
            print('MightPoints  = +' + str(WARFIVE[4]) + '%')
            print('')
            print('______________')
            print('Heavy Forces     : ')
            print('--------------')
            print(str(WARSIX[0]) + ' = $' + str(WARSIX[2]))
            print('buildTime    = ' + str(WARSIX[3]))
            print('MightPoints  = +' + str(WARSIX[4]) + '%')
            print('')
            print(str(WARSEVEN[0]) + ' = $' + str(WARSEVEN[2]))
            print('buildTime    = ' + str(WARSEVEN[3]))
            print('MightPoints  = +' + str(WARSEVEN[4]) + '%')
            print('')
            print('')
            print(str(WAREIGHT[0]) + ' = $' + str(WAREIGHT[2]))
            print('buildTime    = ' + str(WAREIGHT[3]))
            print('MightPoints  = +' + str(WAREIGHT[4]) + '%')
            print('')
            fast_print('Press Enter to clear ')
            print('')
            price = 'off'
        if show == 'on':
            print('Light Unit : ' + str(unitOne[1] + unitTwo[1]))
            print('--------------')
            print(str(unitOne[0]) +  ' : ' + str(unitOne[1]))
            print(str(unitTwo[0]) +   ' : ' + str(unitTwo[1]))
            print('')
            print('Core Division : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
            print('--------------')
            print(str(unitThree[0]) +   ' : ' + str(unitThree[1]))
            print(str(unitFour[0]) +   ' : ' + str(unitFour[1]))
            print(str(unitFive[0]) +   ' : ' + str(unitFive[1]))
            print('')   
            print('Heavy Forces: ' + str(unitSix[1] + unitSeven[1]))
            print('--------------')
            print(str(unitSix[0]) +   ' : ' + str(unitSix[1]))
            print(str(unitSeven[0]) +   ' : ' + str(unitSeven[1]))
            print('')
            print('Super Weapon' )
            print('--------------')
            print(str(unitEight[0]) +   ' : ' + str(unitEight[1]))
            print('')
            fast_print('press Enter to clear')
            print(' ')
            show = 'off'
        print('Options')
        print('[V] View your units')
        print('[P] Get Unit scrap valuation')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            print('Moves used up.')
            return(myNation)


        buildSelection = str(input('Please chose an option \n')).upper()
        if buildSelection == 'A':
            clearScreen()
            if unitOne[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'1')
        if buildSelection == 'B':
            clearScreen()
            if unitTwo[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'2')
        if buildSelection == 'C':
            clearScreen()
            if unitThree[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'3')
        if buildSelection == 'D':
            clearScreen()
            if unitFour[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'4')
        if buildSelection == 'E':
            clearScreen()
            if unitFive[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'5')
        if buildSelection == 'F':
            clearScreen()
            if unitSix[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'6')
        if buildSelection == 'G':
            clearScreen()
            if unitSeven[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'7')
        if buildSelection == 'H':
            clearScreen()
            if unitEight[1] < 1:
                fast_print('You dont have any to scrap..')
                continue
            myNation = scrapUnits(myNation,year,WAR_BRIEFING,'8')
        if buildSelection == 'V':
            clearScreen()
            show = 'on'
        if buildSelection == 'P':
            clearScreen()
            price = 'on'
        if buildSelection == 'R' or buildSelection == '':
            return(myNation)
    return(myNation)




def scrapUnits(myNation,year,WAR_BRIEFING,unit):

    era        = myNation[0]['Tech']['era']

    name       = WAR_BRIEFING['weapons'][era][unit][0]
    price      = WAR_BRIEFING['weapons'][era][unit][2]
    wait       = WAR_BRIEFING['weapons'][era][unit][3]
    bonusMight = WAR_BRIEFING['weapons'][era][unit][4]
    unitsOwned = myNation[0]['War']['weapons'][unit][1]

    print('Note* This unit as a wait time of  ' + str(wait) + ' round[s]')
    print('You can scrap up to ' + str(unitsOwned) + ' ' + str(name) + ' for $' + str(price) + ' each.')

    try:
        scrapAmount = int(input('Enter amount to be scrapped \n'))
    except:
        print("Entered incorrectly, please try again")
        return(myNation)

    valuation = scrapAmount * price

    if scrapAmount > unitsOwned:
        input('you entered too much \n')
        return(myNation)
    if scrapAmount < 1:
        input('Enter an incorrect value \n')
        return(myNation)

    # Reduce units and Place Order
    myNation[0]['War']['weapons'][unit][1] -= scrapAmount
    myNation[0]['Nextmoves']               += [['WeaponsScrap',unit, scrapAmount,valuation,bonusMight]]


    superfast_print('Scrap order for ' + str(name) + ' placed at a cost of ' + str(valuation) + '\n')
    print('You will get paid next round \n')
    print('')
    input('Press enter to continue \n')
    return(myNation)




def manoeuvresMenu(myNation,year,WAR_BRIEFING):
    manoeuvresSelection = ' '
    flag = ''
    while manoeuvresSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']


        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('       !!MILITARY MANOEUVRES HQ!!        :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team        : ' + str(myNation[1]))
        print('Year           : ' + str(year))
        print('Might          : ' + str(myNation[0]['War']['might']) )
        print('Rank           : ' + str(myNation[0]['War']['level']))
        print('Light Unit     : ' + str(unitOne[1] + unitTwo[1]))
        print('Core Division  : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
        print('Heavy Forces   : ' + str(unitSix[1] + unitSeven[1]))
        print('SuperWeapons   : ' + str(unitEight[1]))
        print('Firepower      : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print(' ')
        flag = showAssets(myNation,year,flag)
        print('')
        print('[D] Drill your forces')
        print('[J] Joint manoeuvres')
        print('[I] Intimidation manoeuvres')
        print(' ')
        print(' ')
        print('[D] Detailed forces review')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)

        manoeuvresSelection = input('Select an option \n').upper()
        clearScreen()
        if manoeuvresSelection == 'D':
            myNation = drillMenu(myNation,year,WAR_BRIEFING)
        if manoeuvresSelection == 'J':
            print('Not ready')
        if manoeuvresSelection == 'I':
            print('Not ready')
        if manoeuvresSelection == 'D':
            flag = 'yes'
        if manoeuvresSelection == 'R' or manoeuvresSelection == '':
            return(myNation)
    return(myNation)    


"""
# =====================================================================
# =====================================================================
# =====================================================================
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#    DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#     DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
#    DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL DRILL 
# =====================================================================
# =====================================================================
# =====================================================================
"""



def drillMenu(myNation,year,WAR_BRIEFING):
    drillSelection = ' '
    flag = ''
    while drillSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']


        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('       !!MILITARY DRILL HEADQUARTERS!!   :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team        : ' + str(myNation[1]))
        print('Year           : ' + str(year))
        print('Might          : ' + str(myNation[0]['War']['might']) )
        print('Rank           : ' + str(myNation[0]['War']['level']))
        print('Light Unit     : ' + str(unitOne[1] + unitTwo[1]))
        print('Core Division  : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
        print('Heavy Forces   : ' + str(unitSix[1] + unitSeven[1]))
        print('SuperWeapons   : ' + str(unitEight[1]))
        print('Firepower      : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        print(' ')
        flag = showAssets(myNation,year,flag)
        print('')
        print('[L] Light Unit')
        print('[C] Core Division ')
        print('[H] Heavy Forces')
        print(' ')
        print(' ')
        print('[D] Detailed forces review')
        print('[R] Return')
        print(' ')
        print(' ')
        print(' ')
        print('Moves: ' + str(checkMoves(myNation,"%^")[0]) )
        print('****************************************')
        print(' ')
        print(' ')
        # CHECK MAX MOVES SINCE INSIDE WHILE LOOP
        returnCode = checkMoves(myNation,'%^')[1]
        if returnCode > 0: 
            fast_print('All moves used up')
            return(myNation)

        drillSelection = input('Select a divison to train \n').upper()
        clearScreen()
        if drillSelection == 'L':
            if (unitOne[1] + unitTwo[1]) < 1:
                input('No Light assets to train... \n')
                break
            units = [('1',unitOne[1]),('2',unitTwo[1])]
            myNation = drill(myNation, 'Light Units',units,WAR_BRIEFING)
        if drillSelection == 'C':
            if (unitThree[1] + unitFour[1] + unitFive[1]) < 1:
                input('No navy assets to train... \n')
                break
            units = [('3',unitThree[1]),('4',unitFour[1]),('5',unitFive[1])]
            myNation = drill(myNation, 'Core Division',units,WAR_BRIEFING)
        if drillSelection == 'H':
            if (unitSix[1] + unitSeven[1]) < 1:
                input('No airforce assets to train... \n')
                break
            units = [('6',unitSix[1]),('7',unitSeven[1])]
            myNation = drill(myNation, 'Heavy Forces',units,WAR_BRIEFING)
        if drillSelection == 'D':
            flag = 'yes'
        if drillSelection == 'R' or drillSelection == '':
            return(myNation)
    return(myNation)    




def drill(myNation, branch,units,WAR_BRIEFING):
    print('')
    # CHECK MAX MOVES 
    returnCode = checkMoves(myNation,'drill')[1]
    if returnCode > 0: 
        fast_print('All moves used up, or already drilling this round.')
        return(myNation)


    intensity = 'low'
    while intensity != 'XYZFFJJJJJJ':
        print('[S] Soft')
        print('[M] Medium')
        print('[H] Hard')
        print('[I] More Info')
        print('[R] Return')
        intensity = input('How hard do you want to train your ' + str(branch) + '?\n').upper()
        clearScreen()
        if intensity == 'S':
            drillOrder = ['drill',branch,'soft',units]
            break
        if intensity == 'M':
            drillOrder = ['drill',branch,'medium',units]
            break
        if intensity == 'H':
            drillOrder = ['drill',branch,'hard',units]
            break
        if intensity == 'I':
            fast_print('The harder you drill your units the more benefits you will gain, but the risk of loss also increases. \n')
            print('Soft  : Might ++, low probability of loss')
            print('Medium: Might ++, credits ++, medium probability of loss')
            print('Hard  : Might ++, credits ++ newUnits ++, high probability of loss')
            print('Remember drilling your units means they are off standby and unavailable for the next round, be vigilant incase you come under attack.')
            input('Enter to continue \n')
        if intensity == 'R' or intensity == '':
            return(myNation)


    # Deduct units
    for unit in units:
        unit = unit[0]
        myNation[0]['War']['weapons'][unit][1] = 0

    # Place Order
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [drillOrder]

    print('You will drill your ' + str(branch) + ' at ' + str(drillOrder[2]) + ' intensity')
    print('Your '  + str(branch) + ' will embark on training, the units will be returned to you next round.' )
    buffer = input('Press enter to continue \n ')
    return(myNation)



"""
# =====================================================================
# =====================================================================
# =====================================================================
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#      MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#      MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
#     MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION MISSION 
# =====================================================================
# =====================================================================
# =====================================================================
"""

def missionsMenu(myNation,NATION_ARRAY,year,WAR_BRIEFING):
    flag = ''
    friendshipFlag = ''
    missionSelection = ' '
    while missionSelection != 'XYZFFJJJJJJ':
        clearScreen()
        unitOne      = myNation[0]['War']['weapons']['1']
        unitTwo      = myNation[0]['War']['weapons']['2']
        unitThree    = myNation[0]['War']['weapons']['3']
        unitFour     = myNation[0]['War']['weapons']['4']
        unitFive     = myNation[0]['War']['weapons']['5']
        unitSix      = myNation[0]['War']['weapons']['6']
        unitSeven    = myNation[0]['War']['weapons']['7']
        unitEight    = myNation[0]['War']['weapons']['8']
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('                 MISSION PLANNING        :X        ')
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('')
        print('My Team        : ' + str(myNation[1]))
        print('Year           : ' + str(year))
        print('Might          : ' + str(myNation[0]['War']['might']) )
        print('Rank           : ' + str(myNation[0]['War']['level']))
        print('Light Unit     : ' + str(unitOne[1] + unitTwo[1]))
        print('Core Division  : ' + str(unitThree[1] + unitFour[1] + unitFive[1])) 
        print('Heavy Forces   : ' + str(unitSix[1] + unitSeven[1]))
        print('SuperWeapons   : ' + str(unitEight[1]))
        print('Firepower      : ' + str(myNation[0]['War']['firePower']) )
        print(' ')
        flag = showAssets(myNation,year,flag)
        friendshipFlag = showFriendship(myNation,friendshipFlag)
        print('')
        print('[E] Espionage')
        print('[C] Covert Operations')
        print('[T] Tactical Strike')
        print('[D] Declare War')
        print(' ')
        print(' ')
        print(' ')
        print('[F] Show Friendships (Internaitonal Relations)')
        print('[S] Show Military Assets')
        print('[H] Help & Explanation')
        print('[R] Return')
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
        missionSelection = str(input('Please chose an option \n')).upper()
        if missionSelection == 'E':
            myNation = espionage(myNation,NATION_ARRAY,WAR_BRIEFING)
        if missionSelection == 'C':
            myNation = covert(myNation,NATION_ARRAY,WAR_BRIEFING)
        if missionSelection == 'T':
            fast_print('not ready')
        if missionSelection == 'D':
            fast_print('not ready')
        if missionSelection == 'F':
            friendshipFlag = 'Y'
        if missionSelection == 'S':
            flag = 'yes'
        if missionSelection == 'H':
            print('*****Explanation of Options *****')
            print('')
            print('ESPIONAGE: Obtains intel about enemy, a small amount of points and forces them to skip a round. May incur loss in friendship if found out.')
            print('COVERT OPERATIONS: Damage an enemy moderately, possibility of stealing resources, May incur signiciant loss in friendship if found out.')
            print('TACTICAL STRIKE: Damage an enemy severely, signiciant drop in friendship and possible repercussions.')
            print('DECLARE WAR: Forces the enemy into a round by round battle of attrition, only military moves can be carried out. You can win, lose, surrender or offer a truce. Will lose some global backing.')
            print('***All Options depend on your frienship levels with the nation state.')
            print('')
            input('Enter to continue')
        if missionSelection == 'R' or missionSelection == '':
            return(myNation)
    return(myNation)



def covert(myNation,NATION_ARRAY,WAR_BRIEFING):
    covertThreshold = -20
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'covert')[1]
    if returnCode > 0: return(myNation)
    
    returnCode,NationChoice = selectCountry(NATION_ARRAY,myNation,'****CHOOSE A TARGET****')
    if returnCode > 0: return(myNation)
    
    # CHECK FRIENDSHIP 
    if myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level'] > covertThreshold:
        print('Sorry, your friendship with ' + str(NATION_ARRAY[NationChoice][-1]) + ' is ' + str(myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level']) + '.  \n Covert operations are only available when friendship deteriorates below < ' + str(covertThreshold) + '. \n Please check international relations option to view friendship levels.')
        input('')
        return(myNation)

    covertOrder = ''
    covertChoice = ""
    while covertChoice != 'XYZFFJJJJJJ':
        print('[E] Economy')
        print('[M] Military')
        print('[S] Science')
        print('[P] Politics')
        print(' ')
        print(' ')
        print('[I] More Info')
        print('[R] Return')
        covertChoice = input('What branch of the ' + str(NationChoice) + ' government do you wish to attack? \n').upper()
        clearScreen()
        if covertChoice == 'E':
            covertOrder = ['covert',NationChoice,'economy']
            break
        if covertChoice == 'M':
            covertOrder = ['covert',NationChoice,'military']
            break
        if covertChoice == 'S':
            covertOrder = ['covert',NationChoice,'science']
            break
        if covertChoice == 'P':
            covertOrder = ['covert',NationChoice,'politics']
            break
        if covertChoice == 'I':
            fast_print('Covert lets you steal and damage enemy assets significantly, this gains benefits but can be risky and lead to war \n')
            print('Depending on what branch you target, will result in corresponding gains i.e. . \n')
            print('As your rank increases you can chose to target a specific branch of the government. \n')
            print('Military  : Might ++')
            print('******IF YOUR GAMBIT FAILS, THE CONSEQUENCES COULD BE SEVERE****')
            input('Enter to continue \n')
        if covertChoice == 'R' or covertChoice == '':
            return(myNation)

    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [covertOrder]

    return(myNation)


def espionage(myNation,NATION_ARRAY,WAR_BRIEFING):
    # CHECK MAX MOVES
    returnCode = checkMoves(myNation,'espionage')[1]
    if returnCode > 0: 
        print('You have already carried out espionage this round.')
        return(myNation)
    # SELECT COUNTRY
    returnCode,NationChoice = selectCountry(NATION_ARRAY,myNation,'****CHOOSE A TARGET****')
    if returnCode > 0: return(myNation)
    
    # CHECK FRIENDSHIP EXCEEDS THRESHOLD
    espionageThreshold = 0
    if myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level'] > espionageThreshold:
        print('Sorry, your friendship with ' + str(NATION_ARRAY[NationChoice][-1]) + ' is ' + str(myNation[0]['Friendship'][NATION_ARRAY[NationChoice][-1]]['level']) + '. Espionage is only available when friendship deteriorates below < ' + str(espionageThreshold) + '. \n Please check international relations option to view friendship levels.')
        input('')
        return(myNation)

    # espionageOrder = ''
    # espionageChoice = ""
    # while covertChoice != 'XYZFFJJJJJJ':
    #     print('[E] Economy')
    #     print('[M] Military')
    #     print('[S] Science')
    #     print('[P] Politics')
    #     print('[I] More Info')
    #     print('[R] Return')
    #     espionageChoice = input('What branch of the ' + str(NationChoice) + ' government do you wish to infiltrate? \n').upper()
    #     clearScreen()
    #     if espionageChoice == 'E':
    #         espionageOrder = ['espionage',NationChoice,'economy']
    #         break
    #     if espionageChoice == 'M':
    #         espionageOrder = ['espionage',NationChoice,'military']
    #         break
    #     if espionageChoice == 'S':
    #         espionageOrder = ['espionage',NationChoice,'science']
    #         break
    #     if espionageChoice == 'P':
    #         espionageOrder = ['espionage',NationChoice,'politics']
    #         break
    #     if espionageChoice == 'I':
    #         fast_print('Espionage lets you steal enemy assets, this gains benefits but can be risky and lead to war \n')
    #         print('Depending on what branch you target, will result in corresponding gains i.e. . \n')
    #         print('As your rank increases you can chose to target a specific branch of the government. \n')
    #         print('Military  : Might ++')
    #         print('******IF YOUR GAMBIT FAILS, THE CONSEQUENCES COULD BE SEVERE****')
    #         input('Enter to continue \n')
    #     if espionageChoice == 'R' or espionageChoice == '':
    #         return(myNation)

    espionageOrder = ['espionage',NationChoice]
    myNation[0]['Nextmoves'] = myNation[0]['Nextmoves'] + [espionageOrder]
    input('Espionage orders given..')

    return(myNation)








 

