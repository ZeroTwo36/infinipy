from datetime import datetime
from infinipy.fetch import fetch
from collections import namedtuple
from PIL import Image

API_URL = "https://api.infinitybotlist.com"


class Bot:
    def __init__(self, **json):
        self.dbid = json.get("_id")
        self.additional_owners = [User(**fetch(f"{API_URL}/users/{x}").json()) for x in json.get("additional_owners")]
        self.announce = json.get("announce")
        self.announce_message = json.get("announce_message")
        self.approval_note = json.get("approval_note")
        self.avatar_url = json.get("avatar")
        self.avatar = Asset(fetch(self.avatar_url))
        self.banner_url = json.get("banner")
        self.banner = Asset(fetch(self.banner_url))
        self.id = int(json.get("bot_id"))
        self.cert_reason = json.get("cert_reason")
        self.certified = json.get("certified")
        self.cert_reason = json.get("claimed")
        self.claimed_by = User(**fetch(json.get("claimed_by")).json())
        self.cross_add = json.get("cross_add")
        self.date = json.get("date")
        self.donate = json.get("donate")
        self.external_source = json.get("external_source")
        self.github = json.get("github")
        self.invite = json.get("invite")
        self.invite_count = json.get("invites")
        self.library = json.get("library")
        self.list_source = json.get("list_source")
        tmp = namedtuple("descriptions", "short", "long")
        self.description = tmp(json.get("short"), json.get("long"))
        self.name = json.get("name")
        self.nsfw = json.get("nsfw")
        self.owner = User(**fetch(f"{API_URL}/users/{json.get('owner')}").json())
        self.pending_cert = json.get("pending_cert")
        self.prefix = json.get("prefix")
        self.has_premium = json.get("premium")
        self.premium_length = json.get("premium_period_length")
        self.servers = json.get("servers")
        self.shards = json.get("shards")
        self.staff = json.get("staff_bot")
        self.premium_start_period = json.get("start_premium_period")
        self.support = json.get("support")
        self.tags = json.get("tags")
        self.servers = json.get("servers")
        self.total_uptime = json.get("total_uptime")
        self.type = json.get("type")
        self.uptime = json.get("uptime")
        self.users = json.get("users")
        self.vanity = json.get("vanity")
        self.views = json.get("views")
        self.voteban = json.get("vote_banned")
        self.votes = json.get("votes")
        self.website = json.get("website")

    def set_stats(self, servers, shards, auth):
        return fetch(f"{API_URL}/bots/stats", body={"servers": servers, "shards": shards},
                     headers={"Authorization": f"{auth}"})

    @property
    def reviews(self):
        reviews = fetch(f"{API_URL}/bots/{self.id}/reviews").json()
        for r in reviews:
            yield Review(self, **r)


class Asset:
    def __init__(self, content):
        self.read = content

    def save(self, filename):
        self.to_imag().save(filename)

    def to_imag(self):
        import io
        return Image.open(io.BytesIO(self.read))


class User:
    def __init__(self, **json):
        self.dbid = json.get("_id")
        self.admin = json.get("admin")
        self.bio = json.get("bio")
        self.certified = json.get("certified")
        self.developer = json.get("developer")
        self.github = json.get("github")
        self.new_staff_stats = json.get("new_staff_stats")
        self.packvotes = json.get("pack_votes")
        self.staff = json.get("staff")
        self.staff_stats = json.get("staff_stats")
        self.id = json.get("user_id")
        self.voteban = json.get("vote_banned")
        self.website = json.get("website")
        self.nickname = json.get("nickname")


class Review:
    def __init__(self, bot, **json):
        self.dbit = json.get("_id")
        self.author = json.get("author")
        self.bot = bot
        self.content = json.get("content")
        self.date = json.get("date")
        self.dislikes = json.get("votes")
        self.edited = json.get("editted")
        self.flagged = json.get("flagged")
        self.likes = json.get("likes")
        self.rate = json.get("rate")
        self.replies = json.get("replies")
        self.stars = json.get("stars")


class Announcement:
    def __init__(self, _id, author, content, id, last_modified, status, target, targetted, title):
        self._id = _id
        self.author = author
        self.content = content
        self.id = id
        self.last_modified = datetime.strptime(last_modified, "%Y-%m-%dT%H:%M:%SZ")
        self.status = status
        self.target = target
        self.targetted = targetted
        self.title = title
