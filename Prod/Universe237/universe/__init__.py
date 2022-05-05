from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conquest.db'
db = SQLAlchemy(app)

from universe.classes import PTc,warDataBase,NATIONS,friendship,warAssets,techAssets,gameTracker,initializeObjects,techEras,techEraBonus,initializeRPAverages

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


from universe import routes