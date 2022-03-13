from flask import Flask,render_template,request,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#setting up configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/nasseh/Python-Flask/nassehblog/myblog.db'
db = SQLAlchemy(app)

class PostedBlog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(100))
    author = db.Column(db.String(50))
    date_of_post = db.Column(db.DateTime)
    blog_content = db.Column(db.Text)


#initialize flask extensions
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # quotes = get_quotes()
    title = 'Home: Welcome to my blog'
    return render_template('index.html', title = title)

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