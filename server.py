from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key="secretkey"

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    if 'text' not in session:
        session['text']=""
    print(session['num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if session['num'] == guess:
        session['text'] = "You Win! Please Reset to Play again"
    elif session['num'] < guess:
        session['text'] = "Too High!"
    elif session['num'] > guess:
        session['text'] = "Too Low!"
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)