from flask import Flask, render_template, request
from forms import TodoForm
import pymongo

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	form = TodoForm()
	if form.validate_on_submit():
		return render_template('./app.html', form=form, myList = [])
	else:
		return render_template('./app.html', form=form, myList = [])


if __name__ == "__main__":
	app.debug = True
	app.secret_key = "hi"
	app.run()


