from app.model import Photo, Tag, User


class TagRepository:
    def get(self, tag_id: str):
        pass

    def add(self, tag: Tag):
        pass


class PhotoRepository:
    def get(self, photo_id: str):
        pass

    def add(self, photo: Photo):
        pass


class UserRepository:
    def get(self, user_id: str):
        pass

    def add(self, user: User):
        pass
