from polyfactory.factories.pydantic_factory import ModelFactory

from app.schemas import (
    AlternativeSlugs,
    Exif,
    ImageInfo,
    Links,
    Location,
    Meta,
    Position,
    ProfileImage,
    Social,
    Tag,
    Topic,
    TopicSubmission,
    TopicSubmissions,
    Urls,
    User,
    UserLinks,
)


class AlternativeSlugsFactory(ModelFactory[AlternativeSlugs]):
    __model__ = AlternativeSlugs


class UrlsFactory(ModelFactory[Urls]):
    __model__ = Urls


class LinksFactory(ModelFactory[Links]):
    __model__ = Links


class TopicSubmissionFactory(ModelFactory[TopicSubmission]):
    __model__ = TopicSubmission


class TopicSubmissionsFactory(ModelFactory[TopicSubmissions]):
    __model__ = TopicSubmissions


class ProfileImageFactory(ModelFactory[ProfileImage]):
    __model__ = ProfileImage


class UserLinksFactory(ModelFactory[UserLinks]):
    __model__ = UserLinks


class SocialFactory(ModelFactory[Social]):
    __model__ = Social


class UserFactory(ModelFactory[User]):
    __model__ = User


class ExifFactory(ModelFactory[Exif]):
    __model__ = Exif


class PositionFactory(ModelFactory[Position]):
    __model__ = Position


class LocationFactory(ModelFactory[Location]):
    __model__ = Location


class MetaFactory(ModelFactory[Meta]):
    __model__ = Meta


class TagFactory(ModelFactory[Tag]):
    __model__ = Tag


class TopicFactory(ModelFactory[Topic]):
    __model__ = Topic


class ImageInfoFactory(ModelFactory[ImageInfo]):
    __model__ = ImageInfo
