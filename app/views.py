from flask import render_template, request
from app import app
from pandas import read_csv


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    up_file = request.files['file']

    if up_file:
        data = read_csv(up_file)
        return render_template('render.html', table=data.to_html())
    else:
        return render_template('upload_error.html', errors=["no file uploaded"])
