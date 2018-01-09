from flask import Flask, render_template, request
#from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()


