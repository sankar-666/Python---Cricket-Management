from flask import *
from database import *

player=Blueprint('player',__name__)

@player.route('/playerhome')
def playerhome():
    data={}
    q="select * from player where player_id='%s'"%(session['pid'])
    data['res']=select(q)
    return render_template('playerhome.html',data=data)


@player.route('/player_view_match')
def player_view_match():
    data={}
    q="select * from team inner join matches where (matches.first_team_id=team.team_id) or (matches.second_team_id=team.team_id) and team_id in (select player_id from player where player_id='%s')"%(session['pid'])
    data['res']=select(q)
    return render_template('player_view_match.html',data=data)



@player.route('/player_view_updates')
def player_view_updates():
    data={}
    q="select * from player_updates where player_id='%s'"%(session['pid'])
    data['res']=select(q)
    return render_template('player_view_updates.html',data=data)


@player.route('/player_view_message')
def player_view_message():
    data={}
    uid=session['loginid']
    q="SELECT * FROM `user` WHERE login_id IN (SELECT IF(sender_id = '%s',receiver_id,sender_id) FROM chat WHERE sender_id='%s' OR receiver_id='%s')"%(uid,uid,uid)
    print(q)
    res=select(q)
    data['res']=res
    return render_template('player_view_message.html',data=data)


@player.route('/player_chat')
def player_chat():
    data={}
    uid=session['loginid']
    did=request.args['did']
    if 'btn' in request.form:
        name=request.form['txt']
    
        q="insert into chat values(NULL,'%s','%s','%s',now())"%(uid,did,name)
        insert(q)
        return redirect(url_for("doctor.doctorchat",did=did))
    q="SELECT * FROM chat WHERE (sender_id='%s' AND receiver_id='%s') OR (sender_id='%s' AND receiver_id=('%s')) order by chat_id"%(uid,did,did,uid)
    # q="select * from chats where senderid='%s' and receiverid=( select login_id from doctors where doctor_id='%s' )"%(uid,did)
    print(q)
    res=select(q)
    data['ress']=res
    return render_template('player_chat.html',data=data)
