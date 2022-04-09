import random
from flask import Flask
app = Flask(__name__)

print(__name__)

generated_number = random.randint(0, 10)


@app.route('/')
def heading():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src = "https://media.giphy.com/media/d1E1szXDsHUs3WvK/giphy.gif" width = 300 height = 300>'


@app.route('/<int:usernumber>')
def detect_user_number(usernumber):
    if usernumber < generated_number:
        return '<h1>Too Low, Try Again!</h1>' \
               '<img src = "https://media.giphy.com/media/7SrHwak3yoO9a/giphy.gif" width = 300 height = 300>'
    elif usernumber > generated_number:
        return '<h1>Too High, Try Again!</h1>' \
               '<img src = "https://media.giphy.com/media/fnkyJXcCXZngY/giphy.gif" width = 300 height = 300>'
    else:
        return '<h1>You Found Me!</h1>' \
               '<img src = "https://media.giphy.com/media/m6OomwWCojfS8/giphy.gif" width = 300 height = 300>'


if __name__ == "__main__":
    app.run(debug=True)
