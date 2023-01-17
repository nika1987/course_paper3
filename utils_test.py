from main import app
import pytest
from utils import PostHandler


@pytest.fixture()
def testing_app():
    return app.test_client()


class TestApi:
    def test_api_posts(self, testing_app):
        respons = testing_app.get('/api/posts/')
        assert respons.status_code == 200, "Статус код не 200"
        result = respons.json
        assert type(result) is list, "Не верный тип данных"
        assert len(result) > 0, "Список пуст"
        for item in result:
            assert type(item) is dict, "Не верный тип данных"

    def test_api_post(self, testing_app):
        respons = testing_app.get('/api/posts/1')
        assert respons.status_code == 200, "Статус код не 200"
        result = respons.json
        assert type(result) is dict, "Не верный тип данных"
        assert len(result.items()) > 0, "Словарь пуст"

    def test_get_post_by_pk(post_number_1):
        post_handler = main()
        post = [post_handler.get_post_by_pk(1)]
        assert post == post_number_1

    def test_get_posts_all():
        post_handler = main()
        len_posts = len(post_handler.get_posts_all())
        assert len_posts == 8

    def test_get_posts_by_user():
        post_handler = main()
        user_post = post_handler.get_posts_by_user('leo')
        assert len(user_post) == 2

    def test_get_comments_by_post_id(comments_7):
        post_handler = main()
        comments = post_handler.get_comments_by_post_id(7)
        assert comments == comments_7

    def test_search_for_posts(post_number_1):
        post_handler = main()
        search_posts = post_handler.search_for_posts('еда')
        assert search_posts == post_number_1