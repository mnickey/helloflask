from flask import Flask

app = Flask(__name__)

@app.route("/")
def root_route():
	return "Hello World! \n For a more personalized version try adding /YOUR_NAME to the end of this URL"

@app.route("/hello")
def hello_world():
	return "Hello World! \n For a more personalized version try adding /YOUR_NAME to the end of this URL"

@app.route("/hello/<name>")
def hello_person(name):
	html = """
	<h1>
		Hello {}!
	</h1>
	<p>
		This is still under construction... so instead of a silly kitten...
	</p>
	<p>
		Here's a picture of a Charlie Sheen. Awww...
	</p>
	<img src="http://placesheen.com/200/300">
	"""
	return html.format(name.title())

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080)