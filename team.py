from flask import *
from database import *

team=Blueprint('team',__name__)

@team.route('/teamhome')
def teamhome():
    return render_template('teamhome.html')