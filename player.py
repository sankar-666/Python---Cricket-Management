from flask import *
from database import *

player=Blueprint('player',__name__)

@player.route('/playerhome')
def playerhome():
    return render_template('playerhome.html')