from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)


pincodes=[303030,202020,404020]

@app.route('/')
def index():
   return render_template('mediserve.html')

@app.route('/mid',methods = ['POST','GET'])
def mid():
	if request.method == 'POST':
		pin=int(request.form['pin'])
		if pin in pincodes:
			return redirect(url_for('fir'))
		else:
		    return 'delivey is not available on your pincode'

@app.route('/success')
def success():
   return 'logged in successfully'


@app.route('/fir')
def fir():
	return render_template('r.html')

if __name__ == '__main__':
   app.run(debug = True)
