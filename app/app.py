from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def dashboard():
	metrics = {
		'cpu':psutil.cpu_percent(interval=1),
		'ram':psutil.virtual_memory().percent,
		'disk':psutil.disk_usage('/').percent
	}
	return render_template('dashboard.html', metrics=metrics)

if __name__=='__main__':
	app.run(host='0.0.0.0', port=5000)
