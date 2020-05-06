from flask import Flask, render_template
from recommender import Recommender

# flask app
app = Flask(__name__)

# intialize a Recommender object
recommender = Recommender()


# route for index page
@app.route('/')
def index():
    """
        function index renders the index.html template
    """
    return render_template('index.html')

# route for comedy tweets
@app.route('/comedy')
def comedy():
    """
        function comedy renders layout.html with comedy tweets
    """
    return render_template('layout.html', title="Comedy", tweets=recommender.get_tweets("best comedy netflix"))

# route for horror tweets
@app.route('/horror')
def horror():
    """
        function comedy renders layout.html with comedy tweets
    """
    return render_template('layout.html', title="Horror", tweets=recommender.get_tweets("best horror netflix"))

# route for romance tweets
@app.route('/romance')
def romance():
    """
        function comedy renders layout.html with romance tweets
    """
    return render_template('layout.html', title="Romance", tweets=recommender.get_tweets("best romance netflix"))

# route for action tweets
@app.route('/action')
def action():
    """
        function comedy renders layout.html with action tweets
    """
    return render_template('layout.html', title="Action", tweets=recommender.get_tweets("best action netflix"))

# route for thriller tweets
@app.route('/thriller')
def thriller():
    """
        function comedy renders layout.html with thriller tweets
    """
    return render_template('layout.html', title="Thriller", tweets=recommender.get_tweets("best thriller netflix"))

# route for drama tweets
@app.route('/drama')
def drama():
    """
        function comedy renders layout.html with drama tweets
    """
    return render_template('layout.html', title="Drama", tweets=recommender.get_tweets("best drama netflix"))


# driver
if __name__ == '__main__':
    app.run(debug=True)
