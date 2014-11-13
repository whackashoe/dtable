from flask import render_template, request
from app import app
from pandas import read_csv, parser


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    up_file = request.files['file']

    if up_file:
    	try:
        	data = read_csv(up_file)
        except (parser.CParserError):
      		return render_template('error.html', errors=["CSV parse error"])

        return render_template('render.html', table=data.to_html())
    else:
        return render_template('error.html', errors=["no file uploaded"])
