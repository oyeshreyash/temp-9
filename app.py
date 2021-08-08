from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/hbd', methods=['POST', 'GET'])
def hbd():
    pin  = request.form['password']
    if pin == '2707':
        return render_template('hbd.html')
    else:
        return render_template('invalid.html')

if __name__ == '__main__':
    app.run(debug=True)