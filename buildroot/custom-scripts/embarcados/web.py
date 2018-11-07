from flask import Flask, flash, redirect, render_template, request, session, abort
from threading import Thread
import time
import os

is_running = False

def cam(delay,shots,local):
    try:
        file = open(local+"/index","r+")    
        index = int(file.readline())
        file.close()
    except:
        index = 0

    for x in range(0,shots):
        index= index+1
        os.system('fswebcam -r 640x480 -S 2 --jpeg -1 --no-banner --save '+local+'/img'+str(index)+'.jpg')
        os.system('cp '+local+'/img'+str(index)+'.jpg ./static/images/capture.jpg')

        time.sleep(delay) 
        

    file = open(local+"/index","w+")    
    file.write(str(index))
    file.close()
    
    global is_running
    is_running = False
    
 
app = Flask(__name__)
 
@app.route('/')
def home():
    #if not session.get('logged_in'):
    #    return render_template('login.html')
    #else:
        if is_running:
            return render_template('app.html')
        else:
            return render_template('page.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
        
@app.route('/app', methods=['POST','GET'])
def page():
        global is_running
    #if not session.get('logged_in'):
    #    return home()
    #else:
        if request.method == 'POST':
            delay = float(request.form['delay'])
            shots = int(request.form['shots'])
            local = request.form['local']
            cam_theread = Thread(target=cam,args=[delay,shots,local])
            is_running = True
            cam_theread.start()
        else:
            if not is_running:
                return home()
        return render_template('app.html') 

 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4004)
