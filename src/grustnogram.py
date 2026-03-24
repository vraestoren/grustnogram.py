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
        self.user_id = None

    def _post(self, endpoint: str, data: dict = None) -> dict:
        return self.session.post(
            f"{self.api}{endpoint}", json=data).json()

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def _put(self, endpoint: str, data: dict = None) -> dict:
        return self.session.put(
            f"{self.api}{endpoint}", json=data).json()

    def _delete(self, endpoint: str) -> dict:
        return self.session.delete(
            f"{self.api}{endpoint}").json()

    def _filter(self, data: dict) -> dict:
        return {key: value for key, value in data.items() if value is not None}

    def upload_media(self, file: bytes) -> dict:
        files = {
            "file": ("image.jpg", file, "image/jpg")
        }
        return self.session.post(
            f"{self.media_api}/cors.php", files=files).json()

    def login(self, email: str, password: str) -> dict:
        data = {
            "email": email,
            "password": password
        }
        response = self._post("/sessions", data)
        if response["data"]:
            self.access_token = response["data"]["access_token"]
            self.session.headers["access-token"] = self.access_token
            self.user_id = self.get_current_session()["data"]["id"]
        return response

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
        return self._post("/users", data)

    def get_current_session(self) -> dict:
        return self._get("/users/self")

    def get_phone_activation_code(
            self,
            phone_key: str,
            phone_number: str) -> dict:
        data = {
            "phone_key": phone_key,
            "phone": phone_number
        }
        return self._post("/callme", data)

    def activate_phone(
            self,
            phone_number: str,
            activation_code: int) -> dict:
        data = {
            "phone": phone_number,
            "code": activation_code
        }
        return self._post("/phoneactivate", data)

    def reset_password(self, email: str) -> dict:
        data = {
            "email": email
        }
        return self._post("/respsswd", data)

    def like_post(self, post_id: int) -> dict:
        return self._post(f"/posts/{post_id}/like")

    def unlike_post(self, post_id: int) -> dict:
        return self._delete(f"/posts/{post_id}/like")

    def get_post_comments(
            self, post_id: int, offset: int = 0) -> dict:
        return self._get(
            f"/posts/{post_id}/comments?offset={offset}")

    def get_post_likes(
            self, post_id: int, offset: int = 0) -> dict:
        return self._get(
            f"/posts/{post_id}/likes?offset={offset}")

    def get_status(self) -> dict:
        return self._get("/status")

    def get_posts_list(self, post_type: str = None) -> dict:
        params = {post_type: 1} if post_type else {}
        return self._get("/posts", params)

    def get_user_posts(
            self,
            user_id: int,
            limit: int = 15,
            offset: int = 0) -> dict:
        return self._get(
            f"/posts?id_user={user_id}&limit={limit}&offset={offset}")

    def comment_post(
            self,
            post_id: int,
            comment: str,
            reply_to: int = -1) -> dict:
        data = {
            "comment": comment,
            "reply-to": reply_to
        }
        return self._post(f"/posts/{post_id}/comments", data)

    def delete_comment(self, comment_id: int) -> dict:
        return self._delete(f"/posts/comments/{comment_id}")

    def follow_user(self, user_id: int) -> dict:
        return self._post(f"/users/{user_id}/follow")

    def unfollow_user(self, user_id: int) -> dict:
        return self._delete(f"/users/{user_id}/follow")

    def get_user_followers(self, user_id: int) -> dict:
        return self._get(f"/followers/{user_id}")

    def get_user_followings(self, user_id: int) -> dict:
        return self._get(f"/follow/{user_id}")

    def edit_profile(
            self,
            nickname: str = None,
            name: str = None,
            about: str = None,
            avatar: bytes = None) -> dict:
        data = self._filter({
            "nickname": nickname,
            "name": name,
            "about": about,
            "avatar": self.upload_media(avatar)["data"] if avatar else None
        })
        return self._put("/users/self", data)

    def create_post(
            self,
            text: str,
            image: bytes,
            post_filter: int = 0) -> dict:
        data = {
            "media": [self.upload_media(image)["data"]],
            "text": text,
            "filter": post_filter
        }
        return self._post("/posts", data)

    def get_user_info(self, nickname: str) -> dict:
        return self._get(f"/users/{nickname}")

    def block_user(self, user_id: int) -> dict:
        return self._post(f"/users/{user_id}/block")

    def unblock_user(self, user_id: int) -> dict:
        return self._delete(f"/users/{user_id}/block")

    def report_user(
            self, user_id: int, report_type: int = 1) -> dict:
        data = {
            "type": report_type
        }
        return self._post(f"/users/{user_id}/complaint", data)

    def report_comment(self, comment_id: int) -> dict:
        return self._post(
            f"/posts/comments/{comment_id}/complaint")

    def report_post(
            self, post_id: int, report_type: int = 1) -> dict:
        data = {
            "type": report_type
        }
        return self._post(f"/posts/{post_id}/complaint", data)

    def like_comment(self, comment_id: int) -> dict:
        return self._post(f"/comments/{comment_id}/like")

    def unlike_comment(self, comment_id: int) -> dict:
        return self._delete(f"/comments/{comment_id}/like")

    def get_notifications(self) -> dict:
        return self._get("/notifications")

    def search_user(self, query: str) -> dict:
        return self._get(f"/users?q={query}")

    def search_post(self, query: str) -> dict:
        return self._get(f"/posts?q={query}")

    def get_users_list(self, top: int = 1) -> dict:
        return self._get(f"/users?top={top}")

    def change_password(
            self,
            old_password: str,
            new_password: str) -> dict:
        data = {
            "old_password": old_password,
            "new_password": new_password
        }
        return self._put("/users/self", data)

    def edit_post(self, post_id: int, text: str) -> dict:
        data = {
            "text": text
        }
        return self._put(f"/posts/{post_id}", data)

    def delete_post(self, post_id: int) -> dict:
        return self._delete(f"/posts/{post_id}")
