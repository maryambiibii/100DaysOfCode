from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

URL = 'https://api.npoint.io/56bf09b124bad6647093'
response = requests.get(URL)
all_posts = response.json()
print(all_posts)


@app.route('/')
def home():
    date = datetime.datetime.now()
    post_date = date.strftime("%B %d, %Y")
    return render_template('index.html', b_posts=all_posts, post_date=post_date)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:b_id>')
def post(b_id):
    date = datetime.datetime.now()
    post_date = date.strftime("%B %d, %Y")
    author = 'Maryam Bibi'
    for blog_post in all_posts:
        if int(blog_post['id']) == int(b_id):
            print(blog_post)
            return render_template('post.html', see_post=blog_post, post_date=post_date, author=author)


if __name__ == '__main__':
    app.run(debug=True)