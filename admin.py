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




@admin.route('/admin_manage_tournaments',methods=['get','post'])
def admin_manage_tournaments():
    data={}
    if 'btn' in request.form:
        name=request.form['name']
        venue=request.form['venue']
        date=request.form['date']
        des=request.form['des']
       
        q="insert into tournaments values (null,'%s','%s','%s','%s')"%(name,venue,date,des)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_tournaments"))

    data={}
    q="select * from tournaments"
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        tid=request.args['tid'] 
    else:
        action=None

    
    if action == "update":
        q="select * from tournaments where tournament_id='%s'"%(tid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            venue=request.form['venue']
            date=request.form['date']
            des=request.form['des']

            q="update tournaments set name='%s', venue='%s', date='%s', description='%s' where tournament_id='%s' "%(name,venue,date,des,tid)
            update(q)
            flash("Updated Successfully")
            return redirect(url_for("admin.admin_manage_tournaments"))
    if action == "delete":
        q="delete from tournaments where tournament_id='%s' "%(tid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_tournaments"))
    return render_template('admin_manage_tournaments.html',data=data) 



@admin.route('/admin_manage_matches',methods=['get','post'])
def admin_manage_matches():
    data={}
    tid=request.args['tid']

    q="select * from team"
    data['team']=select(q)
    if 'btn' in request.form:
        fid=request.form['fid']
        sid=request.form['sid']
        date=request.form['date']
        time=request.form['time']
       
        q="insert into matches values (null,'%s','%s','%s','%s','%s','pending')"%(tid,fid,sid,date,time)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_manage_matches",tid=tid))

    q="SELECT *,t1.team_name AS t1name,t2.team_name AS t2name FROM matches m ,team t1, team t2 WHERE m.first_team_id=t1.team_id AND m.second_team_id=t2.team_id  and tournament_id='%s'"%(tid)
    print(q)
    data['res']=select(q)
    data['count']=len(select(q))

    if 'action' in request.args:
        action=request.args['action']
        mid=request.args['mid'] 
    else:
        action=None

    
    if action == "delete":
        q="delete from matches where matches_id='%s' "%(mid)
        delete(q)
        flash("Deleted Successfully")
        return redirect(url_for("admin.admin_manage_matches",tid=tid))
    return render_template('admin_manage_matches.html',data=data,tid=tid) 



@admin.route('/admin_view_rating')
def admin_view_rating():
    data={}
    q="SELECT *,CONCAT(user.fname,'',user.lname) AS username,CONCAT(player.fname,'',player.lname) AS player FROM `USER` INNER JOIN rating USING (user_id) INNER JOIN player USING (player_id)"
    data['res']=select(q)
    
    return render_template('admin_view_rating.html',data=data)



@admin.route('/admin_add_batting',methods=['get','post'])
def admin_add_batting():
    data={}
    mid=request.args['mid']

    q="select * from player "
    data['player']=select(q)
    
    if 'btn' in request.form:
        player_id=request.form['player_id']
        score=request.form['score']
        balls_faced=request.form['balls_faced']
        single=request.form['single']
        double=request.form['double']
        triple=request.form['triple']
        boundaries=request.form['boundaries']
        six=request.form['six']
        wicket_player=request.form['wicket_player']
        if wicket_player != 'Not Out':
            q="select * from batting where match_id='%s' and player_id='%s'"%(mid,player_id)
            res=select(q)
            if res:
                q="select * from batting where match_id='%s' and player_id='%s' and wicket_taken_by='Not Out'"%(mid,player_id)
                print(q)
                val=select(q)
                if val:
                    q="update batting set score='%s', balls_faced='%s', single='%s',`double`='%s', triple='%s', boundaries='%s', sixes='%s',wicket_taken_by='%s'  where match_id='%s' and player_id='%s'"%(score,balls_faced,single,double,triple,boundaries,six,wicket_player,mid,player_id)
                    update(q)
                    flash("Successfully Added")
                else:
                    flash("Cant Update Scores for Players whose wicket is Gone!")
            else: 
                q="insert into batting values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','Not Out')"%(mid,player_id,score,balls_faced,single,double,triple,boundaries,six)
                insert(q)
                flash("Successfully Added")
        else:

            
            q="select * from batting where match_id='%s' and player_id='%s'"%(mid,player_id)
            res2=select(q)
            if res2:
                q="update batting set score='%s', balls_faced='%s', single='%s',`double`='%s', triple='%s', boundaries='%s', sixes='%s' where match_id='%s' and player_id='%s'"%(score,balls_faced,single,double,triple,boundaries,six,mid,player_id)
                update(q)
                flash("Successfully Added")
            else:
                q="insert into batting values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','Not Out')"%(mid,player_id,score,balls_faced,single,double,triple,boundaries,six)
                insert(q)
                flash("Successfully Added")
            
        return redirect(url_for("admin.admin_add_batting",mid=mid))

    q="SELECT *,CONCAT(t1.fname,'',t1.lname) AS mainplayer,CONCAT(t2.fname,'',t2.lname) AS wicketplayer FROM batting b ,player t1, player t2 WHERE b.player_id=t1.player_id and match_id='%s' group by batting_id"%(mid)
    # q="select *,concat(player.fname,'',player.lname) as playername from player inner join match using (player_id) inner join batting using (match_id) where match_id='%s'"%(mid)
    data['res']=select(q)
    data['count']=len(select(q))

    return render_template("admin_add_batting.html",data=data)



@admin.route('/admin_add_bowling',methods=['get','post'])
def admin_add_bowling():
    data={}
    mid=request.args['mid']

    q="select * from player"
    data['player']=select(q)
    
    if 'btn' in request.form:
        player_id=request.form['player_id']
        overs=request.form['overs']
        wtaken=request.form['wtaken']
        runs=request.form['runs']
        
        
        q="select * from bowling where match_id='%s' and player_id='%s'"%(mid,player_id)
        res=select(q)
        if res:
            q="update bowling set overs_bowled='%s', wickets_taken='%s', runs_conceded='%s' where match_id='%s' and player_id='%s'"%(overs,wtaken,runs,mid,player_id)
            update(q)
        else:
            q="insert into bowling values (null,'%s','%s','%s','%s','%s')"%(mid,player_id,overs,wtaken,runs)
            insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_add_bowling",mid=mid))

    q="SELECT *,CONCAT(t1.fname,'',t1.lname) AS mainplayer,CONCAT(t2.fname,'',t2.lname) AS wicketplayer FROM bowling b ,player t1, player t2 WHERE b.player_id=t1.player_id and match_id='%s' group by bowling_id"%(mid)
    # q="select *,concat(player.fname,'',player.lname) as playername from player inner join match using (player_id) inner join batting using (match_id) where match_id='%s'"%(mid)
    data['res']=select(q)
    data['count']=len(select(q))

    return render_template("admin_add_bowling.html",data=data)



@admin.route('/admin_add_extras',methods=['get','post'])
def admin_add_extras():
    data={}
    mid=request.args['mid']

    q="select * from player"
    data['player']=select(q)
    
    if 'btn' in request.form:
        runs=request.form['runs']
        player_id=request.form['player_id']

        q="insert into extras values (null,'%s','%s','%s')"%(mid,runs,player_id)
        insert(q)
        flash("Successfully Added")
        return redirect(url_for("admin.admin_add_extras",mid=mid))

    q="SELECT *,CONCAT(t1.fname,'',t1.lname) AS mainplayer,CONCAT(t2.fname,'',t2.lname) AS wicketplayer FROM extras b ,player t1, player t2 WHERE b.bowler_id=t1.player_id and match_id='%s' group by extra_id "%(mid)
    # q="select *,concat(player.fname,'',player.lname) as playername from player inner join match using (player_id) inner join batting using (match_id) where match_id='%s'"%(mid)
    data['res']=select(q)
    data['count']=len(select(q))

    return render_template("admin_add_extras.html",data=data)