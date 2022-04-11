from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/68f6ef0a49f1ca921592'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:b_id>')
def b_post(b_id):
    blog_url = 'https://api.npoint.io/68f6ef0a49f1ca921592'
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    for blog_post in all_posts:
        if int(blog_post['id']) == int(b_id):
            print(blog_post)
            return render_template('post.html', see_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
