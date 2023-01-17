import logging

from flask import Flask, render_template, request, jsonify

import utils

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
post_handler = utils.PostHandler()
logging.basicConfig(filename='api.log', format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.INFO, encoding='UTF=8')


@app.route('/')
def index():
    data = post_handler.get_posts_all()
    return render_template("index.html", data=data)


@app.route('/posts/<int:post_id>')
def page_post(post_id):
    post = post_handler.get_post_by_pk(post_id)
    comments = post_handler.get_comments_by_post_id(post_id)
    count_comments = len(comments)
    return render_template("post.html", post=post, comments=comments, count_comments=count_comments)


@app.route('/search/')
def post_search():
    query_word = request.args.get("s")
    posts = post_handler.search_for_posts(query_word)
    count_posts = len(posts)
    if count_posts > 10:
        posts = posts[:10]
    return render_template("search.html", query_word=query_word, posts=posts, count_posts=count_posts)


@app.route('/users/<user_name>')
def get_user_post(user_name):
    user_posts = post_handler.get_posts_by_user(user_name)
    return render_template("user-feed.html", user_posts=user_posts)


@app.errorhandler(404)
def error_404(err):
    return f"Такой страницы не существует, код ошибки {err}"


@app.errorhandler(500)
def error_500(err):
    return f"Ошибка сервера, код ошибки {err}"


@app.route('/api/posts/')
def api_posts():
    logging.info('Запрос /api/posts')
    data = post_handler.get_posts_all()
    return jsonify(data)


@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    logging.info(f'Запрос /api/posts/{post_id}')
    post = post_handler.get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run()


