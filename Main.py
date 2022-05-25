from user import User
from post import Post

app_user_one = User("na@na.com", "First Last", "pwd1", "engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Dev Ops")
app_user_one.get_user_info()

new_post = Post("Your Message Here", app_user_one.name)
new_post.get_post_info()