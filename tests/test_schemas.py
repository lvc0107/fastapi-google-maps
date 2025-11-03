from datetime import datetime

from pydantic import HttpUrl

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
from tests.factories.schemas import (
    AlternativeSlugsFactory,
    ExifFactory,
    ImageInfoFactory,
    LinksFactory,
    LocationFactory,
    MetaFactory,
    PositionFactory,
    ProfileImageFactory,
    SocialFactory,
    TagFactory,
    TopicFactory,
    TopicSubmissionFactory,
    TopicSubmissionsFactory,
    UrlsFactory,
    UserFactory,
    UserLinksFactory,
)


class TestImageInfo:
    def test__image_info(self):
        image_info_data = ImageInfoFactory.build()
        image_info = ImageInfo(**image_info_data.model_dump())

        assert image_info.id == image_info_data.id
        assert isinstance(image_info.id, str)

        assert image_info.slug == image_info_data.slug
        assert isinstance(image_info.slug, str)

        assert image_info.alternative_slugs == image_info_data.alternative_slugs
        assert isinstance(image_info.alternative_slugs, AlternativeSlugs)

        assert image_info.created_at == image_info_data.created_at
        assert isinstance(image_info.created_at, datetime)

        assert image_info.updated_at == image_info_data.updated_at
        assert isinstance(image_info.updated_at, datetime)

        # promoted_at can be None
        if image_info_data.promoted_at is None:
            assert image_info.promoted_at is None
        else:
            assert image_info.promoted_at == image_info_data.promoted_at
            assert isinstance(image_info.promoted_at, datetime)

        assert image_info.width == image_info_data.width
        assert isinstance(image_info.width, int)

        assert image_info.height == image_info_data.height
        assert isinstance(image_info.height, int)

        if not image_info_data.color:
            assert image_info.color is None
        else:
            assert image_info.color == image_info_data.color
            assert isinstance(image_info.color, str)

        if not image_info_data.blur_hash:
            assert image_info.blur_hash is None
        else:
            assert image_info.blur_hash == image_info_data.blur_hash
            assert isinstance(image_info.blur_hash, str)

        if image_info_data.description is None:
            assert image_info.description is None
        else:
            assert image_info.description == image_info_data.description
            assert isinstance(image_info.description, str)

        if image_info_data.alt_description is None:
            assert image_info.alt_description is None
        else:
            assert image_info.alt_description == image_info_data.alt_description
            assert isinstance(image_info.alt_description, str)

        assert image_info.breadcrumbs == image_info_data.breadcrumbs
        assert isinstance(image_info.breadcrumbs, list)

        assert image_info.urls == image_info_data.urls
        assert isinstance(image_info.urls, Urls)

        assert image_info.links == image_info_data.links
        assert isinstance(image_info.links, Links)

        assert image_info.likes == image_info_data.likes
        assert isinstance(image_info.likes, int)

        assert image_info.liked_by_user == image_info_data.liked_by_user
        assert isinstance(image_info.liked_by_user, bool)

        assert image_info.bookmarked == image_info_data.bookmarked
        assert isinstance(image_info.bookmarked, bool)

        assert image_info.current_user_collections == image_info_data.current_user_collections
        assert isinstance(image_info.current_user_collections, list)

        assert image_info.sponsorship == image_info_data.sponsorship
        assert (image_info.sponsorship is None) or isinstance(image_info.sponsorship, dict)

        assert image_info.topic_submissions == image_info_data.topic_submissions
        assert isinstance(image_info.topic_submissions, TopicSubmissions)

        assert image_info.asset_type == image_info_data.asset_type
        assert isinstance(image_info.asset_type, str)

        assert image_info.user == image_info_data.user
        assert isinstance(image_info.user, User)

        assert image_info.exif == image_info_data.exif
        assert isinstance(image_info.exif, Exif)

        assert image_info.location == image_info_data.location
        assert isinstance(image_info.location, Location)

        assert image_info.meta == image_info_data.meta
        assert isinstance(image_info.meta, Meta)

        assert image_info.public_domain == image_info_data.public_domain
        assert isinstance(image_info.public_domain, bool)

        assert image_info.tags == image_info_data.tags
        assert isinstance(image_info.tags, list)
        if image_info.tags:
            for tag in image_info.tags:
                assert isinstance(tag, Tag)

        assert image_info.views == image_info_data.views
        assert isinstance(image_info.views, int)

        assert image_info.downloads == image_info_data.downloads
        assert isinstance(image_info.downloads, int)

        assert image_info.topics == image_info_data.topics
        assert isinstance(image_info.topics, list)
        if image_info.topics:
            for topic in image_info.topics:
                assert isinstance(topic, Topic)


class TestAlternativeSlugs:
    def test__alternative_slugs(self):
        data = AlternativeSlugsFactory.build()
        obj = AlternativeSlugs(**data.model_dump())
        for field in ("en", "es", "ja", "fr", "it", "ko", "de", "pt", "id_country"):
            val = getattr(data, field)
            if val is None:
                assert getattr(obj, field) is None
            else:
                assert getattr(obj, field) == val
                assert isinstance(getattr(obj, field), str)


class TestUrls:
    def test__urls(self):
        data = UrlsFactory.build()
        obj = Urls(**data.model_dump())
        for field in ("raw", "full", "regular", "small", "thumb"):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), HttpUrl)

        # small_s3 may be None
        if data.small_s3 is None:
            assert obj.small_s3 is None
        else:
            assert obj.small_s3 == data.small_s3
            assert isinstance(obj.small_s3, HttpUrl)


