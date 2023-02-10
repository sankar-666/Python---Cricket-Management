from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')



@admin.route('/admin_view_teamsregisterd')
def admin_view_teamsregisterd():
    data={}
    q="select * from team"
    data['res']=select(q)
    return render_template('admin_view_teamsregisterd.html',data=data)


@admin.route('/admin_view_players')
def admin_view_players():
    tid=request.args['tid']
    data={}
    q="select * from player where team_id='%s'"%(tid)
    data['res']=select(q)
    return render_template('admin_view_players.html',data=data)


@admin.route('/admin_view_users')
def admin_view_users():
    data={}
    q="select * from user"
    data['res']=select(q)
    
    return render_template('admin_view_users.html',data=data)
admin_manage_tournaments