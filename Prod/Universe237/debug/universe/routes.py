from flask import render_template, url_for, request, redirect, flash
from datetime import datetime
import random 
from universe import app
from flask_sqlalchemy import SQLAlchemy


@app.route('/', methods=['GET', 'POST'])
@app.route('/begin', methods=['GET', 'POST'])
def begin():


    if request.method == 'POST':
        # START GAME 
        if request.form.get('begin'):
            userChoice = request.form['begin']
            print(userChoice)

            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conquest.db'
            db = SQLAlchemy(app)

            from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,techEraCost,PTcHistory,printDialogue,dialogue,initializeRPAverages
            from universe.routesFunctions  import checkMoves,buyResource,sellResource,investCountryFunction,investResourceFunction,drill,buildFunction,scrapFunction,espionage,advanceEra,researchTech,researchGrant
            from universe.nextRound import processRound

            # Being Thorough 
            db.create_all()
            db.drop_all()
            db.create_all()

            warDataBase.query.delete()
            PTc.query.delete()
            NATIONS.query.delete()
            warAssets.query.delete()
            gameTracker.query.delete()

            initializeObjects(db)
            # INIT MYNATION (only add one row initialized)
            myNation = gameTracker()
            db.session.add(myNation)
            initializeRPAverages(db)
            db.session.commit()

            # # EXAMPLE
            myNation = ''
            global averageRPOne,AverageRPTwo,AverageRPThree
            setup = db.session.query(gameTracker).first()
            averageRPOne   = setup.eraOneAverageRP
            AverageRPTwo   = setup.eraTwoAverageRP
            AverageRPThree = setup.eraThreeAverageRP


            return redirect(url_for('index'))



    return(render_template('index.html'))










def getParms(selected):
    # SETUP YEAR = 1949
    if selected == 'year':
        playerNation = gameTracker.query.get_or_404(1)
        year = str(playerNation.year)
        month = str(playerNation.month)
        if month == "1": month = 'January'
        if month == '2': month = 'February'
        if month == '3': month = 'March'
        if month == '4': month = 'April'
        if month == '5': month = 'May'
        if month == '6': month = 'June'
        if month == '7': month = 'July'
        if month == '8': month = 'August'
        if month == '9': month = 'September'
        if month == '10': month = 'October'
        if month == '11': month = 'November'
        if month == '12': month = 'December'
        return(year,month)
    if selected == 'myNation':
        playerNation = gameTracker.query.get_or_404(1)
        myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
        return(myNation)
    if selected == 'nations':
        nations = db.session.query(NATIONS).all()
        return(nations)
    return(year)









@app.route('/start', methods=['GET', 'POST'])
def index():

    # If started don't let change nations
    myNation = gameTracker.query.get_or_404(1)
    if myNation.started > 0: 
        return redirect(url_for('mainMenu'))

    if request.method == 'POST':
        # START GAME 
        if request.form.get('start'):
            myNation.started = 1
            db.session.commit()
            print('------GAME STARTED-------- country: ' + str(myNation.country))
            return redirect(url_for('mainMenu'))

        # SELECT NATION
        if request.form.get('select_nation'):
            return redirect(url_for('selectNation'))

        # GET STATS
        if request.form.get('country_stats'):
            return redirect(url_for('countryStats'))


    return render_template('start.html')




@app.route('/countryStats', methods=['GET', 'POST'])

def countryStats():
    nations = getParms('nations')
    if request.method == 'POST':
        if request.form.get('return'):
            return redirect(url_for('index'))


    return(render_template('countryStats.html',nations=nations))





@app.route('/selectNation', methods=['GET', 'POST'])

def selectNation():
    nations = getParms('nations')
    if request.method == 'POST':
        if request.form.get('select'):
            # Get User entered ID
            selectedID = request.form.get('select')
            selected = NATIONS.query.get_or_404(int(selectedID))
            # Setting this field to identify which nation is the players
            selected.selected = 1
            db.session.commit()
            
            # Update player database
            myNation = gameTracker.query.get_or_404(1)
            myNation.countryID = selected.id
            myNation.country   = selected.country
            db.session.commit()

            #Verify update by printing to terminal
            myNation = gameTracker.query.get_or_404(1)
            print('Selected nation is: ' + str(myNation))

            #Check no more than one row on player database
            if int(db.session.query(gameTracker).count()) > 1:
                exit()
            return redirect(url_for('index'))
        else:   
            print('Something went wrong')
    return(render_template('selectNation.html',nations=nations))


