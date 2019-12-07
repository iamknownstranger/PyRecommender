from flask import Flask, render_template
from recommender import Recommender

app = Flask(__name__)

recommender = Recommender()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comedy')
def comedy():
    return render_template('layout.html', title="Comedy", tweets=recommender.get_tweets("best comedy netflix"))


@app.route('/horror')
def horror():
    return render_template('layout.html', title="Horror", tweets=recommender.get_tweets("best horror netflix"))


@app.route('/romance')
def romance():
    return render_template('layout.html', title="Romance", tweets=recommender.get_tweets("best romance netflix"))


@app.route('/action')
def action():
    return render_template('layout.html', title="Action", tweets=recommender.get_tweets("best action netflix"))


@app.route('/thriller')
def thriller():
    return render_template('layout.html', title="Thriller", tweets=recommender.get_tweets("best thriller netflix"))


@app.route('/drama')
def drama():
    return render_template('layout.html', title="Drama", tweets=recommender.get_tweets("best drama netflix"))


if __name__ == '__main__':
    app.run(debug=True)
