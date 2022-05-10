from flask import Flask, Response, render_template, request, redirect, session, url_for, flash, jsonify
import predict

app = Flask(__name__)
app.secret_key = "sasank"

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST":
		values = request.form.to_dict()
		search,mode = values["searchbtn"],values["mode"]
		ans = predict.predict(search)
		flash("fake news") if ans == 1 else flash("real news")
		# flash("fake news"?ans:"real news")
		# flash(str(ans))
		return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True,port=8000)