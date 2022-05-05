
# UTILITIES 
import sys
import time
import itertools

#p = 'All'

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

def preferencePrint(s,p,i,playerNationIndex):
    with open("log.txt", "a") as myfile:
        myfile.write(s)
        myfile.write('\n')

    if p == 'All':
        print(s)
    elif p == 'Me':
        if str(i) == str(playerNationIndex):
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
        return(p)
    if selection == '2':
        p = printupdates(p)
        return(p)
    if selection == '3':
        developer(NATION_ARRAY)
        return(p)



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
    print('2. Exit')

    selection = str(input('Please select an option \n'))
    countrySelected = ' '
    NationChoice = 9999
    if selection == '1':
        while countrySelected != 'Y':
            print('')
            print('Printing nation list')
            print('')

            for x in range(0, len(NATION_ARRAY)):
                print(str(x) + '. ' + str(NATION_ARRAY[x][-1]))
            print('')
            while NationChoice not in range(0, len(NATION_ARRAY)):
                try:
                    NationChoice = int(input('Please chose a country \n'))
                except:
                    print("Entered incorrectly, please try again")

            input('Your chosen country is : ' +    str(NATION_ARRAY[NationChoice][-1]) + '\n')
            print('')   
            countrySelected = 'Y'
            
        for key in NATION_ARRAY[NationChoice][0].keys():
            print(key)
            print(NATION_ARRAY[NationChoice][0][key])
            print('')
            buffer = input('Press Enter to continue \n')
            clearScreen()
        print('all')
        print(NATION_ARRAY[NationChoice])
        input()

    if selection == '2':
        fast_print('Exiting')
        clearScreen()



# returns how many moves remain and error code.
def checkMoves(myNation,duplicateToCheck):
    mlimit = int( myNation[0]['Special']['moveLimit'])
    mvs    = int(len(myNation[0]['Nextmoves']))
    array = myNation[0]['Nextmoves']
    pnding = list(itertools.chain(*array)).count('pending')


    movesLeft = int(mlimit-mvs+pnding)
    if movesLeft < 1: 
        return(movesLeft,1)
    for item in myNation[0]['Nextmoves']:
        if duplicateToCheck in item:
            #print('you have already carried out '  + str(duplicateToCheck) + ' in this round')
            return(movesLeft,1)
    return(movesLeft,0)

def selectCountry(NATION_ARRAY,myNation,printMessage):
    NationChoice = 9999
    countrySelected = ''
    clearScreen()
    while countrySelected != 'Y':
        print('')
        print(printMessage)
        print('')
        for x in range(0, len(NATION_ARRAY)):
            if NATION_ARRAY[x][-1] != myNation[-1]:
                print(str(x) + '. ' + str(NATION_ARRAY[x][-1]))
        print('')
        while NationChoice not in range(0, len(NATION_ARRAY)):
            try:
                 NationChoice = int(input('Please select a country. \n'))
            except:
                print("Entered incorrectly, please try again")
        if NATION_ARRAY[NationChoice][-1] == myNation[-1]:
            print('You cant select your own country ' + str(NATION_ARRAY[NationChoice][-1]) + ' nice try...')
            return(1,NationChoice)
        print('Your chosen country is : ' + str(NATION_ARRAY[NationChoice][-1]) + '\n')
        input('')
        countrySelected = 'Y'
        clearScreen()
    return(0,NationChoice)



def enterMoney(myNation,printMessage):
    creditsAvailable = int(myNation[0]['Finance']['wealth'])
    spendAmount = 0

    if creditsAvailable < 1:
        input('you do not have enough money, sorry')  
        return(1,spendAmount)

    fast_print(str(printMessage) + '\n')
    while spendAmount < 1:
        try:
            spendAmount = int(input('Input amount between 1 and ' + str(creditsAvailable) + '\n'))
        except:
            print("Entered incorrectly, please try again")
    
    if spendAmount > creditsAvailable:
        fast_print('Entered too much')
        return(1,spendAmount)
        clearScreen()
        
    return(0,spendAmount)

# Tech tree in each nation has five catagories that are blank strink
# They need updated according to what era they are in 
# i.e Industrial first key would be 'wool', 
# i.e. when it goes to infoAge it upgrades to 'DigitalElectronics'
# This function takes care of that.  
# Call Example: NATION_ARRAY = updateTechNames(NATION_ARRAY,index,TECH_MAP)

def updateTechNames(NATION_ARRAY,TECH_MAP):
    for index in range(0,len(NATION_ARRAY)):
        current     = NATION_ARRAY[index][0]
        era         = current['Tech']['era']
        updateOne   = TECH_MAP['Era'][era]['one']
        updateTwo   = TECH_MAP['Era'][era]['two']
        updateThree = TECH_MAP['Era'][era]['three']
        updateFour  = TECH_MAP['Era'][era]['four']
        updateFive  = TECH_MAP['Era'][era]['five']
        
        # Update/populate Names
        current['Tech']['researched']['one'][1]    = updateOne
        current['Tech']['researched']['two'][1]    = updateTwo
        current['Tech']['researched']['three'][1]  = updateThree
        current['Tech']['researched']['four'][1]   = updateFour
        current['Tech']['researched']['five'][1]   = updateFive
        
    return(NATION_ARRAY)

