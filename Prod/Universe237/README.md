# OverView

# High Level   

Env folder is for virtual env for pip package management stuff.   
Requirements file is overkill, the only two things needing installed is `flask` and `flasksqlalchemy` both via pip.  


Entry point is by running `python app.py`  which picks up the init module and kicks that off, which does some setup of DB and server shizz.  

Routes is the overall coordinator program - everything is managed there.  

The way it works is the first line denotes the route second the function called by the root.   

```Python
@app.route('/start', methods=['GET', 'POST'])
def index():

```

 So far I have been unsuccessful in breaking the routes module into smaller modules hence why its so big.   



 