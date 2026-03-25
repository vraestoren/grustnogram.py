# <img src="https://grustnogram.ru/favicon/apple-icon.png" width="28" style="vertical-align:middle;" />  grustnogram.py

> Mobile-API for [GrustnoGram](https://play.google.com/store/apps/details?id=com.tokarevco.grustnogram) a Russian Instagram-like social network with posts, comments, follows, and stories.

## Quick Start
```python
from grustnogram import GrustnoGram

grustnogram = GrustnoGram()
grustnogram.login(email="example@gmail.com", password="password")

# Get your profile
print(grustnogram.get_current_session())
```

---

## Authentication

| Method | Description |
|--------|-------------|
| `login(email, password)` | Sign in and store access token |
| `register(nickname, email, password)` | Create a new account |
| `reset_password(email)` | Send a password reset email |
| `change_password(old_password, new_password)` | Change your password |
| `get_phone_activation_code(phone_key, phone_number)` | Request phone activation code |
| `activate_phone(phone_number, activation_code)` | Verify phone number |

---

## Profile

| Method | Description |
|--------|-------------|
| `get_current_session()` | Get current user's profile |
| `get_user_info(nickname)` | Get a user's public profile |
| `edit_profile(nickname, name, about, avatar)` | Update your profile |
| `search_user(query)` | Search users by query |
| `get_users_list(top)` | Get top users list |

---

## Posts

| Method | Description |
|--------|-------------|
| `create_post(text, image, post_filter)` | Create a new post with an image |
| `edit_post(post_id, text)` | Edit a post's text |
| `delete_post(post_id)` | Delete a post |
| `get_posts_list(post_type)` | Get posts feed |
| `get_user_posts(user_id, limit, offset)` | Get posts by a user |
| `like_post(post_id)` | Like a post |
| `unlike_post(post_id)` | Unlike a post |
| `get_post_likes(post_id, offset)` | Get users who liked a post |
| `report_post(post_id, report_type)` | Report a post |

---

## Comments

| Method | Description |
|--------|-------------|
| `comment_post(post_id, comment, reply_to)` | Post a comment |
| `delete_comment(comment_id)` | Delete a comment |
| `get_post_comments(post_id, offset)` | Get comments on a post |
| `like_comment(comment_id)` | Like a comment |
| `unlike_comment(comment_id)` | Unlike a comment |
| `report_comment(comment_id)` | Report a comment |

---

## Users

| Method | Description |
|--------|-------------|
| `follow_user(user_id)` | Follow a user |
| `unfollow_user(user_id)` | Unfollow a user |
| `get_user_followers(user_id)` | Get a user's followers |
| `get_user_followings(user_id)` | Get who a user follows |
| `block_user(user_id)` | Block a user |
| `unblock_user(user_id)` | Unblock a user |
| `report_user(user_id, report_type)` | Report a user |

---

## Misc

| Method | Description |
|--------|-------------|
| `get_notifications()` | Get your notifications |
| `get_status()` | Get API server status |
| `upload_media(file)` | Upload an image and get its URL |
| `search_post(query)` | Search posts by query |
