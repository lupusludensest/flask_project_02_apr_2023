from flask import Flask, render_template
from utils.view_modifiers import response

app = Flask(__name__)

def get_films():
    return [
    {
        'id': 1,
        'title': 'The Matrix\'s best',
        'release_date': '1999-03-31',
    },
    {
        'id': 2,
        'title': 'Harry Potter and the Chamber of Secrets',
        'release_date': '2002-11-13',
    },
    {
        'id': 3,
        'title': 'Brother-1',
        'release_date': '2000-05-11',
    },
]

@app.route('/')
@app.route('/hello')
@response(template_file='hello.html')
def index():
    films = get_films()
    # return render_template('hello.html', films=films)
    return {'films': films}

@app.route('/about')
def about():
    # return render_template('about.html', title='About')
    return {'title': 'About'}

@app.route('/<string:name>')
def greeting(name: str):
    return f'<h1>Hello, {name.capitalize()}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)


