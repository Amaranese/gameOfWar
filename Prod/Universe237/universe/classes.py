from universe import db
import random 


class NATIONS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country               = db.Column(db.String(50), nullable=False)
    selected              = db.Column(db.Integer, nullable=False, default=0)
    score                 = db.Column(db.Integer, nullable=False, default=0)
    
    wealth                = db.Column(db.Integer, nullable=False)
    fLevel                = db.Column(db.String(50), nullable=False)
    gold                  = db.Column(db.Integer, nullable=False)
    gems                  = db.Column(db.Integer, nullable=False)
    rareMetals            = db.Column(db.Integer, nullable=False)
    oil                   = db.Column(db.Integer, nullable=False)

    might                 = db.Column(db.Integer, nullable=False)
    wLevel                = db.Column(db.String(50), nullable=False)
    firePower             = db.Column(db.Integer, nullable=False)

    KP                    = db.Column(db.Integer, nullable=False)
    tLevel                = db.Column(db.Integer, nullable=False)
    era                   = db.Column(db.String(50), nullable=False)
    RP                    = db.Column(db.Integer, nullable=False)

    influence             = db.Column(db.Integer, nullable=False)
    pLevel                = db.Column(db.String(50), nullable=False)
    stability             = db.Column(db.Integer, nullable=False)
    backing               = db.Column(db.Integer, nullable=False)

    chance                = db.Column(db.Integer, nullable=False)
    aggression            = db.Column(db.Integer, nullable=False)
    creativity            = db.Column(db.Integer, nullable=False)
    materialism           = db.Column(db.Integer, nullable=False)
    prudence              = db.Column(db.Integer, nullable=False)
    bonusUnits            = db.Column(db.Integer, nullable=False)
    notes                 = db.Column(db.String(50), nullable=False)

    hints                 = db.Column(db.String(50), nullable=False)
    Nextmoves             = db.Column(db.String(50), nullable=False, default='')
    moveLimit             = db.Column(db.Integer, nullable=False) 


    def __repr__(self):
       return f"ID:{self.id} \n Country: {self.country} \n Selected?: {self.selected} \n Score: {self.score} \n Wealth: {self.wealth} \n Finance: {self.fLevel} \n Gold: {self.gold} \n Gems: {self.gems} \n RareMetals: {self.rareMetals} \n Oil: {self.oil} \n Might: {self.might} \n wLevel: {self.wLevel}\n Firepower: {self.firePower} \n KP:{self.KP} \n  tLevel:{self.tLevel} \n  era:{self.era} \n  RP:{self.RP} \n influence:{self.influence} \n pLevel:{self.pLevel} \n stability:{self.stability} \n backing:{self.backing} \n chance:{self.chance} \n moveLimit:{self.moveLimit} \n aggression:{self.aggression} \n creativity:{self.creativity} \n materialism:{self.materialism} \n prudence:{self.prudence} \n bonusUnits:{self.bonusUnits} \n notes:{self.notes} \n hints:{self.hints} \n Nextmoves:{self.Nextmoves} \n"

class gameTracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    countryID             = db.Column(db.Integer, nullable=False,default = 1)
    country               = db.Column(db.String(50), nullable=False, default = "USA")
    started               = db.Column(db.Integer, nullable=False,default = 0)
    year                  = db.Column(db.Integer, nullable=False,default = 1949)
    month                 = db.Column(db.Integer, nullable=False,default = 1)

    # Only need once 
    eraOneAverageRP       = db.Column(db.Integer, nullable=False,default = 1)
    eraTwoAverageRP       = db.Column(db.Integer, nullable=False,default = 1)
    eraThreeAverageRP     = db.Column(db.Integer, nullable=False,default = 1) 

    def __repr__(self):
        return f"countryID:{self.countryID} \n country:{self.country} \n  started:{self.started} \n  year:{self.year} \n month:{self.month} \n  eraOneAverageRP:{self.eraOneAverageRP} \n  eraTwoAverageRP:{self.eraTwoAverageRP} \n  eraThreeAverageRP:{self.eraThreeAverageRP} \n "

