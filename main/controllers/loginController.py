class loginController():
    def checkLoginDetails(users,user):
        if user in users:
            return True
        else:
            return False