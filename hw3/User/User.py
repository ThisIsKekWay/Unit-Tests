class User:
    def __init__(self, login: str, password: str, is_admin: bool = False):
        self._login = login
        self._password = password
        self._is_admin = is_admin
        self._is_authenticate = False

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def is_authenticate(self):
        return self._is_authenticate

    def authenticate(self, login: str, password: str) -> bool:
        self._is_authenticate = self.login == login and self.password == password
        return self.is_authenticate

    def unauthenticate(self):
        self._is_authenticate = False

    def __eq__(self, other):
        return self.login == other.login

    def __hash__(self):
        return hash((self.login, self.password, self.is_authenticate))

    def __repr__(self):
        return f'User("{self.login}", is_admin={self.is_admin})'
