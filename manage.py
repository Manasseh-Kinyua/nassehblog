from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import urllib.request,json
# from .models import Quotes
# from .request import get_quotes


app = Flask(__name__)

#setting up configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nasseh/Python-Flask/nassehblog/myblog.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nwuxebpglulhwp:0955a892af88faaa6ab6ef03da81e3e846d32b86b83b3c215ae417e6b6ccebd8@ec2-54-224-120-186.compute-1.amazonaws.com:5432/dctjb313qu3sen'


db = SQLAlchemy(app)


class PostedBlog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_of_post = db.Column(db.DateTime)
    blog_content = db.Column(db.Text)

class Quotes:
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote


#initialize flask extensions
bootstrap = Bootstrap(app)

base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quotes():
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quote_obj = None
        if get_quotes_response:
            author = get_quotes_response.get('author')
            quote = get_quotes_response.get('quote')

            quote_obj = Quotes(author,quote)

    return quote_obj



@app.route('/')
def index():
    posts = PostedBlog.query.order_by(PostedBlog.date_of_post.desc()).all()
    quotes = get_quotes()
    title = 'Home: Welcome to my blog'
    return render_template('index.html', title = title, posts=posts, quotes=quotes)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = PostedBlog.query.filter_by(id=post_id).one()

    date_of_post = post.date_of_post.strftime('%b %d, %y')

    return render_template('post.html', post=post, date_of_post=date_of_post)


@app.route('/about')
def about():
    title = 'Home: Welcome to my blog'
    return render_template('about.html', title = title)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    blog_content = request.form['blog_content']

    post = PostedBlog(title=title, subtitle=subtitle, author=author, blog_content=blog_content, date_of_post=datetime.now())
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))






if __name__ == '__main__':
    app.run(debug = True)