from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
	cpu = psutil.cpu_percent(interval=1)
	ram = psutil.virtual_memory().percent
	disk = psutil.disk_usage('/').percent
	temp = psutil.sensors_temperatures()
	cpu_temp = temp['cpu_thermal'][0].current if 'cpu_thermal' in temp else 0
	uptime = psutil.boot_time()
	return render_template('index.html', cpu=cpu, ram=ram, disk=disk, temp=cpu_temp)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
