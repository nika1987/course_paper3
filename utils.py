import json

from json import JSONDecodeError


from constants import JSON_FILE, COMMENT_FILE


class PostHandler:
    @staticmethod
    def load_json(file_name):
        """
        Функция загружает данные из json файла
        :param file_name: json файл
        :return: возвращает список словарей
        """
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                posts = json.load(f)
        except FileNotFoundError:
            print('Ошибка файл не найден')
            return posts
        except JSONDecodeError:
            print('Ошибка получения данных из Json')
            return posts
        return posts


    def get_posts_all(self):
        """
        Функция загружает возвращает все посты
        :return: все посты из json формата в формате python.
        """
        return self.load_json(JSON_FILE)


    def get_posts_by_user(self, user_name):
        """
        Метод возвращает посты определенного пользователя.
        :param user_name: атрибут метода для поиска поста по имени.
        :return: посты определенного пользователя.
        """
        posts = []
        posts_data = self.get_posts_all()
        try:
            for poster in posts_data:
                if user_name.lower() == poster['poster_name'].lower():
                    posts.append(poster)
        except ValueError:
            print('Такого пользователя нет')
            return posts
        return posts

    # post_handler = PostHandler()
    # print(post_handler.get_posts_by_user("leo"))

    def get_comments_by_post_id(self, post_id):
        """
        Метод возвращает комментарии определенного поста.
        :param post_id:id для поиска комментарий определенного поста
        :return:комментарии определенного пользователя
        """
        found_comments = []
        found_posts = self.get_post_by_pk(post_id)
        if not found_posts:
            raise ValueError

        comments_data = self.load_json(COMMENT_FILE)
        try:
            for comment in comments_data:
                if post_id == comment['post_id']:
                    found_comments.append(comment)
        except KeyError:
            print('Нет такого ключа')
            return []
        return found_comments

    def search_for_posts(self, query):
        """
        Функция возвращает список постов по ключевому слову
        :param query:атрибут метода для поиска поста по  ключевому слову
        :return: список постов по ключевому слову
        """
        list_query = []
        posts = self.get_posts_all()
        for post in posts:
            if query.lower() in post['content'].lower():
                list_query.append(post)
        return list_query

    def get_post_by_pk(self, pk):
        """
        Функция  возвращает один пост по его идентификатору.
        :param pk:атрибут метода для поиска поста по идентификатору
        :return:возвращаает один пост по его идентификатору
        """

        posts_data = self.get_posts_all()
        for post in posts_data:
            if post["pk"] == pk:
                return post

# post_handler = PostHandler()
# print(post_handler.get_post_by_pk(3))
#post_handler = PostHandler()
#print(post_handler.search_for_posts("еда"))
#post_handler = PostHandler()
#print(post_handler.search_for_posts("еда"))






