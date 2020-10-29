
# def get_admin_password():
#     return "1234"

# def secure_function(func):
#     if user["access_level"] == "admin":
#         return func

# # user = {"username": "jose", "access_level": "guest"}
# user = {"username": "bob", "access_level": "admin"}
# get_admin_password = secure_function(get_admin_password)


# print(get_admin_password()) # originalrint(admin_password()) # admin version
@make_secure
def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()

    return secure_function

get_admin_password = make_secure(
    get_admin_password
)  # `get_admin_password` is now `secure_func` from above

user = {"username": "jose", "access_level": "guest"}
print(get_admin_password())  # Now we check access level

user = {"username": "bob", "access_level": "admin"}
print(get_admin_password())  # Now we check access level


================

decorator


@login_required("ADMIN")
@nonzerobalance("SAVINGS_ACCOUNT")
def withdraw():
    # current bal - withdraw bal


    

