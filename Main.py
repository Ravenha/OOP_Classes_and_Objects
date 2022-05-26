from user import User
from post import Post


# If this file is ever imported, this code should only run when
# explicitly told to. To enable this functionality, we encapsulate
# in a function and call it only if this is the entry file
# e.g. "python3 Main.py" ; as opposed to "import Main.py"
def main():
    app_user_one = User("na@na.com", "First Last", "pwd1", "engineer")
    app_user_one.get_user_info()

    app_user_one.change_job_title("Dev Ops")
    app_user_one.get_user_info()

    new_post = Post("Your Message Here", app_user_one.name)
    new_post.get_post_info()


# __name__ is the name of the current module. The file used as the
# entry-point gets a special name, however, which is "__main__".
# So to check if the code should run, we check if this file is
# the entry-point.
if __name__ == '__main__':
    main()