class dialogue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playerPrintLine            = db.Column(db.String(80))
    AIPrintLine                = db.Column(db.String(80))
    gamePrintLine              = db.Column(db.String(80))


class PTc(db.Model):
    # id column     
    id = db.Column(db.Integer, primary_key=True) 
    goldPrice       = db.Column(db.Integer, nullable=False)
    gold            = db.Column(db.Integer, nullable=False)
    goldPriceChange = db.Column(db.String(50), nullable=False)
    goldHistory     = db.Column(db.String(100), nullable=False)
    goldAverage     = db.Column(db.Integer, nullable=False)

    rareMetalsPrice         = db.Column(db.Integer, nullable=False)
    rareMetals              = db.Column(db.Integer, nullable=False)
    rareMetalsPriceChange   = db.Column(db.String(50), nullable=False)
    rareMetalsHistory       = db.Column(db.String(100), nullable=False)
    rareMetalsAverage       = db.Column(db.Integer, nullable=False)

    gemsPrice         = db.Column(db.Integer, nullable=False)
    gems              = db.Column(db.Integer, nullable=False)
    gemsPriceChange   = db.Column(db.String(50), nullable=False)
    gemsHistory       = db.Column(db.String(100), nullable=False)
    gemsAverage       = db.Column(db.Integer, nullable=False)

    oilPrice         = db.Column(db.Integer, nullable=False)
    oil              = db.Column(db.Integer, nullable=False)
    oilPriceChange   = db.Column(db.String(50), nullable=False)
    oilHistory       = db.Column(db.String(100), nullable=False)
    oilAverage       = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f" goldPrice: {self.goldPrice} \n gold: {self.gold} \n goldPriceChange: {self.goldPriceChange} \n goldHistory: {self.goldHistory} \n goldAverage: {self.goldAverage} \n rareMetalsPrice: {self.rareMetalsPrice} \n rareMetals: {self.rareMetals} \n rareMetalsPriceChange: {self.rareMetalsPriceChange} \n rareMetalsHistory: {self.rareMetalsHistory} \n rareMetalsAverage: {self.rareMetalsAverage} \n gemsPrice: {self.gemsPrice} \n gems: {self.gems} \n gemsPriceChange: {self.gemsPriceChange} \n gemsHistory: {self.gemsHistory} \n gemsAverage: {self.gemsAverage} \n oilPrice: {self.oilPrice} \n oil: {self.oil} \n oilPriceChange: {self.oilPriceChange} \n oilHistory: {self.oilHistory} \n oilAverage: {self.oilAverage} \n "



class PTcHistory(db.Model):
    # id column     
    id = db.Column(db.Integer, primary_key=True) 
    goldPrice       = db.Column(db.Integer, nullable=False)
    gold            = db.Column(db.Integer, nullable=False)
    goldPriceChange = db.Column(db.String(50), nullable=False)
    goldHistory     = db.Column(db.String(100), nullable=False)
    goldAverage     = db.Column(db.Integer, nullable=False)

    rareMetalsPrice         = db.Column(db.Integer, nullable=False)
    rareMetals      = db.Column(db.Integer, nullable=False)
    rareMetalsPriceChange   = db.Column(db.String(50), nullable=False)
    rareMetalsHistory       = db.Column(db.String(100), nullable=False)
    rareMetalsAverage       = db.Column(db.Integer, nullable=False)

    gemsPrice         = db.Column(db.Integer, nullable=False)
    gems              = db.Column(db.Integer, nullable=False)
    gemsPriceChange   = db.Column(db.String(50), nullable=False)
    gemsHistory       = db.Column(db.String(100), nullable=False)
    gemsAverage       = db.Column(db.Integer, nullable=False)

    oilPrice         = db.Column(db.Integer, nullable=False)
    oil              = db.Column(db.Integer, nullable=False)
    oilPriceChange   = db.Column(db.String(50), nullable=False)
    oilHistory       = db.Column(db.String(100), nullable=False)
    oilAverage       = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f" goldPrice: {self.goldPrice} \n gold: {self.gold} \n goldPriceChange: {self.goldPriceChange} \n goldHistory: {self.goldHistory} \n goldAverage: {self.goldAverage} \n rareMetalsPrice: {self.rareMetalsPrice} \n rareMetals: {self.rareMetals} \n rareMetalsPriceChange: {self.rareMetalsPriceChange} \n rareMetalsHistory: {self.rareMetalsHistory} \n rareMetalsAverage: {self.rareMetalsAverage} \n gemsPrice: {self.gemsPrice} \n gems: {self.gems} \n gemsPriceChange: {self.gemsPriceChange} \n gemsHistory: {self.gemsHistory} \n gemsAverage: {self.gemsAverage} \n oilPrice: {self.oilPrice} \n oil: {self.oil} \n oilPriceChange: {self.oilPriceChange} \n oilHistory: {self.oilHistory} \n oilAverage: {self.oilAverage} \n "


