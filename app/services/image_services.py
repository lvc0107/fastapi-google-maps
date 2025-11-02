#
# class ImageService:
#     def save_image_to_db(self, image_info: ImageInfo):
#         user_repo = UserRepository()
#         tag_repo = TagRepository()
#         photo_repo = PhotoRepository()
#         if not (user := user_repo.get(image_info.user)):
#             user = User(
#                 id=user_data["id"],
#                 username=user_data["username"],
#                 name=user_data.get("name"),
#                 portfolio_url=user_data.get("portfolio_url"),
#             )
#             session.add(user)
#
#         # Handle photo
#         photo = Photo(
#             id=data["id"],
#             created_at=data.get("created_at", datetime.now(UTC)),
#             description=data.get("description"),
#             alt_description=data.get("alt_description"),
#             url_full=data["urls"]["full"],
#             url_thumb=data["urls"]["thumb"],
#             user=user,
#         )
#         session.add(photo)
#
#         # Handle tags
#         for tag_data in data.get("tags", []):
#             tag = Tag(title=tag_data["title"], photo=photo)
#             session.add(tag)
#
#         session.commit()
