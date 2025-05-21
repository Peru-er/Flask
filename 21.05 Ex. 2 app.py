
from flask import Flask, render_template, redirect, url_for, abort
import random


app = Flask(__name__)


films = {
    1: {
        'title': 'Cruella',
        'description': 'A rebellious fashion icon rises in 1970s London. A stylish origin story of the legendary villain.'
    },
    2: {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'description': 'An orphan boy discovers he is a wizard and begins his journey at Hogwarts School of Witchcraft and Wizardry.'
    },
    3: {
        'title': 'Fantastic Beasts and Where to Find Them',
        'description': 'Magizoologist Newt Scamander arrives in New York with a suitcase full of magical creatures—and chaos ensues.'
    },
    4: {
        'title': 'The Lord of the Rings: The Fellowship of the Ring',
        'description': 'A hobbit sets out on an epic quest to destroy a powerful ring and save Middle-earth.'
    },
    5: {
        'title': 'Maleficent',
        'description': 'The untold story of Disney’s most iconic villain reveals a complex fairy cursed by betrayal and seeking justice.'
    }
}

@app.route('/')
def index():
    return render_template('index.html', films=films)

@app.route('/film/<int:film_id>')
def film_detail(film_id):
    film = films.get(film_id)
    if not film:
        abort(404)
    return render_template('film.html', film=film, film_id=film_id)

@app.route('/random')
def random_film():
    film_id = random.choice(list(films.keys()))
    return redirect(url_for('film_detail', film_id=film_id))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
