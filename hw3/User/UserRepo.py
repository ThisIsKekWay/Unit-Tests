from User import User


class UserRepository:
    def __init__(self, users: list[User] = None):
        self._users = users
        if users is None:
            self._users = []

    @property
    def users(self):
        return self._users

    def add_user(self, user: User) -> None:
        if user.is_authenticate:
            self._users.append(user)

    def logout_not_admins(self) -> None:
        i = 0
        while i < len(self._users):
            if not self._users[i].is_admin:
                self._users[i].unauthenticate()
                self._users.remove(self._users[i])
                i -= 1
            i += 1