class warDataBase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era                   = db.Column(db.String(50), nullable=False)
    unit_key              = db.Column(db.Integer, nullable=False)
    unit_name             = db.Column(db.String(50), nullable=False)
    power                 = db.Column(db.Integer, nullable=False)
    price                 = db.Column(db.Integer, nullable=False)
    buildTime             = db.Column(db.Integer, nullable=False)
    mightBonus            = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f" Era: {self.era} \n unit_key: {self.unit_key} \n unit_name: {self.unit_name} \n power: {self.power} \n price: {self.price} \n buildTime: {self.buildTime} \n mightBonus: {self.mightBonus} \n "

# Each Country to have 4 or 5 rows for each era
class warAssets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country             = db.Column(db.String(50), nullable=False)
    era                 = db.Column(db.String(50), nullable=False)
    active              = db.Column(db.Integer, nullable=False, default=0)
    wOne                = db.Column(db.String(50), nullable=False)
    wOneAmount          = db.Column(db.Integer, nullable=False)
    wOneLevel           = db.Column(db.Integer, nullable=False)
    wOnePower          = db.Column(db.Integer, nullable=False)

    wTwo                = db.Column(db.String(50), nullable=False)
    wTwoAmount          = db.Column(db.Integer, nullable=False)
    wTwoLevel           = db.Column(db.Integer, nullable=False)
    wTwoPower          = db.Column(db.Integer, nullable=False)
    
    wThree              = db.Column(db.String(50), nullable=False)
    wThreeAmount        = db.Column(db.Integer, nullable=False)
    wThreeLevel         = db.Column(db.Integer, nullable=False)
    wThreePower        = db.Column(db.Integer, nullable=False)

    wFour               = db.Column(db.String(50), nullable=False)
    wFourAmount         = db.Column(db.Integer, nullable=False)
    wFourLevel          = db.Column(db.Integer, nullable=False)
    wFourPower         = db.Column(db.Integer, nullable=False)

    wFive                = db.Column(db.String(50), nullable=False)
    wFiveAmount          = db.Column(db.Integer, nullable=False)
    wFiveLevel           = db.Column(db.Integer, nullable=False)
    wFivePower          = db.Column(db.Integer, nullable=False)

    wSix                 = db.Column(db.String(50), nullable=False)
    wSixAmount           = db.Column(db.Integer, nullable=False)
    wSixLevel            = db.Column(db.Integer, nullable=False)
    wSixPower           = db.Column(db.Integer, nullable=False)

    wSeven               = db.Column(db.String(50), nullable=False)
    wSevenAmount         = db.Column(db.Integer, nullable=False)
    wSevenLevel          = db.Column(db.Integer, nullable=False)
    wSevenPower         = db.Column(db.Integer, nullable=False)

    wEight               = db.Column(db.String(50), nullable=False)
    wEightAmount         = db.Column(db.Integer, nullable=False)
    wEightLevel          = db.Column(db.Integer, nullable=False)
    wEightPower         = db.Column(db.Integer, nullable=False)

    def __repr__(self):
       return f"ID:{self.id} \n Country: {self.country} \n  era: {self.era} \n active: {self.active} \n wOne: {self.wOne}  {self.wOneAmount} {self.wOneLevel} {self.wOnePower}    \n wTwo: {self.wTwo} {self.wTwoAmount} {self.wTwoLevel} {self.wTwoPower} \n wThree: {self.wThree} {self.wThreeAmount} {self.wThreeLevel} {self.wThreePower}   \n wFour: {self.wFour} {self.wFourAmount} {self.wFourLevel} {self.wFourPower}\n wFive: {self.wFive} {self.wFiveAmount} {self.wFiveLevel} {self.wFivePower} \n wSix: {self.wSix} {self.wSixAmount} {self.wSixLevel}{self.wSixPower}  \n wSeven: {self.wSeven} {self.wSevenAmount} {self.wSevenLevel} {self.wSevenPower} \n wEight: {self.wEight} {self.wEightAmount} {self.wEightLevel} {self.wEightPower} \n"

