from flask import *
from flask import flash
import bcrypt
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
import os
from flask_login import LoginManager
from functools import wraps
from wtforms import *
import psycopg2
# login_manager = LoginManager()


app=Flask(__name__,template_folder='templates')

# app.secret_key = "super secret key"
# app.config['MYSQL_HOST']='localhost'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']=''
# app.config['MYSQL_DB']='professionals'
# mysql=MySQL(app)
# login_manager.init_app(app)
con = psycopg2.connect(dbname="professionals", user='postgres', host='localhost', password='Post@515',port=5433)


@app.route('/')
def index():
    return render_template('/Member/Index.html')

@app.errorhandler(404) 
def invalid_route(e): 
    return "Invalid route."

@app.route('/signin')
def signin():
    return render_template('/Member/Signin.html')

def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('empsigin'))
    return wrap



@app.route('/empsignin',methods=['GET','POST'])
def empsigin():
    message = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'empid' in request.form and 'emppass' in request.form:
        # Create variables for easy access
        empid = request.form['empid']
        emppassword = request.form['emppass']
        # Check if account exists using MySQL
       # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur1 = con.cursor()
        cur1.execute('SELECT * FROM empinfo WHERE empid = %s AND emppass = %s', (empid, emppassword))
        # Fetch one record and return result
        
        empvalidation= cur1.fetchone()
               
        if empvalidation:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['empid'] = empvalidation[0]  #'empid'
            session['emppassword'] = empvalidation[1]  #'emppass'
            
            # Redirect to home page
           # return render_template('/Member/Home.html')
            return redirect(url_for('main'))
        else:
            # Account doesnt exist or username/password incorrect
            message = 'Incorrect username/password!'
            flash(message)
    return render_template('/Member/index.html', message='')

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

@app.route('/backtomain')
def backtomain():
    return render_template('/Member/Home.html')

@app.route('/main')
#@login_required
def main():
    #   flash("Welcome session[empid]")
      eid=session['empid']
    #  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      cur2 = con.cursor()
      cur2.execute('SELECT * FROM empinfo WHERE empid= %s ',(eid,))
      ename=cur2.fetchall()
      con.commit()
      return render_template('/Member/Home.html',name=ename,id=session['empid'])


@app.route('/viewprofile')
# @login_required
def viewprofile():
    profileid=session['empid']
    #cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur = con.cursor()
    cur.execute('SELECT * from empinfo where empid= %s',(profileid,))
    profile=cur.fetchall()
    return render_template('/Member/Profile.html',profile=profile,profileid=profileid)


@app.route('/updateprofile/<int:id>',methods=['POST','GET'])
def updateprofile(id):
    id=session['empid']
    if request.method == 'POST':
        
        empphno = request.form['phone-number']
        empseating = request.form['seating']
        
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur = con.cursor()
        cur.execute("UPDATE empinfo SET phno = %s, seating= %s WHERE empid = %s", 
               (empphno,empseating, session['empid'],))
        
        
        con.commit()
        
        return redirect(url_for('viewprofile'))
               

    return render_template('/Member/Updatefield.html',id=id)

@app.route('/teamdirectory')
def teamdirectory():
    return render_template('/Member/Directory.html')

@app.route('/humanresource')
def humanresource():
    teamname='Human Resource'
    head='Guru Moorthi K'
  #  cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur = con.cursor()
    cur.execute('SELECT * from  hr')
    team_profile=cur.fetchall()
    return render_template('/Member/Directory-profiles.html',head=head,team_profile=team_profile,team_name=teamname)

@app.route('/employeeinfo/<int:eid>',methods=['POST','GET'])
def employeeinfo(eid):
    s_id=session['empid']
   # cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur = con.cursor()
    cur.execute('SELECT * from  hr where id=%s',(eid,))
    team_p=cur.fetchall()
    con.commit()
    # if request.method=='POST':
    #     skill = request.form['skills']
    #     # cur.execute("INSERT INTO skillsets(id,s1,s2,s3,s4,s5) VALUES (%s,%s,%s,%s,%s,%s)",
    #     # (session['empid'],"k","c","e","d","p",))   
    #     cur = con.cursor()   
    #     cur.execute("insert into skillsets(id,skill) values(%s,%s)",(s_id,skill,))
   
        
    # cur = con.cursor()
    cur.execute('SELECT * from  skillset where empid=%s',(s_id,))
    empSkills=cur.fetchall()
      
    return render_template('/Member/Employeeinfo.html',team_p=team_p,s_id=s_id,empSkills=empSkills)


@app.route('/employeeskills/<int:seid>',methods=['POST','GET'])
def employeeskills(seid):
    seid=session['empid']
    if request.method=='POST':
        skill = request.form['skills']
        # cur.execute("INSERT INTO skillsets(id,s1,s2,s3,s4,s5) VALUES (%s,%s,%s,%s,%s,%s)",
        # (session['empid'],"k","c","e","d","p",))   
        cur = con.cursor()   
        cur.execute("insert into skillset(empid,skill) values(%s,%s)",(seid,skill,))
   
        con.commit()
    
    return render_template('/Member/Employeeskills.html',id=seid)

@app.route('/skilldetails/<int:uid>',methods=['post','get'])
def skilldetails(uid):
    seid=session['empid']
    cur = con.cursor()   
    cur.execute("select skill from skillset where uid=%s",(uid,))
    skillrecord=cur.fetchone()
    cur = con.cursor() 
    cur.execute("select uid from skillset where uid=%s",(uid,)) 
    del_id=cur.fetchone()
    return render_template('/Member/SkillDetails.html',skillrecord=skillrecord,del_id=del_id,seid=seid)

@app.route("/delete_data/<int:uid>", methods=["GET","POST"])
def delete_data(uid):
    seid=session['empid']
    cur= con.cursor() 
    # cur.execute("select empid from skillset where uid=%s",(uid,))
    # id_check=cur.fetchone()

    cur.execute("delete from skillset where uid=%s and empid=%s",(uid,seid,))
    cur.connection.commit()
    cur.close() 
    

    return redirect(url_for('employeeinfo',eid=seid))


@app.route('/userlogout')
def userlogout():
    session.pop('empid')
    return redirect(url_for('index'))


if __name__=='__main__':
    app.secret_key='super secret key'
    app.run(debug=True)
