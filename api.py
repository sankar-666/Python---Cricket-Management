from flask import *
from database import *

api=Blueprint('api',__name__)



@api.route('/login')
def login():
    data={}
    un=request.args['username']
    pwd=request.args['password']
    z="select * from `login` where username='%s' and password='%s' "%(un,pwd)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    return str(data)


@api.route("/reg",methods=['get','post'])
def reg():
    data={}

    fname=request.args['fname']
    lname=request.args['lname']
    place=request.args['place']
    phone=request.args['phone']
    email=request.args['email']
    username=request.args['uname']
    password=request.args['pass']
   

    q="select * from login where username='%s'"%(username)
    rep=select(q)

    if rep:
        data['status']='already'
    else:
        q="insert into `login` values(NULL,'%s','%s','user') "%(username,password)
        ref=insert(q)
        v="insert into `user` values(NULL,'%s','%s','%s','%s','%s','%s') "%(ref,fname,lname,phone,email,place)
        insert(v)
        data['status']='success'
    data['method']="reg"
    return str(data)


@api.route('/viewteams')
def viewteams():
    data={}

    z="select * from team"
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewteams'
    return str(data)


@api.route('/viewplayers')
def viewplayers():
    data={}
    tid=request.args['tid']
    z="select *,concat(fname,'',lname) as name from player where team_id='%s'"%(tid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewplayers'
    return str(data)


@api.route('/viewplayerupdates')
def viewplayerupdates():
    data={}
    pid=request.args['pid']
    z="select * from player_updates where player_id='%s'"%(pid)
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewplayerupdates'
    return str(data)


@api.route("/chatdetail")
def chatdetail():
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	
	data={}
	q="select * from chat where (sender_id='%s' and receiver_id='%s') or (sender_id='%s' and receiver_id='%s') group by chat_id "%(sid,rid,rid,sid)
	
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		
		data['status']="failed"
	data['method']='chatdetail'
	
	return str(data)

@api.route("/chat")
def chat():
	data={}
	sid=request.args['sender_id']
	rid=request.args['receiver_id']
	det=request.args['details']
	
	
	q="insert into chat values(null,'%s','%s','%s',curdate())"%(sid,rid,det)
	insert(q)
	data['status']='success'
	data['method']='chat'
	return str(data)


@api.route('/addrating')
def addrating():
    data={}
    lid=request.args['lid']
    pid=request.args['pid']
    rate=request.args['rating']
    q="select * from rating where user_id=(select user_id from user where login_id='%s') and player_id='%s'"%(lid,pid)
    res=select(q)
    if res:
        q="update rating set rated_point='%s' where user_id=(select user_id from user where login_id='%s') and player_id='%s'"%(rate,lid,pid)
        update(q)
    else:
        q="insert into rating values(null,(select user_id from user where login_id='%s'),'%s','%s')"%(lid,pid,rate)
        insert(q)

    data['status']="success"
    data['method']="addrating"
    return str(data)


@api.route('/viewrating')
def viewrating():
    data={}
    lid=request.args['lid']
    pid=request.args['pid']
    rating=""
    z="select * from rating where user_id=(select user_id from user where login_id='%s') and player_id='%s'"%(lid,pid)
    res=select(z)
    if res:
        rating=res[0]['rated_point']

    if res:
        data['status']='okey'
        data['data']=rating
    else:
        data['status']='failed'
    data['method']='viewrating'
    return str(data)


@api.route('/viewtour')
def viewtour():
    data={}
    z="SELECT * FROM `tournaments`"
    res=select(z)

    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewtour'
    return str(data)


@api.route('/viewmatches')
def viewmatches():
    data={}
    tid=request.args['tid']
    q="SELECT *,t1.team_name AS t1name,t2.team_name AS t2name FROM matches m ,team t1, team t2 WHERE m.first_team_id=t1.team_id AND m.second_team_id=t2.team_id  and tournament_id='%s'"%(tid)
    res=select(q)


    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewmatches'
    return str(data)


@api.route('/viewbowlingscore')
def viewbowlingscore():
    data={}
    mid=request.args['mid']
    q="SELECT *,concat(fname,'',lname) as playername from bowling inner join player using (player_id)  where match_id='%s' order by bowling_id DESC LIMIT 1"%(mid)
    res=select(q)


    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewbowlingscore'
    return str(data)


@api.route('/viewbattingscore')
def viewbattingscore():
    data={}
    mid=request.args['mid']
    q="SELECT *,concat(fname,'',lname) as playername from batting inner join player using (player_id)  where match_id='%s' order by batting_id DESC LIMIT 1"%(mid)
    res=select(q)


    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewbattingscore'
    return str(data)


@api.route('/viewextras')
def viewextras():
    data={}
    mid=request.args['mid']
    q="SELECT *,CONCAT(fname,'',lname) AS playername FROM extras INNER JOIN player ON `extras`.`bowler_id`=`player`.`player_id`  WHERE match_id='%s' ORDER BY extra_id"%(mid)
    # print(q)
    res=select(q)


    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewextras' 
    return str(data)

@api.route('/viewfinalscore')
def viewfinalscore():
    data={}
    # mid=request.args['mid']
    q="SELECT * from match_summary inner join team on match_summary.winner_team_id = team.team_id"
    # print(q)
    res=select(q)

    fscore = res[0]['first_team_score']
    sscore = res[0]['second_team_score']
    score=0
    wicket=0
    if fscore > sscore:
        score=fscore
        wicket=res[0]['first_team_wicket']
    else:
        score=sscore
        wicket=res[0]['second_team_wicket']
 
    if res:
        data['status']='success'
        data['data']=res
        data['score']=score
        data['wicket']=wicket
    else:
        data['status']='failed'
    data['method']='viewfinalscore' 
    return str(data)
