

class User:
    def get_by_id(self, _id: int) -> dict:
        return {"_id": _id, "name": "Roman"}

    def get_by_users_list(self, user_id: int) -> list[dict]: ...

    def create(self, name: str) -> dict:
        return {"_id": 1, "name": name}

    def update(self, _id: int, name: str) -> dict: ...

    def delete(self, _id: int) -> None: ...


class Post:
    def get_by_id(self, _id: int) -> dict: ...

    def get_by_user_id(self, user_id: int) -> list[dict]: ...

    def create(self, content: str) -> dict: ...

    def update(self, _id: int, content: str) -> dict: ...

    def delete(self, _id: int) -> None: ...