from flask import Flask, jsonify, render_template, url_for
app = Flask(__name__) 

@app.route('/') 
def hello():
	results = {} 
	return render_template('index.html', results=results)


@app.route('/test/') 
def test():
	return 'Success'
	
if __name__ == '__main__': 
	app.run()