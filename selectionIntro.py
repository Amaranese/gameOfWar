from gameConquest_utilities import slow_print as slow_print
from gameConquest_utilities import med_print as med_print
from gameConquest_utilities import fast_print as fast_print
from gameConquest_utilities import superfast_print as superfast_print
from gameConquest_utilities import clearScreen as clearScreen
from gameConquest_utilities import preferencePrint as preferencePrint
import sys
import time

def start(userName,myNation):
    assistant = 'Arbiter: '
    print(""" 
    @('_')@
                """)
    fast_print('**rustle**....**clunk** ..."oh not again!" \n')
    fast_print(str(assistant) + '....wait... \n')
    time.sleep(0.7)
    fast_print(str(assistant) +'..who the hell are you? How did you get in here? ... \n')
    userName = input('Enter your name \n')
    clearScreen()
    print(' ')
    med_print(str(userName) + ': ... im ' + str(userName) + '\n')
    clearScreen()
    print("""
    @('_')@
                """)
    fast_print(str(assistant) + 'ah, so YOU are the one. \n')
    time.sleep(0.4)
    fast_print(str(assistant) + 'Its truly an honour to meet you ' + str(userName) +  ' please know that we all appreciate your sacrifice  \n')
    fast_print(str(assistant) + '...are you ready?  \n ')
    print('')
    input(' Press enter to continue..')
    clearScreen()
    print(""" 
    @('_')@
                """)
    fast_print(str(assistant) + 'executing dynamic cascade sequence now, this should feel... uh..uh....  \n ')
    time.sleep(0.6)
    fast_print('....a little weird \n ')
    time.sleep(1.50)
    clearScreen()
    time.sleep(1.50)

    for y in range(0,3):
        for x in range(0,10):
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        time.sleep(0.50)
    fast_print('..........universe destruction in progress......\n')
    for x in range(0,10):
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    time.sleep(0.50)
    for x in range(0,10):
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    time.sleep(0.50)
    for x in range(0,10):
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    fast_print('....booting up universe simulation #734 omega .......\n')
    for y in range(0,3):
        for x in range(0,10):
            print('><><><>><><><>><><><>><><><>><><><>><><><>><><><>><><><')
        time.sleep(0.50)
    time.sleep(0.580)
    for y in range(0,3):
        for x in range(0,5):
            print('asklfdj;l;j;adfj;kj;afdkjaklsdjfaghaldg;asdkjf;lkja;ajd')
        time.sleep(0.30)
        for x in range(0,5):
            print('skakdf 9873472393khgfas lalsdjhf lkladf iuhwer 82348989')
        time.sleep(0.30)
        for x in range(0,5):
            print('sweir;nvda;eradf jasd;klfjasfjghlaadsljfh lasdhfhdlafdd')
        time.sleep(0.50)
    for y in range(0,3):
        for x in range(0,10):
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        time.sleep(0.50)
    clearScreen()
    time.sleep(1.10)
    med_print('....Lead me, follow me, or get out of my way ........ \n')
    print('(George S Patton)')
    time.sleep(1.90)
    clearScreen()
    for x in range(0,20):
        print(' ')
    time.sleep(0.50)
    print('')
    y = 5
    for x in range(0, 5):
        print(str(y))
        y= y-1
        time.sleep(1.20)
        clearScreen()



    fast_print('Good morning commander ' + str(userName) + '..... \n')
    fast_print('')
    time.sleep(0.80)
    fast_print('The year is 1949, the devestating and costly war has finally come to an end.\nIt is your responsibility to lead ' + str(myNation[-1]) + ' to greatness. \n')
    time.sleep(0.80)
    fast_print('There are many ways to win, trade, politics, war....the path is up to you? \n')
    time.sleep(1.50)
    return(userName)

"""
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                              END SECTION
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""

