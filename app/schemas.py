from datetime import datetime
from typing import List

from pydantic import BaseModel, HttpUrl


class AlternativeSlugs(BaseModel):
    en: str | None = None
    es: str | None = None
    ja: str | None = None
    fr: str | None = None
    it: str | None = None
    ko: str | None = None
    de: str | None = None
    pt: str | None = None
    id: str | None = None


class Urls(BaseModel):
    raw: HttpUrl
    full: HttpUrl
    regular: HttpUrl
    small: HttpUrl
    thumb: HttpUrl
    small_s3: HttpUrl | None = None


class Links(BaseModel):
    self: HttpUrl
    html: HttpUrl
    download: HttpUrl
    download_location: HttpUrl


class TopicSubmission(BaseModel):
    status: str
    approved_on: datetime | None = None


class TopicSubmissions(BaseModel):
    wallpapers: TopicSubmission | None = None
    act_for_nature: TopicSubmission | None = None
    nature: TopicSubmission | None = None
    travel: TopicSubmission | None = None


class ProfileImage(BaseModel):
    small: HttpUrl
    medium: HttpUrl
    large: HttpUrl


class UserLinks(BaseModel):
    self: HttpUrl
    html: HttpUrl
    photos: HttpUrl
    likes: HttpUrl
    portfolio: HttpUrl


class Social(BaseModel):
    instagram_username: str | None = None
    portfolio_url: HttpUrl | None = None
    twitter_username: str | None = None
    paypal_email: str | None = None


class User(BaseModel):
    id: str
    updated_at: datetime
    username: str
    name: str
    first_name: str
    last_name: str | None = None
    twitter_username: str | None = None
    portfolio_url: HttpUrl | None = None
    bio: str | None = None
    location: str | None = None
    links: UserLinks
    profile_image: ProfileImage
    instagram_username: str | None = None
    total_collections: int
    total_likes: int
    total_photos: int
    total_promoted_photos: int
    total_illustrations: int
    total_promoted_illustrations: int
    accepted_tos: bool
    for_hire: bool
    social: Social


class Exif(BaseModel):
    make: str | None = None
    model: str | None = None
    name: str | None = None
    exposure_time: str | None = None
    aperture: str | None = None
    focal_length: str | None = None
    iso: int | None = None


class Position(BaseModel):
    latitude: float | None = None
    longitude: float | None = None


class Location(BaseModel):
    name: str | None = None
    city: str | None = None
    country: str | None = None
    position: Position


class Meta(BaseModel):
    index: bool


class Tag(BaseModel):
    type: str
    title: str


class Topic(BaseModel):
    id: str
    title: str
    slug: str
    visibility: str


class ImageInfo(BaseModel):
    id: str
    slug: str
    alternative_slugs: AlternativeSlugs
    created_at: datetime
    updated_at: datetime
    promoted_at: datetime | None = None
    width: int
    height: int
    color: str | None = None
    blur_hash: str | None = None
    description: str | None = None
    alt_description: str | None = None
    breadcrumbs: List = []
    urls: Urls
    links: Links
    likes: int
    liked_by_user: bool
    bookmarked: bool
    current_user_collections: List = []
    sponsorship: dict | None = None
    topic_submissions: TopicSubmissions
    asset_type: str
    user: User
    exif: Exif
    location: Location
    meta: Meta
    public_domain: bool
    tags: List[Tag]
    views: int
    downloads: int
    topics: List[Topic]
