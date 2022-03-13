from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#setting up configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/nasseh/Python-Flask/nassehblog/myblog.db'
db = SQLAlchemy(app)

class PostedBlog(db.Model):
    id = db.column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.string(100))
    date_of_post = db.Column(db.DateTime)
    blog_content = db.Column(db.Text)


#initialize flask extensions
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # quotes = get_quotes()
    title = 'Home: Welcome to my blog'
    return render_template('index.html', title = title)

@app.route('/about')
def about():
    title = 'Home: Welcome to my blog'
    return render_template('about.html', title = title)




if __name__ == '__main__':
    app.run(debug = True)