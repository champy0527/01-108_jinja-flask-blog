from flask import Flask, render_template
import requests
from post import Post

post = Post()

app = Flask(__name__)


@app.route('/')
def index():
    blog_posts = post.get_all_posts()
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:post_id>')
def read_more(post_id):
    post_body, post_title, post_subtitle, post_image, post_date, post_author = post.get_post_content(post_id)
    return render_template('post.html', body=post_body, title=post_title, subtitle=post_subtitle, image=post_image, date=post_date, author=post_author)


if __name__ == "__main__":
    app.run(debug=True)
