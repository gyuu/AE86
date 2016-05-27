from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    )

from car import move

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/car', methods=['POST'])
def car():
	op = request.form['op']
	if not op:
		return jsonify(status='400', mesg='no op.')
	else:
		# move(op)
		return jsonify(status='200', mesg=op)

if __name__ == '__main__':
    app.run(debug=True)