class TestLinks:
    def test__links(self):
        data = LinksFactory.build()
        obj = Links(**data.model_dump())
        for field in ("self", "html", "download", "download_location"):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), HttpUrl)


class TestTopicSubmission:
    def test__topic_submission(self):
        data = TopicSubmissionFactory.build()
        obj = TopicSubmission(**data.model_dump())
        assert obj.status == data.status
        assert isinstance(obj.status, str)
        # approved_on may be None
        if data.approved_on is None:
            assert obj.approved_on is None
        else:
            assert obj.approved_on == data.approved_on
            assert isinstance(obj.approved_on, datetime)


class TestTopicSubmissions:
    def test__topic_submissions(self):
        data = TopicSubmissionsFactory.build()
        obj = TopicSubmissions(**data.model_dump())
        # fields may be None or TopicSubmission
        for field in ("wallpapers", "act_for_nature", "nature", "travel"):
            val = getattr(data, field)
            if val is None:
                assert getattr(obj, field) is None
            else:
                assert isinstance(getattr(obj, field), TopicSubmission)


class TestProfileImage:
    def test__profile_image(self):
        data = ProfileImageFactory.build()
        obj = ProfileImage(**data.model_dump())
        for field in ("small", "medium", "large"):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), HttpUrl)


class TestUserLinks:
    def test__user_links(self):
        data = UserLinksFactory.build()
        obj = UserLinks(**data.model_dump())
        for field in ("self", "html", "photos", "likes", "portfolio"):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), HttpUrl)


class TestSocial:
    def test__social(self):
        data = SocialFactory.build()
        obj = Social(**data.model_dump())
        for field in ("instagram_username", "twitter_username", "paypal_email"):
            if getattr(data, field) is None:
                assert getattr(obj, field) is None
            else:
                assert getattr(data, field) == getattr(obj, field)
                assert isinstance(getattr(obj, field), str)
        if obj.portfolio_url is None:
            assert obj.portfolio_url is None
        else:
            assert obj.portfolio_url == data.portfolio_url
            assert isinstance(obj.portfolio_url, HttpUrl)


class TestUser:
    def test__user(self):
        data = UserFactory.build()
        obj = User(**data.model_dump())
        for field in ("id", "username", "name", "first_name"):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), str)

        for field in ("last_name", "twitter_username", "bio", "location", "instagram_username"):
            if getattr(data, field) is None:
                assert getattr(obj, field) is None
            else:
                assert getattr(data, field) == getattr(obj, field)
                assert isinstance(getattr(obj, field), str)

        for field in (
            "total_collections",
            "total_likes",
            "total_photos",
            "total_promoted_photos",
            "total_illustrations",
            "total_promoted_illustrations",
        ):
            assert getattr(data, field) == getattr(obj, field)
            assert isinstance(getattr(obj, field), int)

        assert obj.updated_at == data.updated_at
        assert isinstance(obj.updated_at, datetime)
        assert obj.links == data.links
        assert isinstance(obj.links, UserLinks)
        assert obj.profile_image == data.profile_image
        assert isinstance(obj.profile_image, ProfileImage)
        if obj.portfolio_url is None:
            assert obj.portfolio_url is None
        else:
            assert obj.portfolio_url == data.portfolio_url
            assert isinstance(obj.portfolio_url, HttpUrl)
        assert obj.social == data.social
        assert isinstance(obj.social, Social)

        assert obj.accepted_tos == data.accepted_tos
        assert isinstance(obj.accepted_tos, bool)
        assert obj.for_hire == data.for_hire
        assert isinstance(obj.for_hire, bool)


class TestExif:
    def test__exif(self):
        data = ExifFactory.build()
        obj = Exif(**data.model_dump())
        # all fields optional; if present check types
        for attr in ("make", "model", "name", "exposure_time", "aperture", "focal_length"):
            val = getattr(data, attr)
            if val is None:
                assert getattr(obj, attr) is None
            else:
                assert getattr(obj, attr) == val
                assert isinstance(getattr(obj, attr), str)
        if data.iso is None:
            assert obj.iso is None
        else:
            assert obj.iso == data.iso
            assert isinstance(obj.iso, int)


class TestPosition:
    def test__position(self):
        pos = PositionFactory.build()
        p_obj = Position(**pos.model_dump())
        if pos.latitude is None:
            assert p_obj.latitude is None
        else:
            assert isinstance(p_obj.latitude, float)
        if pos.longitude is None:
            assert p_obj.longitude is None
        else:
            assert isinstance(p_obj.longitude, float)


class TestLocation:
    def test__location(self):
        data = LocationFactory.build()
        obj = Location(**data.model_dump())
        assert obj.position == data.position
        assert isinstance(obj.position, Position)
        for attr in ("name", "city", "country"):
            val = getattr(data, attr)
            if val is None:
                assert getattr(obj, attr) is None
            else:
                assert getattr(obj, attr) == val
                assert isinstance(getattr(obj, attr), str)


class TestMeta:
    def test__meta(self):
        data = MetaFactory.build()
        obj = Meta(**data.model_dump())
        assert obj.index == data.index
        assert isinstance(obj.index, bool)


class TestTag:
    def test__tag(self):
        data = TagFactory.build()
        obj = Tag(**data.model_dump())
        assert obj.type == data.type
        assert isinstance(obj.type, str)
        assert obj.title == data.title
        assert isinstance(obj.title, str)


class TestTopic:
    def test__topic(self):
        data = TopicFactory.build()
        obj = Topic(**data.model_dump())
        for attr in ("id", "title", "slug", "visibility"):
            val = getattr(data, attr)
            assert getattr(obj, attr) == val
            assert isinstance(getattr(obj, attr), str)
