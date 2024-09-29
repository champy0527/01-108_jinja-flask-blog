import requests


class Post:
    def __init__(self):
        self.response = requests.get("https://api.npoint.io/b67ad1c30240153dba9c")
        self.response.raise_for_status()
        self.posts = self.response.json()

    def get_all_posts(self):
        return self.posts

    def get_post_content(self, post_id):
        body = self.posts[post_id]['body']
        title = self.posts[post_id]['title']
        subtitle = self.posts[post_id]['subtitle']
        image = self.posts[post_id]['image']
        date = self.posts[post_id]['date']
        author = self.posts[post_id]['author']

        return body, title, subtitle, image, date, author
