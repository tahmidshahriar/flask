from flask import Flask, render_template, request
from forms import TodoForm
import pymongo

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	form = TodoForm()
	if form.validate_on_submit():
		try:
			conn=pymongo.MongoClient()
			db = conn.test
			todo = db.todo
			data = {}
			print request.form['todo']
			data['todo'] = request.form['todo']
			todo.insert(data)
			return redirect('/')
		except:
			print "Failed"
			return redirect('/')
	else:
		try:
			conn=pymongo.MongoClient()
			db = conn.test
			todo = db.todo
			myList = list(todo.find())
			print myList
			return render_template('./app.html', form=form, myList = myList)
		except:
			print "Failed"
			return render_template('./app.html', form=form, myList = [])



if __name__ == "__main__":
	app.debug = True
	app.secret_key = "hi"
	app.run()


