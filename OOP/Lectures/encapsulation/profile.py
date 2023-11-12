class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if len(username) < 5 or len(username) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')
        else:
            self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        else:
            self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {len(self.password)*"*"}.'
