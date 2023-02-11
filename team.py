from flask import *
from database import *

team=Blueprint('team',__name__)

@team.route('/teamhome')
def teamhome():
    return render_template('teamhome.html')

import uuid

@team.route('/team_manage_player',methods=['get','post'])
def team_manage_player():
    data={}
    if 'btn' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        dob=request.form['dob']
        phone=request.form['phone']
        email=request.form['email']
        img=request.files['img']
        path="static/uploads/"+str(uuid.uuid4())+img.filename
        img.save(path)
        teamrole=request.form['teamrole']
        place=request.form['place']
        pin=request.form['pin']
        uname=request.form['uname']
        passw=request.form['passw']

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else: 
            q="insert into login values (null,'%s','%s','player')"%(uname,passw)
            lid=insert(q)
            q="insert into player values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,session['tid'],fname,lname,dob,phone,email,path,teamrole,place,pin)
            insert(q)
            flash("Successfully Added")
        return redirect(url_for("team.team_manage_player"))

    data={}
    q="select * from player"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        lid=request.args['lid'] 
        pid=request.args['pid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from player where player_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

    if 'update' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        dob=request.form['dob']
        phone=request.form['phone']
        email=request.form['email']
        teamrole=request.form['teamrole']
        place=request.form['place']
        pin=request.form['pin']
        if request.files['img']:
            img=request.files['img']
            path="static/uploads/"+str(uuid.uuid4())+img.filename
            img.save(path)
            q="update player set fname='%s', lname='%s', dob='%s', phone='%s', email='%s', photo='%s', team_role='%s', place='%s', pincode='%s' where player_id='%s' "%(fname,lname,dob,phone,email,path,teamrole,place,pin,pid)
        else:
            q="update player set fname='%s', lname='%s', dob='%s', phone='%s', email='%s',  team_role='%s', place='%s', pincode='%s' where player_id='%s' "%(fname,lname,dob,phone,email,teamrole,place,pin,pid)
        update(q)
        flash("Updated Successfully")
        return redirect(url_for("team.team_manage_player"))
    

    if action == "delete":
        q="delete from player where player_id='%s' "%(pid)
        delete(q)
        q="delete from login where login_id='%s' "%(lid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("team.team_manage_player"))
    return render_template('team_manage_player.html',data=data) 



@team.route('/team_player_status',methods=['get','post'])
def team_player_status():
    data={}
    player=request.args['player']
    pid=request.args['pid']
    if 'btn' in request.form:
        details=request.form['details']
      

     
        q="insert into player_updates values (null,'%s','%s',now())"%(pid,details)
        lid=insert(q)
        flash("Successfully Added")
        return redirect(url_for("team.team_player_status",pid=pid,player=player))

    data={}
    q="select *,concat(player.fname,'',player.lname) as playername from player_updates inner join player using (player_id) where player_id='%s'"%(pid)
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        uid=request.args['uid'] 
    else:
        action=None
    

    if action == "delete":
        q="delete from player_updates where update_id='%s' "%(uid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("team.team_player_status",pid=pid,player=player))
    return render_template('team_player_status.html',data=data,player=player) 


@team.route('/team_view_match')
def team_view_match():
    data={}
    q="select * from matches where first_team_id='%s' or second_team_id='%s'"%(session['tid'],session['tid'])
    # q="SELECT *,t1.team_name AS t1name,t2.team_name AS t2name FROM matches m ,team t1, team t2 WHERE m.first_team_id=t1.team_id AND m.second_team_id=t2.team_id first_team_id='%s' or second_team_id='%s'"%(session['tid'],session['tid'])
    data['res']=select(q)
    return render_template('team_view_match.html',data=data)


@team.route('/team_view_opponentteam')
def team_view_opponentteam():
    data={}
    q="select * from team where team_id in (select if(first_team_id='%s',second_team_id,first_team_id) from matches where first_team_id='%s' or second_team_id='%s')"%(session['tid'],session['tid'],session['tid'])
    data['res']=select(q)
    return render_template('team_view_opponentteam.html',data=data)


@team.route('/team_add_players_to_team',methods=['get','post'])
def team_add_players_to_team():
    data={}
    mid=request.args['mid']
    q="select * from player where team_id='%s'"%(session['tid'])
    print(q)
    data['player']=select(q)

    if 'btn' in request.form:
        player_id=request.form['player_id']
        q="select * from playing_eleven where player_id='%s'"%(player_id)
        val = select(q)
        if val:
            flash("This Player is Already Added!")
        else:
            q="insert into playing_eleven values(null,'%s','%s')"%(player_id,mid)
            insert(q)
            flash("Player Added")
        return redirect(url_for("team.team_add_players_to_team",mid=mid))
    
    q="SELECT * from playing_eleven inner join player using (player_id) where match_id='%s' "%(mid)
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        p11_id=request.args['p11_id'] 
    else:
        action=None

    
    if action == "delete":
        q="delete from playing_eleven where playing_id='%s' "%(p11_id)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("team.team_add_players_to_team",mid=mid))
    return render_template('team_add_players_to_team.html',data=data,mid=mid)
