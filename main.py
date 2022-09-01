from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    phrase = "This home page is awesome"
    return render_template('indx.html', phrase=phrase)


@app.route('/about')
def about():
    sum = 45 + 45
    return render_template('about.html', anything = sum)


if __name__ == '__main__':
    app.run(debug=False)