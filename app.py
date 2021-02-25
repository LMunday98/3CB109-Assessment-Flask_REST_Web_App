from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
   return 'Hello %s!' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('hello',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('hello',name = user))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug=True)