from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import CheckConstraint
from sqlalchemy import column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'

# init db
db = SQLAlchemy(app)
#create db model
class Orders(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	username  = db.Column(db.String(32),nullable=False)
	date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	price = db.Column(db.Float,nullable=False)
	# CheckConstraint(column(price)>=0)
	share_amount = db.Column(db.Integer,nullable=False)
	# CheckConstraint(column(share_amount)>=0)
	kind = db.Column(db.String(4),nullable=False)
	# CheckConstraint((column(kind)=='Sell') or (column(kind)=='Buy'))
	def __init__(self,username,price,share_amount,kind):
		self.username = username
		self.price = price
		self.share_amount = share_amount
		self.kind = kind


@app.route('/')
def index():
	return render_template("index.html")

# @app.route('/order',methods=['POST','GET'])
# def order():
# 	title = "order"
# 	return render_template("order.html")

@app.route('/buy',methods=['POST','GET'])
def buy():
	title = "buy"
	if request.method == "POST":
		username = request.form['username']
		share_amount = render.form['share_amount']
		price = request.form['price']
		order = Orders(username=username,share_amount=share_amount,price=price,kind="Buy")
		try:
			db.session.add(order)
			db.session.commit()
			return redirect('/buy')
		except:
			return "there was an error buying the share"
	return render_template("buy.html")

db.create_all()