# Each Country to have 4 or 5 rows for each era
class techAssets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country               = db.Column(db.String(50), nullable=False)
    era                   = db.Column(db.String(50), nullable=False)
    active                = db.Column(db.Integer, nullable=False, default=0)
    one                  = db.Column(db.String(50), nullable=False)
    oneRp                 = db.Column(db.Integer, nullable=False)
    oneP                 = db.Column(db.Integer, nullable=False)
    
    two                  = db.Column(db.String(50), nullable=False)
    twoRp                 = db.Column(db.Integer, nullable=False)
    twoP                 = db.Column(db.Integer, nullable=False)

    three                = db.Column(db.String(50), nullable=False)
    threeRp               = db.Column(db.Integer, nullable=False)
    threeP               = db.Column(db.Integer, nullable=False)

    four                 = db.Column(db.String(50), nullable=False)
    fourRp                = db.Column(db.Integer, nullable=False)
    fourP                = db.Column(db.Integer, nullable=False)

    five                 = db.Column(db.String(50), nullable=False)
    fiveRp                = db.Column(db.Integer, nullable=False)
    fiveP                = db.Column(db.Integer, nullable=False)

    def __repr__(self):
       return f"ID:{self.id} \n Country: {self.country} \n era: {self.era}  \n active: {self.active}  \nrOne:{self.one} C:{self.oneRp} P:{self.oneP} \n two:{self.two} C:{self.twoRp} P:{self.twoP} \n three:{self.three} C:{self.threeRp} P:{self.threeP} \n  four:{self.four} C:{self.fourRp} P:{self.fourP} \n  five:{self.five} C:{self.fiveRp} P:{self.fiveP} \n"


