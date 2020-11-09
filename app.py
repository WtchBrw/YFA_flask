from flask import Flask, render_template, redirect, json, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', divs='')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(port=8000)