@app.route('/mainMenu', methods=['GET', 'POST'])
def mainMenu():
    # Clear last years dialogue
    updateDialogue = db.session.query(dialogue).all()
    updates = []
    xcount = 0
    # Lazy coding
    for item in updateDialogue:
        if item.AIPrintLine is None:
            continue
        if 'The current country' in item.AIPrintLine: continue 
        if '------------------' in item.AIPrintLine: continue
        if '++++++++++++++++' in item.AIPrintLine: continue 
        if '--------END-------' in item.AIPrintLine: continue
        if 'Time Remaining' in item.AIPrintLine: continue
        updates.append(item.AIPrintLine)
        xcount +=1
        if xcount > 10: break

    dialogue.query.delete()
    db.session.commit()
    year,month = getParms('year')
    myNation = getParms('myNation')
    movesLeft = checkMoves(myNation,'%^')[0]
    displayFlag = ""
    notes = ""
    # If there are any updates, print and flush
    if len(myNation.notes) > 0:
        displayFlag = "notes"
        notes = myNation.notes
        notes = notes.split(':')
        myNation.notes = ""
        db.session.commit()

    if len(updates) < 1:
        updates = ['Welcome to Universe 237', 'This game is a work in progress and still not complete.' , 'For suggestions and queries email murchie85@gmail.com']



    if request.method == 'POST':
        if request.form.get('LB'):
            return redirect(url_for('LB'))
        if request.form.get('FB'):
            return redirect(url_for('financeMenu'))
        if request.form.get('MW'):
            return redirect(url_for('warMenu'))
        if request.form.get('T'):
            return redirect(url_for('techMenu'))
        if request.form.get('N'):
            # Process Next year
            message = processRound(db,averageRPOne,AverageRPTwo,AverageRPThree)
            return redirect(url_for('nextYear'))




    return(render_template('mainMenu.html',year=year,month=month, myNation = myNation,movesLeft=movesLeft,notes=notes,displayFlag=displayFlag, updates=updates))



@app.route('/LeaderBoard', methods=['GET', 'POST'])
def LB():
    year,month = getParms('year')
    allNations = db.session.query(NATIONS).order_by(-NATIONS.score).all()

    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))


    return(render_template('LB.html',year=year,month=month,allNations=allNations))

@app.route('/LeaderBoardRanks', methods=['GET', 'POST'])
def LBrank():
    year,month = getParms('year')
    allNations = db.session.query(NATIONS).order_by(-NATIONS.score).all()
    playerTech = techAssets.query.filter_by(active=1).all()

    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))


    return(render_template('LBrank.html',year=year,month=month,allNations=allNations,playerTech=playerTech))



@app.route('/LeaderBoardScience', methods=['GET', 'POST'])
def LBscience():
    year,month = getParms('year')
    allNations = db.session.query(NATIONS).order_by(-NATIONS.score).all()
    playerTech = techAssets.query.filter_by(active=1).all()

    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))


    return(render_template('LBscience.html',year=year,month=month,allNations=allNations,playerTech=playerTech))

@app.route('/LeaderBoardWar', methods=['GET', 'POST'])
def LBwar():
    year,month = getParms('year')
    allNations = db.session.query(NATIONS).order_by(-NATIONS.score).all()
    playerWar = warAssets.query.filter_by(active=1).all()

    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))


    return(render_template('LBwar.html',year=year,month=month,playerWar=playerWar))








#---------------------------------------------------------
#                      FINANCE ROUTES
#---------------------------------------------------------

