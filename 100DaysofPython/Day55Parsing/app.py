from flask import Flask
import random
app = Flask(__name__)


def make_bold(func):
    def wrapper(**kwargs):
        return '<b>' + func(**kwargs) + '</b>'
    wrapper.__name__ = func.__name__
    return wrapper


def make_emphasis(func):
    def wrapper(**kwargs):
        return "<em>" + func(**kwargs) + "</em>"
    wrapper.__name__ = func.__name__
    return wrapper


def make_underline(func):
    def wrapper(**kwargs):
        return "<u>" + func(**kwargs) + "</u>"
    wrapper.__name__ = func.__name__
    return wrapper


@app.route('/')
def home_page():
    return f'<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


secret_number = random.randint(0, 9)


@app.route('/<int:num>')
def num_page(num):
    if secret_number == num:
        return f'<h1 style="text-green">You found me!</h1><img src="https://media3.giphy.com/media/CqVNwrLt9KEDK/giphy.gif">'
    elif secret_number > num:  # too low
        return f'<h1 style="text-red">Too low, try again!</h1><img src="https://media3.giphy.com/media/ExMGjbktr4phe/giphy.gif">'
    elif secret_number < num:  # too high
        return f'<h1 style="text-blue">Too high, try again!</h1><img src="https://media3.giphy.com/media/UotLuplZSzKRa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
