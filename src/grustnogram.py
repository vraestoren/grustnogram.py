from requests import Session

class GrustnoGram:
    def __init__(self) -> None:
        self.api = "https://api.grustnogram.ru"
        self.media_api = "https://media.grustnogram.ru"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Dart/2.16 (dart:io)"
        }
        self.access_token = None

    def upload_media(self, file: bytes) -> dict:
        files = {
            "file": (
                "image.jpg",
                file,
                "image/jpg"
            )
        }
        return self.session.post(
            f"{self.media_api}/cors.php", files=files).json()

    def login(self, email: str, password: str) -> dict:
        data = {
            "email": email,
            "password": password
        }
        response = self.session.post(
            f"{self.api}/sessions", json=data).json()
        if response["data"]:
            self.access_token = response["data"]["access_token"]
            self.session.headers["access-token"] = self.access_token
            self.user_id = self.get_current_session()["data"]["id"]
        return response

    def get_current_session(self) -> dict:
        return self.session.get( f"{self.api}/users/self").json()

    def register(
            self,
            nickname: str,
            email: str,
            password: str) -> dict:
        data = {
            "nickname": nickname,
            "email": email,
            "password": password
        }
        return self.session.post(
            f"{self.api}/users", json=data).json()

    def get_phone_activation_code(
            self,
            phone_key: str,
            phone_number: str) -> dict:
        data = {
            "phone_key": phone_key,
            "phone": phone_number
        }
        return self.session.post(
            f"{self.api}/callme", json=data).json()

    def activate_phone(
            self,
            phone_number: str,
            activation_code: int) -> dict:
        data = {
            "phone": phone_number,
            "code": activation_code
        }
        return self.session.post(
            f"{self.api}/phoneactivate", json=data).json()

    def reset_password(self, email: str) -> dict:
        data = {
            "email": email
        }
        return self.session.post(
            f"{self.api}/respsswd", json=data).json()

    def like_post(self, post_id: int) -> dict:
        return self.session.post(
            f"{self.api}/posts/{post_id}/like").json()

    def unlike_post(self, post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}/like").json()

    def get_post_comments(
            self,
            post_id: int,
            offset: int = 0) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/comments?offset={offset}").json()

    def get_post_likes(
            self,
            post_id: int,
            offset: int = 0) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/likes?offset={offset}").json()

    def get_status(self) -> dict:
        return self.session.get(
            f"{self.api}/status").json()

    def get_posts_list(self, type: str = None) -> dict:
        params = {type: 1} if type else {}
        return self.session.get(
            f"{self.api}/posts", params=params).json()

    def get_user_posts(
            self,
            user_id: int,
            limit: int = 15,
            offset: int = 0) -> dict:
        return self.session.get(
            f"{self.api}/posts?id_user={user_id}&limit={limit}&offset={offset}").json()

    def comment_post(
            self,
            post_id: int,
            comment: str,
            reply_to: int = -1) -> dict:
        data = {
            "comment": comment,
            "reply-to": reply_to
        }
        return self.session.post(
            f"{self.api}/posts/{post_id}/comments", json=data).json()

    def delete_comment(self, comment_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/comments/{comment_id}").json()

    def follow_user(self, user_id: int) -> dict:
        return self.session.post(
            f"{self.api}/users/{user_id}/follow").json()

    def unfollow_user(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/{user_id}/follow").json()

    def get_user_followers(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/followers/{user_id}").json()

    def get_user_followings(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/follow/{user_id}").json()

    def edit_profile(
            self,
            nickname: str = None,
            name: str = None,
            about: str = None,
            avatar: bytes = None) -> dict:
        data = {
            "nickname": nickname,
            "name": name,
            "about": about,
            "avatar": self.upload_media(avatar)["data"] if avatar else None
        }
        filtered_data = {
            key: value for key, value in data.items() if value is not None
        }
        return self.session.put(
            f"{self.api}/users/self", json=filtered_data).json()

    def create_post(
            self,
            text: str,
            image: bytes,
            filter: int = 0) -> dict:
        data = {
            "media": [self.upload_media(image)["data"]],
            "text": text,
            "filter": filter
        }
        return self.session.post(
            f"{self.api}/posts", json=data).json()

    def get_user_info(self, nickname: str) -> dict:
        return self.session.get(
            f"{self.api}/users/{nickname}").json()

    def block_user(self, user_id: int) -> dict:
        return self.session.post(
            f"{self.api}/users/{user_id}/block").json()

    def unblock_user(self, user_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/users/{user_id}/block").json()

    def report_user(
            self,
            user_id: int,
            type: int = 1) -> dict:
        data = {
            "type": type
        }
        return self.session.post(
            f"{self.api}/users/{user_id}/complaint", json=data).json()

    def report_comment(self, comment_id: int) -> dict:
        return self.session.post(
            f"{self.api}/posts/comments/{comment_id}/complaint").json()

    def report_post(
            self,
            post_id: int,
            type: int = 1) -> dict:
        data = {
            "type": type
        }
        return self.session.post(
            f"{self.api}/posts/{post_id}/complaint", json=data).json()

    def like_comment(self, comment_id: int) -> dict:
        return self.session.post(
            f"{self.api}/comments/{comment_id}/like").json()

    def unlike_comment(self, comment_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/comments/{comment_id}/like").json()

    def get_notifications(self) -> dict:
        return self.session.get(
            f"{self.api}/notifications").json()

    def search_user(self, query: str) -> dict:
        return self.session.get(
            f"{self.api}/users?q={query}").json()

    def search_post(self, query: str) -> dict:
        return self.session.get(
            f"{self.api}/posts?q={query}").json()

    def get_users_list(self, top: int = 1) -> dict:
        return self.session.get(
            f"{self.api}/users?top={top}").json()

    def change_password(
            self,
            old_password: str,
            new_password: str) -> dict:
        data = {
            "old_password": old_password,
            "new_password": new_password
        }
        return self.session.put(
            f"{self.api}/users/self", json=data).json()

    def edit_post(self, post_id: int, text: str) -> dict:
        data = {
            "text": text
        }
        return self.session.put(
            f"{self.api}/posts/{post_id}", json=data).json()

    def delete_post(self, post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}").json()