@app.route('/financeMenu', methods=['GET', 'POST'])
def financeMenu():
    year,month = getParms('year')
    myNation = getParms('myNation')
    movesLeft = checkMoves(myNation,'%^')[0]

    
    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))
        if request.form.get('Gamble'):
            return redirect(url_for('gambleMenu'))
        if request.form.get('Trade'):
            print('trade selected')
            return redirect(url_for('tradeMenu'))
        if request.form.get('invest'):
            print('invest selected')
            return redirect(url_for('investMenu'))

    return(render_template('financeMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft))


@app.route('/gambleMenu', methods=['GET', 'POST'])
def gambleMenu():
    year,month = getParms('year')
    myNation = getParms('myNation')
    myWealth = myNation.wealth 
    movesChecked = checkMoves(myNation,'gamble')
    if movesChecked[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))

    message = "Enter a gamble amount.."


    if request.method == 'POST':
        if request.form.get('gamble'):
            gambleAmount = request.form['gamble']
            gambleAmount = int(gambleAmount)
            if isinstance(gambleAmount,int):
                if  gambleAmount <=  myWealth and gambleAmount > 0:
                    print('success')
                    print(gambleAmount)
                    
                    #Deduct wealth & set next move
                    myNation.wealth -= gambleAmount
                    myNation.Nextmoves += str('gamble' + ',' + str(gambleAmount) + ':')
                    db.session.commit()
                    print(myNation)

                    return redirect(url_for('mainMenu'))
            else:
                print('caught')
                print(gambleAmount)
                print(type(gambleAmount))
                message = 'You entered an incorrect amount'


        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))


    return(render_template('gambleMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesChecked[0],message=message))



@app.route('/tradeMenu', methods=['GET', 'POST'])
def tradeMenu():
    year,month = getParms('year')
    myNation = getParms('myNation')
    myWealth = myNation.wealth 
    PT  = PTc.query.order_by(PTc.id).all()
    displayFlag = "main"
    movesChecked = checkMoves(myNation,'gamble')

    if request.method == 'POST':
        if request.form.get('buy'):
            return redirect(url_for('buyMenu'))
        if request.form.get('sell'):
            return redirect(url_for('sellMenu'))


        if request.form.get('average'):
            displayFlag = "average"

        if request.form.get('historical'):
            displayFlag = "historical"

        if request.form.get('marketStock'):
            displayFlag = "stock"

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))



    return(render_template('tradeMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesChecked[0],PT=PT,displayFlag=displayFlag))


@app.route('/buyMenu', methods=['GET', 'POST'])
def buyMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    myWealth = myNation.wealth 
    PT  = PTc.query.order_by(PTc.id).all()
    displayFlag = "main"
    purchaseFlag = ''
    global commodity
    global commodityFlag
    commodityFlag = ''
    message =''

    movesChecked = checkMoves(myNation,'buy')

    if movesChecked[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))

    if request.method == 'POST':

        # If user clicks a resource, display a form
        if request.form.get('selectCommodity'):
            commodity = request.form.get('selectCommodity')
            purchaseFlag = "buyCommodity"
            commodityFlag = str(commodity)

        if request.form.get('buyCommodity'):
            if commodity is not None:
                print('called')
                purchaseAmount = request.form.get('buyCommodity')
                buyResult = buyResource(myNation,purchaseAmount,commodity,PT,db)
                message = buyResult[1]
                print('message')
                print(message)


        if request.form.get('average'):
            displayFlag = "average"

        if request.form.get('historical'):
            displayFlag = "historical"

        if request.form.get('marketStock'):
            displayFlag = "stock"

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('buyMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesChecked[0],PT=PT,displayFlag=displayFlag, message=message,purchaseFlag=purchaseFlag,commodityFlag=commodityFlag))



@app.route('/sellMenu', methods=['GET', 'POST'])
def sellMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    myWealth = myNation.wealth 
    PT  = PTc.query.order_by(PTc.id).first() 

    displayFlag = "main"
    purchaseFlag = ''
    global commodity
    global commodityFlag
    salesFlag = ""
    commodityFlag = ''
    message =''

    movesChecked = checkMoves(myNation,'sell')
    if movesChecked[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))

    if request.method == 'POST':

        # If user clicks a resource, display a form
        if request.form.get('selectCommodity'):
            commodity = request.form.get('selectCommodity')
            salesFlag = "sellCommodity"
            commodityFlag = str(commodity)

        if request.form.get('sellCommodity'):
            if commodity is not None:
                print('called')
                sellAmount = request.form.get('sellCommodity')
                sellResult = sellResource(myNation,sellAmount,commodity,PT,db)
                message = sellResult[1]
                print('message')
                print(message)


        if request.form.get('average'):
            displayFlag = "average"

        if request.form.get('historical'):
            displayFlag = "historical"

        if request.form.get('marketStock'):
            displayFlag = "stock"

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('sellMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesChecked[0],PT=PT,displayFlag=displayFlag, message=message,salesFlag=salesFlag,commodityFlag=commodityFlag))


@app.route('/investMenu', methods=['GET', 'POST'])
def investMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    myWealth = myNation.wealth 
    global PT
    PT  = PTc.query.order_by(PTc.id).first()
    movesChecked = checkMoves(myNation,'^&')

    displayFlag = "main"
    global commodity
    global commodityToSubmit
    global commodityPrice
    commodity = ''
    formMessage = ''
    message =''
    friends =db.session.query(friendship).filter_by(country=myNation.country).all()



    if request.method == 'POST':


        if request.form.get('countries'):
            movesChecked = checkMoves(myNation,'investCountry')
            if movesChecked[1] > 0:
                print('Not enough moves or already carried this move out')
                return redirect(url_for('mainMenu'))
            
            return redirect(url_for('investCountry'))

        if request.form.get('gold'):
            commodity = 'gold'
            commodityPrice = PT.goldPrice
            commodityToSubmit = commodity
            displayFlag = "investCommodity"


        if request.form.get('rareMetals'):
            commodity = 'rareMetals'
            commodityPrice = PT.rareMetalsPrice
            commodityToSubmit = commodity
            displayFlag = "investCommodity"

        if request.form.get('gems'):
            commodity = 'gems'
            commodityPrice = PT.gemsPrice
            commodityToSubmit = commodity
            displayFlag = "investCommodity"

        if request.form.get('oil'):
            commodity = 'oil'
            commodityPrice = PT.oilPrice
            commodityToSubmit = commodity
            displayFlag = "investCommodity"



        if request.form.get('investResourceForm'):
            movesChecked = checkMoves(myNation,'investResource')
            if movesChecked[1] > 0:
                print('Not enough moves or already carried this move out')
                return redirect(url_for('mainMenu'))

            investAmount = request.form.get('investResourceForm')
            investResult = investResourceFunction(myNation,investAmount,commodityPrice,commodityToSubmit,db)
            formMessage = investResult[1] 



        if request.form.get('friendship'):
            displayFlag = "friendship"

        if request.form.get('resources'):
            displayFlag = "resources"

        if request.form.get('average'):
            displayFlag = "average"

        if request.form.get('historical'):
            displayFlag = "historical"

        if request.form.get('marketStock'):
            displayFlag = "stock"

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('investMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesChecked[0],PT=PT,displayFlag=displayFlag, message=message,formMessage=formMessage,commodity=commodity,friends=friends))


@app.route('/investCountry', methods=['GET', 'POST'])
def investCountry():
    playerNation = gameTracker.query.get_or_404(1)
    nations = db.session.query(NATIONS).all()
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    selectedOut = ""
    message = ""
    infoMessage = ""
    nationSelectedFlag = ""

    # Check moves 
    movesChecked = checkMoves(myNation,'investCountry')
    if movesChecked[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    if request.method == 'POST':
        # If nation picked - display form
        if request.form.get('select'):
            # Get User entered ID
            selectedID = request.form.get('select')
            global selected
            selected = NATIONS.query.get_or_404(int(selectedID))
            selectedOut = selected 
            nationSelectedFlag = "selected"

        if request.form.get('investForm'):
            if selected is not None:
                investAmount = request.form.get('investForm')
                investResult = investCountryFunction(myNation,investAmount,selected,db)
                message = investResult[1] 

    if request.form.get('mainMenu'):
        return redirect(url_for('mainMenu'))

    if request.form.get('information'):
        infoMessage = 'Investing in the growth of a country, helps boost friendship and earns money.'


    return(render_template('investCountry.html',nations=nations,myNation=myNation,nationSelectedFlag=nationSelectedFlag,selectedOut=selectedOut,message=message,infoMessage=infoMessage))


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                   END   FINANCE ROUTES
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




#---------------------------------------------------------
#                      WAR ROUTES
#---------------------------------------------------------

@app.route('/warMenu', methods=['GET', 'POST'])
def warMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    movesLeft = checkMoves(myNation,'%^')[0]

    
    if request.method == 'POST':
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))
        if request.form.get('combat'):
            return redirect(url_for('maneuvers'))
        if request.form.get('weapons'):
            return redirect(url_for('weaponsMenu'))
        if request.form.get('offensive'):
            return redirect(url_for('planning'))

    return(render_template('warMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft))

@app.route('/maneuvers', methods=['GET', 'POST'])
def maneuvers():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    myWar    = db.session.query(warAssets).filter_by(country=myNation.country,era=myNation.era).first()
    displayFlag = ""
    message = " "

    # Works the best
    movesToCheck = checkMoves(myNation,'drill')
    movesLeft = movesToCheck[0]
    if movesToCheck[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    if request.method == 'POST':
        if request.form.get('drill'):
            displayFlag = 'drill'

        if request.form.get('division'):
            displayFlag = 'intensity'
            global division
            division = request.form.get('division')

        if request.form.get('intensity'):
            displayFlag = 'intensity'
            intensity = request.form.get('intensity')
            print(intensity)
            print(division)
            drillResult = drill(myNation,myWar,division,intensity,db)
            message = drillResult[1]
            print(message)

        if request.form.get('combat'):
            return redirect(url_for('mainMenu'))



        if request.form.get('review'):
            displayFlag = 'combat'
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('maneuvers.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,myWar=myWar,displayFlag=displayFlag,message=message))


@app.route('/weaponsMenu', methods=['GET', 'POST'])
def weaponsMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    
    myWar    = db.session.query(warAssets).filter_by(country=myNation.country,era=myNation.era).first()
    lightForces = int(myWar.wOneAmount) + int(myWar.wTwoAmount)
    coreForces = int(myWar.wThreeAmount) + int(myWar.wFourAmount) + int(myWar.wFiveAmount)
    heavyForces = int(myWar.wSixAmount) + int(myWar.wSevenAmount)
    displayFlag = ""
    # Works the best
    movesToCheck = checkMoves(myNation,'&^')
    movesLeft = movesToCheck[0]
    if movesToCheck[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    
    if request.method == 'POST':
        if request.form.get('build'):
            return redirect(url_for('build'))
        if request.form.get('scrap'):
            return redirect(url_for('scrap'))

        if request.form.get('review'):
            displayFlag = 'combat'
        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('weaponsMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,displayFlag=displayFlag,lightForces=lightForces,coreForces=coreForces,heavyForces=heavyForces,myWar=myWar))


@app.route('/build', methods=['GET', 'POST'])
def build():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    
    myWar    = db.session.query(warAssets).filter_by(country=myNation.country,era=myNation.era).first()
    lightForces = int(myWar.wOneAmount) + int(myWar.wTwoAmount)
    coreForces = int(myWar.wThreeAmount) + int(myWar.wFourAmount) + int(myWar.wFiveAmount)
    heavyForces = int(myWar.wSixAmount) + int(myWar.wSevenAmount)
    warPricing  = db.session.query(warDataBase).filter_by(era=myNation.era).all()

    displayFlag = ""
    buildMessage = ""
    # Works the best
    movesToCheck = checkMoves(myNation,'x')
    movesLeft = movesToCheck[0]
    if movesToCheck[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    
    if request.method == 'POST':
        if request.form.get('build'):
            displayFlag = 'build'
            global unitSelected 
            unitSelected = request.form.get('build')
            buildMessage = unitSelected

        if request.form.get('buildForm'):
            buildAmount  = request.form.get('buildForm')
            unitSelected = unitSelected
            priceRow     = db.session.query(warDataBase).filter_by(era=myNation.era,unit_name=unitSelected).first()
            buildResult  = buildFunction(myNation,myWar,unitSelected,priceRow,buildAmount,db)
            buildMessage = buildResult[1]

        if request.form.get('review'):
            displayFlag = 'review'

        if request.form.get('disposition'):
            displayFlag = 'disposition'
            

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('build.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,displayFlag=displayFlag,lightForces=lightForces,coreForces=coreForces,heavyForces=heavyForces,myWar=myWar,buildMessage=buildMessage,warPricing=warPricing))

@app.route('/scrap', methods=['GET', 'POST'])
def scrap():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    
    myWar    = db.session.query(warAssets).filter_by(country=myNation.country,era=myNation.era).first()
    lightForces = int(myWar.wOneAmount) + int(myWar.wTwoAmount)
    coreForces = int(myWar.wThreeAmount) + int(myWar.wFourAmount) + int(myWar.wFiveAmount)
    heavyForces = int(myWar.wSixAmount) + int(myWar.wSevenAmount)
    warPricing  = db.session.query(warDataBase).filter_by(era=myNation.era).all()

    displayFlag = ""
    scrapMessage = ""
    # Works the best
    movesToCheck = checkMoves(myNation,'WeaponsScrap')
    movesLeft = movesToCheck[0]
    if movesToCheck[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    
    if request.method == 'POST':
        if request.form.get('scrap'):
            displayFlag = 'scrap'
            global unitSelected 
            unitSelected = request.form.get('scrap')
            scrapMessage = unitSelected

        if request.form.get('scrapForm'):
            scrapAmount  = request.form.get('scrapForm')
            unitSelected = unitSelected
            priceRow     = db.session.query(warDataBase).filter_by(era=myNation.era,unit_name=unitSelected).first()
            scrapResult  = scrapFunction(myNation,myWar,unitSelected,priceRow,scrapAmount,db)
            scrapMessage = scrapResult[1]

        if request.form.get('review'):
            displayFlag = 'review'

        if request.form.get('disposition'):
            displayFlag = 'disposition'
            

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('scrap.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,displayFlag=displayFlag,lightForces=lightForces,coreForces=coreForces,heavyForces=heavyForces,myWar=myWar,scrapMessage=scrapMessage,warPricing=warPricing))

@app.route('/planning', methods=['GET', 'POST'])
def planning():
    year,month = getParms('year')
    # VARIABLES FOR CONDITIONS AND FUNCTIONS
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    nations = db.session.query(NATIONS).all()
    myWar    = db.session.query(warAssets).filter_by(country=myNation.country,era=myNation.era).first()
    lightForces = int(myWar.wOneAmount) + int(myWar.wTwoAmount)
    coreForces = int(myWar.wThreeAmount) + int(myWar.wFourAmount) + int(myWar.wFiveAmount)
    heavyForces = int(myWar.wSixAmount) + int(myWar.wSevenAmount)
    friends =db.session.query(friendship).filter_by(country=myNation.country).all()

    displayFlag = ""
    planningMessage = ""
    
    # Works the best
    movesToCheck = checkMoves(myNation,'espionage')
    movesLeft = movesToCheck[0]
    if movesToCheck[1] > 0:
        print('Not enough moves or already carried this move out')
        return redirect(url_for('mainMenu'))


    
    if request.method == 'POST':
        if request.form.get('espionage'):
            displayFlag = 'espionage'
            planningMessage = 'Pick a nation to sabotage'

        if request.form.get('select'):
            # Get User entered ID
            selectedID = request.form.get('select')
            global selected
            selected = NATIONS.query.get_or_404(int(selectedID))
            selectedOut = selected 
            #planningMessage = 'you selected ' + str(selectedOut.country)
            enemy =db.session.query(friendship).filter_by(country=myNation.country, targetCountry=selectedOut.country).first()
            friendshipLevel = enemy.level
            targetNation = selectedOut.country
            planningMessage = espionage(myNation,targetNation,friendshipLevel,db)
            planningMessage = planningMessage[1]

        if request.form.get('review'):
            displayFlag = 'review'

        if request.form.get('disposition'):
            displayFlag = 'disposition'

        if request.form.get('friendship'):
            displayFlag = 'friendship'
            

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('planning.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,displayFlag=displayFlag,lightForces=lightForces,coreForces=coreForces,heavyForces=heavyForces,myWar=myWar,planningMessage=planningMessage,friends=friends,nations=nations))






#---------------------------------------------------------
#                      TECH ROUTES
#---------------------------------------------------------



@app.route('/techMenu', methods=['GET', 'POST'])
def techMenu():
    year,month = getParms('year')
    playerNation = gameTracker.query.get_or_404(1)
    myNation = NATIONS.query.get_or_404(int(playerNation.countryID))
    movesLeft = checkMoves(myNation,'%^')[0]
    displayFlag = ""

    
    if request.method == 'POST':
        if request.form.get('academia'):
            return redirect(url_for('mainMenu'))
        if request.form.get('research'):
            return redirect(url_for('researchMenu'))


        if request.form.get('techAssets'):
            displayFlag = tech

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('techMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft))



@app.route('/researchMenu', methods=['GET', 'POST'])
def researchMenu():
    year,month = getParms('year')
    myNation = getParms('myNation')
    playerTech = techAssets.query.filter_by(active=1, country=myNation.country).first()
    movesToCheck = checkMoves(myNation,'&^')
    movesLeft = movesToCheck[0]
    message = ""
    displayFlag = ""
    infoFlag = ""

    
    if request.method == 'POST':
        if request.form.get('advance'):
            advanceResult = advanceEra(playerTech,myNation,db)
            message = advanceResult[1]

        if request.form.get('develop'):
            # Works the best
            movesToCheck = checkMoves(myNation,'research')
            movesLeft = movesToCheck[0]
            if movesToCheck[1] > 0:
                print('Ran out of moves')
                if movesToCheck[1] > 1:
                    print('Already carried this move out....')
                return redirect(url_for('mainMenu'))


            displayFlag = "tech"
            message = "Please pick a Technology to Research"

        if request.form.get('dev'):
            techResponse    = request.form.get('dev')
            techChoice     = str(techResponse).split(',')[0]
            techKey        = str(techResponse).split(',')[1]

            techRow        = techEraCost.query.filter_by(era=myNation.era).first()
            techCost       = getattr(techRow, techKey)
            pointsEarned   = getattr(playerTech, techKey)
            researchResult = researchTech(techChoice,techKey,techCost,pointsEarned,myNation,playerTech,db)
            message = researchResult[1]
            

        if request.form.get('grant'):
            # Works the best
            movesToCheck = checkMoves(myNation,'gainResearch')
            movesLeft = movesToCheck[0]
            if movesToCheck[1] > 0:
                print('Ran out of moves')
                if movesToCheck[1] > 1:
                    print('Already carried this move out....')
                return redirect(url_for('mainMenu'))

            displayFlag = "grant"
            message = 'Please select a degree of commitment.'
        if request.form.get('intensity'):
            intensity = request.form.get('intensity')
            if intensity == 'info':
                displayFlag = "grant"
                infoFlag = 'info'

            grantsResponse = researchGrant(myNation,intensity,db)
            message = grantsResponse[1]

        if request.form.get('purchase'):
             return redirect(url_for('mainMenu'))

        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('researchMenu.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,playerTech=playerTech,message=message,displayFlag=displayFlag,infoFlag=infoFlag))





#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#                   END   TECH
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




#---------------------------------------------------------
#                      NEXT YEAR
#---------------------------------------------------------

@app.route('/nextYear', methods=['GET', 'POST'])
def nextYear():
    year,month = getParms('year')
    myNation = getParms('myNation')
    playerTech = techAssets.query.filter_by(active=1, country=myNation.country).first()
    DIALOGUE       = db.session.query(dialogue).all()
    # Works the best
    movesToCheck = checkMoves(myNation,'^&')
    movesLeft = movesToCheck[0]

    message = ""
    displayFlag = ""
    infoFlag = ""

    
    if request.method == 'POST':
        if request.form.get('playerUpdates'):
            displayFlag = "playerUpdates"
        if request.form.get('AIUpdates'):
            displayFlag = "AIUpdates"
        if request.form.get('allUpdates'):
            displayFlag = "allUpdates"


        if request.form.get('mainMenu'):
            return redirect(url_for('mainMenu'))

    return(render_template('nextYear.html',year=year,month=month,myNation=myNation,movesLeft=movesLeft,playerTech=playerTech,message=message,displayFlag=displayFlag,infoFlag=infoFlag,DIALOGUE=DIALOGUE))