class techEras(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era                   = db.Column(db.String(50), nullable=False )
    nextEra               = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"era:{self.era} \n nextEra:{self.nextEra} \n"


class techEraBonus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era                   = db.Column(db.String(50), nullable=False )
    one                   = db.Column(db.String(50), nullable=False )
    two                   = db.Column(db.String(50), nullable=False)
    three                 = db.Column(db.String(50), nullable=False)
    four                  = db.Column(db.String(50), nullable=False)
    five                  = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"one:{self.one} \n two:{self.two} \n three:{self.three} \n four:{self.four} \n five:{self.five} \n  "

class techEraCost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era                    = db.Column(db.String(50), nullable=False )
    oneRp                  = db.Column(db.Integer, nullable=False)
    oneW                   = db.Column(db.Integer, nullable=False)
    twoRp                  = db.Column(db.Integer, nullable=False)
    twoW                   = db.Column(db.Integer, nullable=False)
    threeRp                = db.Column(db.Integer, nullable=False)
    threeW                 = db.Column(db.Integer, nullable=False)
    fourRp                 = db.Column(db.Integer, nullable=False)
    fourW                  = db.Column(db.Integer, nullable=False)
    fiveRp                 = db.Column(db.Integer, nullable=False)
    fiveW                  = db.Column(db.Integer, nullable=False)




                      
# A row for each country and their allied country
class friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country       = db.Column(db.String(50), nullable=False)
    targetCountry = db.Column(db.String(50), nullable=False)
    level         = db.Column(db.Integer, nullable=False)
    warDate       = db.Column(db.String(50), nullable=False)
    initiated     = db.Column(db.Integer, nullable=False)
    numWars       = db.Column(db.Integer, nullable=False)
    declared      = db.Column(db.String(50), nullable=False)
    attacked      = db.Column(db.String(50), nullable=False)
    lost          = db.Column(db.Integer, nullable=False)
    won           = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"country:{self.country} \n targetCountry:{self.targetCountry} \n level:{self.level} \n warDate:{self.warDate} \n initiated:{self.initiated} \n numWars  :{self.numWars} \n declared:{self.declared} \n attacked:{self.attacked}  \n lost:{self.lost}  \n won:{self.won} "



# Update average values only once 
def initializeRPAverages(db):
    myNation = db.session.query(gameTracker).filter_by(id=1).first()
    eraone = techEraCost.query.filter_by(era='INDUSTRIAL REVOLUTION').first()
    sumEraone = int(eraone.oneRp) + int(eraone.twoRp) + int(eraone.threeRp) + int(eraone.fourRp) + int(eraone.fiveRp) 
    eraOneAverage = sumEraone/5
    myNation.eraOneAverageRP = eraOneAverage
    db.session.commit()

    eratwo = techEraCost.query.filter_by(era='INFORMATION AGE').first()
    sumEraTwo = int(eratwo.oneRp) + int(eratwo.twoRp) + int(eratwo.threeRp) + int(eratwo.fourRp) + int(eratwo.fiveRp) 
    eraTwoAverage = sumEraTwo/5
    myNation.eraTwoAverageRP = eraTwoAverage
    db.session.commit()

    erathree = techEraCost.query.filter_by(era='SECOND ENLIGHTENMENT').first()
    sumEraThree = int(erathree.oneRp) + int(erathree.twoRp) + int(erathree.threeRp) + int(erathree.fourRp) + int(erathree.fiveRp) 
    eraThreeAverage = sumEraThree/5
    myNation.eraThreeAverageRP = eraThreeAverage
    db.session.commit()



def initializeObjects(db):
    #SETUP PRICETRACKER
    pT = PTc(goldPrice =120, gold=10000, goldPriceChange='+0', goldHistory='120', goldAverage=120,rareMetalsPrice= 60, rareMetals= 2000, rareMetalsPriceChange= '+0', rareMetalsHistory='60',rareMetalsAverage=60,gemsPrice= 250, gems= 2000, gemsPriceChange= '+0', gemsHistory='250',gemsAverage=250, oilPrice= 12, oil= 10000, oilPriceChange= '+0', oilHistory='12',oilAverage=12)
    db.session.add(pT)
    db.session.commit()

    # REFERENCE ONLY
    WAR_BRIEFING = {'weapons':{
        
        'INDUSTRIAL REVOLUTION':{'1':['Conscripts',1,10,2,0.01],     '2':['Cavalry',2,300,2,0.1],       '3':['Cannon Specialists',10,100,2,0.005],'4':['Special-Ops',15,2000,3,0.1],    '5':['MiniSubs',25,20000,4,1],   '6':['Steam Warships',150,5000,2,0.3],'7':['Iron-clad Battleships',300,7000,3,0.35],'8':['Airships',350,100000,4,5]},
        'INFORMATION AGE':      {'1':['Fiflemen',8,10,2,0.01],       '2':['Tanks',5,300,2,0.1],         '3':['Gunboats',20,100,2,0.005],          '4':['Destroyers',50,2000,3,0.1],     '5':['Jets',40,20000,4,1],   '6':['Bombers',200,5000,2,0.3],          '7':['carriers',350,7000,3,0.35],              '8':['Nukes',500,100000,4,5]},
        'SECOND ENLIGHTENMENT': {'1':['Laser Infantry',20,10,2,0.01],'2':['Mech Troopers',10,300,2,0.1],'3':['Naval Swarm',40,100,2,0.005],       '4':['Hybrid Fighters',80,2000,3,0.1],'5':['EMP Drones',100,20000,4,1],'6':['Heavy Bomber Drone',250,5000,2,0.3], '7':['Giga swarm',400,7000,3,0.35],            '8':['Orbital Strike',999,100000,4,5]}
    } 
    }
    # Each Era to have eight only

    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=1 , unit_name='Conscripts'            , power=1 ,price=10 ,buildTime=1 ,mightBonus=0.01)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=2 , unit_name='Cavalry'               , power=2 ,price=50 ,buildTime=2 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=3 , unit_name='Cannon Specialists'    , power=5 ,price=100 ,buildTime=2 ,mightBonus=0.05)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=4 , unit_name='Special-Ops'           , power=10 ,price=500 ,buildTime=3 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=5 , unit_name='MiniSubs'              , power=20 ,price=2000 ,buildTime=3 ,mightBonus=0.2)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=6 , unit_name='Steam Warships'        , power=30 ,price=3000 ,buildTime=3 ,mightBonus=0.3)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=7 , unit_name='Iron-clad Battleships' , power=40 ,price=5000 ,buildTime=4 ,mightBonus=0.4)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INDUSTRIAL REVOLUTION' , unit_key=8 , unit_name='Airships'              , power=100 ,price=10000 ,buildTime=5 ,mightBonus=0.5)
    db.session.add(WAR_ROW)

    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=1 , unit_name='Fiflemen'   , power=80 ,price=4500 ,buildTime=1 ,mightBonus=0.01)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=2 , unit_name='Tanks'      , power=90 ,price=7000 ,buildTime=1 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=3 , unit_name='Gunboats'   , power=100 ,price=10000 ,buildTime=2 ,mightBonus=0.05)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=4 , unit_name='Destroyers' , power=200 ,price=15000 ,buildTime=2 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=5 , unit_name='Jets'       , power=400 ,price=18000 ,buildTime=3 ,mightBonus=0.2)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=6 , unit_name='Bombers'    , power=600 ,price=25000 ,buildTime=3 ,mightBonus=0.3)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=7 , unit_name='carriers'   , power=800 ,price=35000 ,buildTime=4 ,mightBonus=0.4)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='INFORMATION AGE' , unit_key=8 , unit_name='Nukes'     , power=1000 ,price=100000 ,buildTime=5 ,mightBonus=0.5)
    db.session.add(WAR_ROW)
    
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=1 , unit_name='Laser Infantry'     , power=700 ,price=40000 ,buildTime=1 ,mightBonus=0.01)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=2 , unit_name='Mech Troopers'      , power=800 ,price=50000 ,buildTime=1 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=3 , unit_name='Naval Swarm'        , power=1000 ,price=80000 ,buildTime=2 ,mightBonus=0.05)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=4 , unit_name='Hybrid Fighters'    , power=1200 ,price=100000 ,buildTime=2 ,mightBonus=0.1)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=5 , unit_name='EMP Drones'         , power=1500 ,price=120000 ,buildTime=3 ,mightBonus=0.2)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=6 , unit_name='Heavy Bomber Drone' , power=2000 ,price=150000 ,buildTime=3 ,mightBonus=0.3)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=7 , unit_name='Giga Swarm'         , power=3000 ,price=180000 ,buildTime=4 ,mightBonus=0.4)
    db.session.add(WAR_ROW)
    WAR_ROW = warDataBase(era='SECOND ENLIGHTENMENT' , unit_key=8 , unit_name='Orbital Strike'     , power=5000 ,price=200000 ,buildTime=5 ,mightBonus=0.5)
    db.session.add(WAR_ROW)
    db.session.commit()
 
    TECH_ROW = techEras(era='INDUSTRIAL REVOLUTION',nextEra='INFORMATION AGE')
    db.session.add(TECH_ROW)
    db.session.commit()
    TECH_ROW = techEras(era='INFORMATION AGE',nextEra='SECOND ENLIGHTENMENT')
    db.session.add(TECH_ROW)
    db.session.commit()
    TECH_ROW = techEras(era='SECOND ENLIGHTENMENT',nextEra='SPACE AGE')
    db.session.add(TECH_ROW)
    db.session.commit()
    TECH_ROW = techEras(era='SPACE AGE',nextEra='THE ASCENDANCE')
    db.session.add(TECH_ROW)
    db.session.commit()

    era = 'INDUSTRIAL REVOLUTION'

    techRow = techEraBonus(era='INDUSTRIAL REVOLUTION', one='K,100',two='W,400:K,300',three='W,500:K,500:R,500',four='W,800:K,1000:R,400',five='W,1000:K,2000:R,500')
    db.session.add(techRow)
    techRow = techEraBonus(era='INFORMATION AGE', one='K,2000',two='W,4000:K,3000',three='W,5000:K,5000:R,2000',four='W,8000:K,10000:R,4000',five='W,10000:K,20000:R,5000')
    db.session.add(techRow)
    techRow = techEraBonus(era= 'SECOND ENLIGHTENMENT', one='K,10000',two='1,40000:K,30000',three='W,500000,K,500000:R,20000',four='W,80000:K,100000:R,40000',five='W,100000:K,200000:R,50000')
    db.session.add(techRow)
    db.session.commit()


    techRow = techEraCost(era='INDUSTRIAL REVOLUTION', oneRp=50 ,   oneW=0 ,   twoRp=100 ,   twoW=100 ,threeRp=200 ,  threeW=100 ,fourRp=400 , fourW=100 ,fiveRp=600 ,fiveW=100 )
    db.session.add(techRow)
    techRow = techEraCost(era='INFORMATION AGE' ,      oneRp=600 ,  oneW=100 , twoRp=1000 ,  twoW=100 ,threeRp=2000 , threeW=100 ,fourRp=4000 , fourW=100 ,fiveRp=6000 ,fiveW=100 )
    db.session.add(techRow)
    techRow = techEraCost(era='SECOND ENLIGHTENMENT' , oneRp=6000 , oneW=100 , twoRp=10000 , twoW=100 ,threeRp=12000 ,threeW=100 ,fourRp=14000 , fourW=100 ,fiveRp=16000 ,fiveW=100 )
    db.session.add(techRow)
    db.session.commit()



    NATION_ARRAY = ['USA','UK','GERMANY','CHINA','INDIA','RUSSIA','ITALY','SPAIN','FRANCE','JAPAN',
    'BRAZIL','SOUTHKOREA','SOUTHAFRICA','PAKISTAN','INDONESIA','NIGERIA','MEXICO','EGYPT','VIETNAM','IRAN','KENYA']
    score        = 100
    wealth       = 500 
    gems         = 5
    rareMetals   = 0
    oil          = 0
    might        = 100  
    troops       = 500
    aggression   = 0 


    # INITIALIZE TABLES
    for item in NATION_ARRAY:
        NATION_ROW = NATIONS(country=item,wealth=wealth, fLevel='PickPocket', gold=60,gems=gems,rareMetals=rareMetals,oil=oil,might=might,wLevel='Private', firePower=0, KP=0,tLevel=0,era=era,RP=300, influence=1,pLevel=0,stability=0,backing=0,chance=0,moveLimit=2,aggression=random.randint(0,100),creativity=random.randint(0,100),materialism=random.randint(0,100),prudence=random.randint(0,100),bonusUnits="",notes="",hints="",)
        db.session.add(NATION_ROW)
        db.session.commit()

        warIRRow = warAssets(country=item,era='INDUSTRIAL REVOLUTION',  active=1, wOne='Conscripts',wOneAmount=troops,wOneLevel=1,wOnePower=0,wTwo= 'Cavalry', wTwoAmount = 0, wTwoLevel= 1,wTwoPower= 0,wThree = 'Cannon Specialists',wThreeAmount = 0,wThreeLevel = 1,wThreePower = 0, wFour = 'Special-Ops',wFourAmount = 0,wFourLevel = 1,wFourPower = 0,wFive = 'MiniSubs', wFiveAmount = 0, wFiveLevel = 1, wFivePower = 0,wSix = 'Steam Warships', wSixAmount = 0, wSixLevel = 1, wSixPower = 0,wSeven = 'Iron-clad Battleships', wSevenAmount = 0, wSevenLevel = 1, wSevenPower = 0,wEight = 'Airships', wEightAmount = 0, wEightLevel = 1, wEightPower = 0)
        warIARow = warAssets(country=item,era='INFORMATION AGE',        active=0, wOne='Fiflemen',wOneAmount=0,wOneLevel=1,wOnePower=0,wTwo= 'Tanks', wTwoAmount = 0, wTwoLevel= 1,wTwoPower= 0,wThree = 'Gunboats',wThreeAmount = 0,wThreeLevel = 1,wThreePower = 0, wFour = 'Destroyers',wFourAmount = 0,wFourLevel = 1,wFourPower = 0,wFive = 'Jets', wFiveAmount = 0, wFiveLevel = 1, wFivePower = 0,wSix = 'Bombers', wSixAmount = 0, wSixLevel = 1, wSixPower = 0,wSeven = 'carriers', wSevenAmount = 0, wSevenLevel = 1, wSevenPower = 0,wEight = 'Nukes', wEightAmount = 0, wEightLevel = 1, wEightPower = 0)
        warSARow = warAssets(country=item,era='SECOND ENLIGHTENMENT' ,  active=0, wOne='Laser Infantry',wOneAmount=0,wOneLevel=1,wOnePower=0,wTwo= 'Mech Troopers', wTwoAmount = 0, wTwoLevel= 1,wTwoPower= 0,wThree = 'Naval Swarm',wThreeAmount = 0,wThreeLevel = 1,wThreePower = 0, wFour = 'Hybrid Fighters',wFourAmount = 0,wFourLevel = 1,wFourPower = 0,wFive = 'EMP Drones', wFiveAmount = 0, wFiveLevel = 1, wFivePower = 0,wSix = 'Heavy Bomber Drone', wSixAmount = 0, wSixLevel = 1, wSixPower = 0,wSeven = 'Giga Swarm', wSevenAmount = 0, wSevenLevel = 1, wSevenPower = 0,wEight = 'Orbital Strike', wEightAmount = 0, wEightLevel = 1, wEightPower = 0)
        db.session.add(warIRRow)
        db.session.add(warIARow)
        db.session.add(warSARow)
        db.session.commit()

        techIRRow = techAssets(country = item, era = 'INDUSTRIAL REVOLUTION', active=1, one = 'Wool', oneRp = 0, oneP = 0,two = 'Manufacturing Line', twoRp = 0, twoP = 0,three = 'Glass Production', threeRp = 0, threeP = 0,four = 'Cement', fourRp = 0, fourP = 0, five = 'Electricity', fiveRp = 0, fiveP = 0)
        techIARow = techAssets(country = item, era = 'INFORMATION AGE'      , active=0, one = 'Digital Electronics', oneRp = 0, oneP = 0,two = 'Internet', twoRp = 0, twoP = 0,three = 'Mobile Technologies', threeRp = 0, threeP = 0,four = 'Cloud Computing', fourRp = 0, fourP = 0, five = 'Internet of Things', fiveRp = 0, fiveP = 0)
        techSRRow = techAssets(country = item, era = 'SECOND ENLIGHTENMENT' , active=0, one = 'Decentralisation', oneRp = 0, oneP = 0,two = 'NeuralLink', twoRp = 0, twoP = 0,three = 'Artificial Intelligence', threeRp = 0, threeP = 0,four = 'Bio Computing', fourRp = 0, fourP = 0, five = 'The Convergance', fiveRp = 0, fiveP = 0)   
        db.session.add(techIRRow)
        db.session.add(techIARow)
        db.session.add(techSRRow)
        db.session.commit()  


        for nation in NATION_ARRAY:
            friendshipLevel = random.randint(-10,50)
            if nation != item:
                FRIENDSHIP_ROW = friendship(country=item, targetCountry=nation, level=friendshipLevel, warDate='', initiated=0, numWars=0, declared='', attacked='', lost=0, won=0)
                db.session.add(FRIENDSHIP_ROW)
                db.session.commit()

        score      = score - 5
        wealth     = wealth - 5
        gems       = gems + 5
        rareMetals = rareMetals + 5
        oil        = oil + 5
        might      = might - 3
        troops     = troops -1


def printDialogue(printType,text,db):
    if printType == "player":
        out = dialogue(playerPrintLine = text)
        db.session.add(out)
        db.session.commit()
    elif printType == "AI":
        out = dialogue(AIPrintLine = text)
        db.session.add(out)
        db.session.commit()
    elif printType == "all":
        out = dialogue(gamePrintLine = text)
        db.session.add(out)
        db.session.commit()
    else:
        out = dialogue(playerPrintLine = text)
        db.session.add(out)
        db.session.commit()
    return(text)
